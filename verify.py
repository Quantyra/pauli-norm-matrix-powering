"""Bounded dense checks of the coherent clock input, Clifford signs, and finite-bit margins."""

from cmath import exp
from itertools import product
import json
from math import pi, sqrt, trunc


def identity(size):
    return [[int(i == j) for j in range(size)] for i in range(size)]


def adjoint(a):
    return [[v.conjugate() for v in col] for col in zip(*a)]


def multiply(a, b):
    cols = list(zip(*b))
    return [[sum(x * y for x, y in zip(row, col)) for col in cols] for row in a]


def power(a, degree):
    result = identity(len(a))
    while degree:
        if degree & 1:
            result = multiply(result, a)
        degree //= 2
        if degree:
            a = multiply(a, a)
    return result


def difference(a, b):
    return max(abs(v - w) for row, other in zip(a, b) for v, w in zip(row, other))


def pauli_phase(x, z, j):
    return (1j ** ((x & z).bit_count() % 4)) * (-1) ** ((z & j).bit_count() % 2)


def coefficients(a):
    size = len(a)
    terms = []
    for x, z in product(range(size), repeat=2):
        value = sum(pauli_phase(x, z, j).conjugate() * a[j ^ x][j]
                    for j in range(size)) / size
        assert abs(value.imag) < 1e-12
        if abs(value.real) > 1e-14:
            terms.append((x, z, value.real))
    return terms


def expand(size, terms):
    out = [[0j] * size for _ in range(size)]
    for x, z, coefficient in terms:
        for j in range(size):
            out[j ^ x][j] += coefficient * pauli_phase(x, z, j)
    return out


def apply_clock(vector, tape):
    work = len(tape[0])
    result = [0j] * len(vector)
    for a, gate in enumerate(tape):
        target = (a + 1) % len(tape)
        for i in range(work):
            result[target * work + i] = sum(
                gate[i][j] * vector[a * work + j] for j in range(work)
            )
    return result


def check_case(name, gates, z, expected, reciprocal_d):
    work = len(gates[0])
    circuit = identity(work)
    for gate in gates:
        circuit = multiply(gate, circuit)
    p = sum(abs(circuit[k][z]) ** 2 for k in range(1, work, 2))
    assert abs(p - expected) < 1e-12

    reflection = [[(1 if i % 2 else -1) if i == j else 0
                   for j in range(work)] for i in range(work)]
    program = gates + [reflection] + [adjoint(gate) for gate in reversed(gates)]
    M = 1 << (max(4, 2 * len(program)) - 1).bit_length()
    L = M // 2
    tape = [identity(work)] * L + program + [identity(work)] * (L - len(program))
    size = M * work

    # W^(2M) = I. Its period average projects onto eigenvalue +1.
    initial = [1 / sqrt(L) if i // work < L and i % work == z else 0
               for i in range(size)]
    vector = initial
    projected = [0j] * size
    for _ in range(2 * M):
        for i, value in enumerate(vector):
            projected[i] += value / (2 * M)
        vector = apply_clock(vector, tape)
    assert max(abs(x - y) for x, y in zip(initial, vector)) < 1e-12
    weight = sum(abs(v) ** 2 for v in projected)
    assert abs(weight - p / 2) < 1e-12

    w = [[0j] * size for _ in range(size)]
    for a, gate in enumerate(tape):
        for i, j in product(range(work), repeat=2):
            w[((a + 1) % M) * work + i][a * work + j] = gate[i][j]
    a_matrix = [[(w[i][j] + w[j][i].conjugate()) / 2 for j in range(size)]
                for i in range(size)]
    raw_terms = coefficients(a_matrix)
    mask = (L - 1) * work
    after_clifford = []
    for x, zmask, value in raw_terms:
        exchanged_bits = (x ^ zmask) & mask
        sign = (-1) ** ((x & zmask & mask).bit_count() % 2)
        after_clifford.append((x ^ exchanged_bits, zmask ^ exchanged_bits, sign * value))
    assert sum(abs(v) for _, _, v in raw_terms) == sum(abs(v) for _, _, v in after_clifford)
    # Direct clock Hadamards give a second implementation of that conjugation.
    q = [[(-1) ** ((i & j & mask).bit_count() % 2) / sqrt(L) if (i ^ j) & ~mask == 0 else 0
          for j in range(size)] for i in range(size)]
    assert difference(expand(size, after_clifford), multiply(multiply(q, a_matrix), q)) < 1e-12

    s = 1 / (2 * M * reciprocal_d)
    m = 6 * M ** 3 * reciprocal_d
    tau = 1 / (1 << (256 * m - 1).bit_length())
    terms = {(x, zmask): s * value for x, zmask, value in after_clifford}
    terms[0, 0] = terms.get((0, 0), 0) + 1 - s
    mesh_denom = 1 << (2 * len(terms) * round(1 / tau) - 1).bit_length()
    rounded = [(x, zmask, trunc((1 - tau) * value * mesh_denom) / mesh_denom)
               for (x, zmask), value in terms.items()]
    coefficient_mass = sum(abs(v) for _, _, v in rounded)
    assert coefficient_mass <= 1 + 1 / reciprocal_d
    rounding_mass = sum(abs(value - (1 - tau) * terms[x, zmask])
                        for x, zmask, value in rounded)
    assert rounding_mass <= tau / 2
    observed = power(expand(size, rounded), m)[z][z]
    assert abs(observed.imag) < 1e-10
    assert p / 2 - 3 / 512 <= observed.real <= p / 2 + 1 / 256 + 3 / 512
    if p >= 2 / 3:
        assert observed.real > 9 / 32
    if p <= 1 / 3:
        assert observed.real < 7 / 32
    return dict(case=name, reciprocal_d=reciprocal_d, clock=M, power=m, acceptance=p,
                projected_weight=weight, rounded_diagonal=observed.real, pauli_mass=coefficient_mass)


def main():
    h = [[1 / sqrt(2), 1 / sqrt(2)], [1 / sqrt(2), -1 / sqrt(2)]]
    t = [[1, 0], [0, exp(1j * pi / 4)]]
    high_h = [[h[i // 2][j // 2] if i % 2 == j % 2 else 0 for j in range(4)]
              for i in range(4)]
    cnot = [[int(i == (j ^ (j >> 1))) for j in range(4)] for i in range(4)]
    cases = [
        ("reject", [identity(2)], 0, 0),
        ("accept", [identity(2)], 1, 1),
        ("complex-no", [h, t, h], 0, (2 - sqrt(2)) / 4),
        ("complex-yes", [h, t, h], 1, (2 + sqrt(2)) / 4),
        ("entangled-half", [high_h, cnot], 0, 0.5),
    ]
    print(json.dumps({"scope": "supplementary floating-point checks, independent of uniform proof",
                      "cases": [check_case(*case, reciprocal_d)
                                for reciprocal_d in (2, 1024) for case in cases]}, indent=2))


if __name__ == "__main__":
    main()
