"""Check the first matched pair by collecting actual Pauli coefficients, then forming B^2.

All emitted coefficients and B entries use integer units of eta. B^2 entries
use eta squared. Use real Walsh signs for the Hermitian Pauli labels: a real
symmetric matrix has only even-Y terms, whose remaining Pauli phase is a sign.
"""
from collections import defaultdict
from fractions import Fraction
from functools import cache
from math import isqrt
import json

from verify_chain import installed_rules

TAGS = dict(G=0, R=2, L=4, F=6, U=8, X=9, A=10, V=12, S=14)
DATA = "GRLF"


def walsh(values):
    values = values[:]
    span = 1
    while span < len(values):
        for left in range(0, len(values), 2 * span):
            for i in range(left, left + span):
                a, b = values[i], values[i + span]
                values[i], values[i + span] = a + b, a - b
        span *= 2
    return values


def word(tags, bits):
    number = 0
    data = iter(bits)
    for tag in tags:
        number = 16 * number + TAGS[tag] + (next(data) if tag in DATA else 0)
    return number


@cache
def local_spectrum(left, right, gate, steps):
    """Return real Walsh coefficients before global collection, in three channels.

    Relative to L grid units, the channels are rational/(T+1),
    hadamard/sqrt(2), and marked*sqrt(T)/(T+1).
    """
    width = len(left)
    dimension = 16 ** width
    rows = defaultdict(lambda: [0] * dimension)

    def put(x, y, channel, value):
        rows[(x ^ y, channel)][x] += value

    if gate == "pin":
        put(TAGS["G"], TAGS["G"], 0, -2 * (steps + 1))
    else:
        count = sum(tag in DATA for tag in left)
        for data in range(2 ** count):
            bits = tuple((data >> i) & 1 for i in reversed(range(count)))
            x = word(left, bits)
            if left == "SR":
                y = word(right, (0,) + bits)
                put(x, x, 0, -2)
                put(y, y, 0, -2 * steps)
                put(x, y, 2, 2)
                put(y, x, 2, 2)
                continue
            # Gate-independent diagonal of the propagation projector.
            natural = word(right, bits)
            put(x, x, 0, -(steps + 1))
            put(natural, natural, 0, -(steps + 1))
            if gate == "H":
                exits = [(bits[0:1] + (b,), 1, (-1) ** (bits[1] * b)) for b in (0, 1)]
            elif gate == "CNOT":
                exits = [((bits[0], bits[0] ^ bits[1]), 0, steps + 1)]
            else:
                exits = [(bits, 0, steps + 1)]
            for output, channel, weight in exits:
                y = word(right, output)
                put(x, y, channel, weight)
                put(y, x, channel, weight)

    result = []
    for (flip, channel), row in rows.items():
        for parity, value in enumerate(walsh(row)):
            if value:
                assert (flip & parity).bit_count() % 2 == 0
                result.append((flip, parity, channel, value * (256 // dimension)))
    return result


def slot(site, width, flip, parity):
    used = flip | parity
    if not used:
        return -1, 0, 0, 0
    if width == 2 and used < 16:
        return site + 1, 1, flip, parity
    if width == 2 and used % 16 == 0:
        return site, 1, flip >> 4, parity >> 4
    return site, width, flip, parity


def emit(values, steps, factor):
    rat, had, marked = values
    if had:
        assert not rat and not marked
        magnitude = isqrt((had * factor) ** 2 // 2)
        return magnitude if had > 0 else -magnitude
    if marked:
        assert not rat
        magnitude = isqrt((marked * factor) ** 2 * steps) // (steps + 1)
        return magnitude if marked > 0 else -magnitude
    return (1 if rat >= 0 else -1) * (abs(rat) * factor // (steps + 1))


def compile_rows(n, work, yes):
    size = 7 * n
    steps = 6 * n * (2 * n + 3) + n - 1
    rules = installed_rules(n, 7, True) + [(size - 1, "G", "G")]
    jcount = len(rules)
    assert jcount == 49 * n - 10 and jcount.bit_count() == 1
    power = 144 * (256 * jcount) * steps ** 2
    tau_inv = 1 << (256 * power - 1).bit_length()
    factor = tau_inv - 1
    grid_inv = tau_inv << (4 * (1 + 65536 * jcount) - 1).bit_length()
    assert grid_inv == tau_inv * 2 ** 19 * jcount

    coeffs = defaultdict(lambda: [0, 0, 0])
    hadamard_bonds = {n + w - 2 for w in work}
    for site, left, right in rules:
        gate = "id"
        if left == "G" and right == "G":
            gate = "pin"
        if left == "GR" and site in hadamard_bonds:
            gate = "H"
        if yes and left == "GR" and site == 6 * n - 2:
            gate = "CNOT"
        for flip, parity, channel, value in local_spectrum(left, right, gate, steps):
            coeffs[slot(site, len(left), flip, parity)][channel] += value
    # Global identity shift before the single inward rounding of each string.
    coeffs[(-1, 0, 0, 0)][0] += (steps + 1) * (grid_inv // tau_inv)

    groups = defaultdict(list)
    exceptional_diagonals = 0
    for (site, width, flip, parity), values in coeffs.items():
        if values[0] * factor % (steps + 1):
            assert not flip and site + width <= 2
            exceptional_diagonals += 1
        value = emit(values, steps, factor)
        if value:
            groups[(site, width, flip)].append((parity, value))
    assert exceptional_diagonals > 0

    @cache
    def reconstruct(width, coefficients):
        raw = [0] * (16 ** width)
        for parity, value in coefficients:
            raw[parity] = value
        return walsh(raw)

    # Convert collected and rounded Walsh coefficients back to local rows.
    by_site = defaultdict(list)
    for (site, width, flip), coefficients in groups.items():
        rows = reconstruct(width, tuple(sorted(coefficients)))
        by_site[site, width].append((flip, rows))
    local = []
    for (site, width), flips in by_site.items():
        table = [[(f, vals[x]) for f, vals in flips if vals[x]]
                 for x in range(16 ** width)]
        local.append((site, width, table))

    def row(state):
        acc = defaultdict(int)
        for site, width, table in local:
            if width == 2:
                x = 16 * state[site] + state[site + 1]
            else:
                x = state[site] if width == 1 else 0
            for flip, value in table[x]:
                if flip:
                    y = x ^ flip
                    part = bytes([y]) if width == 1 else bytes(divmod(y, 16))
                    dest = state[:site] + part + state[site+width:]
                else:
                    dest = state
                acc[dest] += value
        return {dest: value for dest, value in acc.items() if value}
    return row, grid_inv, len(coeffs), exceptional_diagonals


def sweep_word(n, sweep, offset, data):
    tags = ["X"] * (sweep * n) + ["L"] * offset + ["G"] + ["R"] * (n - offset - 1)
    tags += ["U"] * (7*n - len(tags))
    result = bytearray(TAGS[t] for t in tags)
    for i, value in enumerate(data):
        result[sweep*n+i] += value
    if sweep == offset == 0:
        assert data[0] == 0
        result[0] = TAGS["S"]
    return bytes(result)


def square(row, x):
    acc = defaultdict(int)
    for z, a in row(x).items():
        for y, b in row(z).items():
            acc[y] += a*b
    return {y: val for y, val in acc.items() if val}


def main():
    n, work = 42, (4, 7)
    no, unit, count_no, diag_no = compile_rows(n, work, False)
    yes, other, count_yes, diag_yes = compile_rows(n, work, True)
    assert other == unit
    data = [0] * n
    data[-2] = 1
    start = sweep_word(n, 0, 0, data)
    assert set(no(start)) == {start, sweep_word(n, 0, 1, data)}
    assert square(no, start) == square(yes, start)

    # At both H cuts check complete one- and two-step support. The conditional
    # exits across each cut have equal magnitude for all four work strings.
    checks = 0
    kernels = {}
    for target in work:
        offset = target - 2
        normalizers = defaultdict(set)
        for assignment in range(4):
            for i, wire in enumerate(work):
                data[wire-1] = assignment >> i & 1
            x = sweep_word(n, 1, offset, data)
            flipped = data[:]
            flipped[target-1] ^= 1
            next_words = {sweep_word(n, 1, offset+1, d) for d in (data, flipped)}
            expected = {x, sweep_word(n, 1, offset-1, data)} | next_words
            one_step = no(x)
            assert set(one_step) == expected
            assert len({abs(one_step[z]) for z in next_words}) == 1
            squared = square(no, x)
            extra = {sweep_word(n, 1, offset-2, data)}
            extra.update(sweep_word(n, 1, offset+2, d) for d in (data, flipped))
            assert set(squared) == expected | extra
            assert len({abs(squared[z]) for z in next_words}) == 1
            assert squared == square(yes, x)
            pre = square(no, sweep_word(n, 1, offset-1, data))
            assert len({abs(pre[z]) for z in next_words}) == 1
            backward = square(no, sweep_word(n, 1, offset+1, data))
            for name, this_row in (("forward", squared), ("forward_two", pre), ("back", backward)):
                normalizers[name].add(sum(map(abs, this_row.values())))
            # Conditional kernel of a backwards two-layer crossing, on the
            # emitted matrix, in the original work-bit coordinates.
            endpoints = [sweep_word(n, 1, offset-1, d) for d in (data, flipped)]
            weights = [abs(backward[z]) for z in endpoints]
            assert weights[0] == weights[1] > 0
            toggle = 1 << work.index(target)
            kernels[target, assignment] = {
                a: Fraction(w, sum(weights))
                for a, w in zip((assignment, assignment ^ toggle), weights)
            }
            before = sweep_word(n, 5, n-4, data)
            assert square(no, before) == square(yes, before)
            near = sweep_word(n, 5, n-3, data)
            end_no = sweep_word(n, 5, n-1, data)
            changed = data[:]
            changed[-1] = 1
            end_yes = sweep_word(n, 5, n-1, changed)
            p, r = square(no, near), square(yes, near)
            assert p[end_no] == r[end_yes] != 0
            assert {z for z in p.keys() | r.keys() if p.get(z) != r.get(z)} == {end_no, end_yes}
            checks += 1
        assert all(len(values) == 1 for values in normalizers.values())
    # Test the last-crossing calculation starting at a late visit, for every
    # incoming data word. The later cut is recrossed twice before reaching the
    # earlier one. Its forward and reverse fair-bit kernels are identical.
    for initial in range(4):
        law = {initial: Fraction(1)}
        for target in (work[1], work[1], work[1], work[0]):
            updated = defaultdict(Fraction)
            for a, prob in law.items():
                for b, transition in kernels[target, a].items():
                    updated[b] += prob * transition
            law = updated
        assert law == {a: Fraction(1, 4) for a in range(4)}
    print(json.dumps(dict(width=n, work_bits=len(work), physical_sites=7*n,
                          collected_slots=[count_no, count_yes],
                          nongrid_diagonal_slots=[diag_no, diag_yes],
                          eta_inverse=str(unit), crossing_and_late_gate_cases=checks,
                          recrossing_final_zero_probability="1/4",
                          marked_start_checked=True), indent=2))


if __name__ == "__main__":
    main()
