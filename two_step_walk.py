"""Rows and single-trial scores for the two-step matrix-power walk.

The CLI reads the S317 Pauli JSON format and prints the exact nonzero entries
of the squared matrix's row at 'basis'. Each value is [real, imaginary].
"""

from fractions import Fraction
import json
import secrets
import sys

from estimate_pauli_power import cumulative_table, draw, read_instance, signed_pauli


def prepare(terms):
    denominator = max((v.denominator for v in terms.values()), default=1)
    labels = []
    for label, value in terms.items():
        flip, parity, phase = signed_pauli(label, value)
        mass = abs(value.numerator) * (denominator // value.denominator)
        labels.append((flip, parity, phase, mass))
    return labels, denominator


def two_step_row(x, prepared):
    labels, denominator = prepared
    totals = {}
    for flip, parity, phase, mass in labels:
        z = x ^ flip
        left_phase = phase + 2 * (x & parity).bit_count()
        for other_flip, other_parity, other_phase, other_mass in labels:
            y = z ^ other_flip
            # signed_pauli gives the action on a ket. Conjugate to obtain a row.
            exponent = -(left_phase + other_phase + 2 * (z & other_parity).bit_count()) % 4
            value = mass * other_mass
            pair = totals.setdefault(y, [0, 0])
            pair[exponent % 2] += value if exponent < 2 else -value
    scale = denominator**2
    return {y: (Fraction(re, scale), Fraction(im, scale))
            for y, (re, im) in totals.items() if re or im}


def trial(prepared, start, power, retries, randbits=secrets.randbits):
    """Return the real score. draw raises DrawLimit on exhaustion of the cap."""
    if power < 2 or power % 2:
        raise ValueError("an even positive power is required")
    x = start
    re, im = Fraction(1), Fraction(0)
    for _ in range(power // 2):
        row = two_step_row(x, prepared)
        if not row:
            return Fraction(0)
        endpoints = list(row)
        masses = [abs(a) + abs(b) for a, b in row.values()]
        idx = draw(cumulative_table(masses), retries, randbits)
        x = endpoints[idx]
        a, b = row[x]
        multiplier = sum(masses) / masses[idx]
        re, im = (re*a - im*b) * multiplier, (re*b + im*a) * multiplier
    return re if x == start else Fraction(0)


if __name__ == "__main__":
    x, _, terms = read_instance(json.load(sys.stdin))
    row = two_step_row(x, prepare(terms))
    print(json.dumps({str(y): [str(a), str(b)] for y, (a, b) in sorted(row.items())}))
