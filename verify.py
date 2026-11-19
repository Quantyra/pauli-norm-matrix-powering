"""Full-matrix checks of the cyclic-clock construction at two fixed norm budgets."""
from itertools import product
from math import ceil, log2, sqrt, trunc
from cmath import exp
from math import pi
import json


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


def check_case(name, gates, z, expected_p, reciprocal_d):
    work = len(gates[0])
    circuit = identity(work)
    for gate in gates:
        circuit = multiply(gate, circuit)
    # Accept when the lowest work bit is 1.
    p = sum(abs(circuit[k][z]) ** 2 for k in range(1, work, 2))
    assert abs(p - expected_p) < 1e-12
    reflection = [[(1 if i % 2 else -1) if i == j else 0
                   for j in range(work)] for i in range(work)]
    tape = gates + [reflection] + [adjoint(g) for g in reversed(gates)]
    M = 1 << (max(4, len(tape)) - 1).bit_length()
    tape += [identity(work)] * (M - len(tape))
    size = M * work
    w = [[0j] * size for _ in range(size)]
    for a, gate in enumerate(tape):
        for i, j in product(range(work), repeat=2):
            w[((a + 1) % M) * work + i][a * work + j] = gate[i][j]
    assert difference(multiply(adjoint(w), w), identity(size)) < 1e-12
    a = [[(w[i][j] + w[j][i].conjugate()) / 2 for j in range(size)]
         for i in range(size)]
    terms = coefficients(a)
    assert difference(expand(size, terms), a) < 1e-12
    K = 2 * M
    assert sum(abs(v) for _, _, v in terms) <= K
    s = 1 / (reciprocal_d * K)
    b = [[s * a[i][j] + (1 - s if i == j else 0) for j in range(size)]
         for i in range(size)]
    m = M ** 3 * reciprocal_d * ceil(log2(64 * M))
    tau = 2.0 ** -ceil(log2(128 * m * M))
    terms_b = coefficients(b)
    mesh = 2.0 ** -ceil(log2(2 * len(terms_b) / tau))
    rounded = [(x, y, trunc((1 - tau) * value / mesh) * mesh)
               for x, y, value in terms_b]
    mass = sum(abs(value) for _, _, value in rounded)
    assert mass <= 1 + 1 / reciprocal_d
    out = expand(size, rounded)
    delta = sum(abs(v - rv) for (_, _, v), (_, _, rv) in zip(terms_b, rounded))
    assert delta <= 1.5 * tau + 1e-14
    obs = power(out, m)[z][z]
    assert abs(obs.imag) < 1e-11
    assert p - 3 / 256 - 1e-8 <= M * obs.real <= p + 7 / 256 + 1e-8
    if p >= 2 / 3:
        assert M * obs.real >= 7 / 12
    if p <= 1 / 3:
        assert M * obs.real <= 5 / 12
    return dict(case=name, M=M, dimension=size, reciprocal_d=reciprocal_d, degree=m, pauli_mass=mass,
                p=p, decoded=M * obs.real)


def main():
    h = [[1 / sqrt(2), 1 / sqrt(2)], [1 / sqrt(2), -1 / sqrt(2)]]
    t = [[1, 0], [0, exp(1j * pi / 4)]]
    x = [[0, 1], [1, 0]]
    high_h = [[h[i // 2][j // 2] if i % 2 == j % 2 else 0
               for j in range(4)] for i in range(4)]
    cnot = [[int(i == (j ^ (j >> 1))) for j in range(4)] for i in range(4)]
    cases = [
        ("reject", [identity(2)], 0, 0),
        ("accept", [x], 0, 1),
        ("nonzero-basis-input", [identity(2)], 1, 1),
        ("complex-no", [h, t, h], 0, (2 - sqrt(2)) / 4),
        ("complex-yes", [h, t, h, x], 0, (2 + sqrt(2)) / 4),
        ("entangled-half", [high_h, cnot], 0, 0.5),
    ]
    print(json.dumps({"scope": "supplementary finite floating-point controls",
                      "cases": [check_case(*case, reciprocal_d) for reciprocal_d in (2, 1024)
                                for case in cases]}, indent=2))


if __name__ == "__main__":
    main()
