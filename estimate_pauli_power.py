"""Fixed-error estimator for an explicitly listed Hermitian Pauli contraction.

Input JSON: {"basis":"0","power_unary":"11","terms":[["X","0.101"],["Z","0.101"]]}.
Coefficients are signed binary fixed-point strings. The example has weight 5/4 and operator
norm 5 sqrt(2)/8. The caller supplies the contraction promise.
"""

from bisect import bisect_right
from fractions import Fraction
from math import ceil, comb, isqrt
import json
import secrets
import sys


def binary_coefficient(text):
    if not isinstance(text, str):
        raise ValueError("use a signed binary fixed-point string")
    sign = -1 if text.startswith("-") else 1
    unsigned = text[1:] if text[:1] in ("-", "+") else text
    whole, point, frac = unsigned.partition(".")
    if not whole or (point and not frac) or any(bit not in "01" for bit in whole + frac):
        raise ValueError("invalid binary coefficient")
    return Fraction(sign * int(whole + frac, 2), 1 << len(frac))


def read_instance(data):
    basis = data["basis"]
    unary = data["power_unary"]
    if not isinstance(basis, str) or not basis or set(basis) - {"0", "1"}:
        raise ValueError("basis must be a nonempty binary string")
    if not isinstance(unary, str) or not unary or set(unary) != {"1"}:
        raise ValueError("power_unary must be a nonempty string of ones")
    terms = {}
    for label, value in data["terms"]:
        if len(label) != len(basis) or set(label) - set("IXYZ"):
            raise ValueError("invalid Pauli label")
        terms[label] = terms.get(label, 0) + binary_coefficient(value)
    return int(basis, 2), len(unary), {p: a for p, a in terms.items() if a}


def power_filter(m, weight):
    """Return the block length and the actual collected monomial coefficients."""
    if weight <= 1:
        return 1, {m: Fraction(1)}
    if weight > Fraction(3, 2):
        raise ValueError("the proved parameter range is Pauli weight at most 3/2")
    block = 1
    mass = weight
    while block < m and mass * weight <= 2:
        block += 1
        mass *= weight
    q, r = divmod(m, block)
    cutoff = min(q, isqrt(12 * q - 1) + 1)
    previous, current = [], [1]  # T_0, with a zero placeholder for its predecessor
    numerator = [0] * (cutoff + 1)
    for k in range(cutoff + 1):
        if (q - k) % 2 == 0:
            count = comb(q, (q - k) // 2) * (2 if k else 1)
            for j, coefficient in enumerate(current):
                numerator[j] += count * coefficient
        if k < cutoff:
            following = [0] + [c * (2 if k else 1) for c in current]
            for j, coefficient in enumerate(previous):
                following[j] -= coefficient
            previous, current = current, following
    return block, {r + block * j: Fraction(c, 1 << q) for j, c in enumerate(numerator) if c}


def cumulative_table(weights):
    """Convert positive dyadic weights to cumulative integer masses."""
    scale = max(w.denominator for w in weights)
    cumulative = []
    total = 0
    for w in weights:
        total += w.numerator * (scale // w.denominator)
        cumulative.append(total)
    return cumulative


class DrawLimit(Exception):
    """A bounded uniform integer draw exhausted its retry allowance."""


def draw(cumulative, retries, randbits):
    total = cumulative[-1]
    if total == 1:
        return 0
    bits = (total - 1).bit_length()
    for _ in range(retries):
        value = randbits(bits)
        if value < total:
            return bisect_right(cumulative, value)
    raise DrawLimit


def signed_pauli(label, coefficient):
    """Masks and phase for i^phase X^flip Z^parity, including coefficient sign."""
    flip = int("".join("1" if p in "XY" else "0" for p in label), 2)
    parity = int("".join("1" if p in "ZY" else "0" for p in label), 2)
    return flip, parity, label.count("Y") + 2 * (coefficient < 0)


def real_diagonal(basis, factors):
    state, phase = basis, 0
    for flip, parity, local_phase in factors:
        phase += local_phase + 2 * ((state & parity).bit_count() % 2)
        state ^= flip
    return (1, 0, -1, 0)[phase % 4] if state == basis else 0


def estimate(data, randbits=secrets.randbits):
    basis, m, terms = read_instance(data)
    if not terms:
        return Fraction(0)
    weight = sum(abs(a) for a in terms.values())
    _, coefficients = power_filter(m, weight)
    degrees = list(coefficients)
    masses = [abs(coefficients[k]) * weight**k for k in degrees]
    total_mass = sum(masses)
    degree_table = cumulative_table(masses)
    factors = [signed_pauli(p, a) for p, a in terms.items()]
    pauli_table = cumulative_table([abs(a) for a in terms.values()])
    samples = max(1, ceil(6 * 64**2 * total_mass**2))
    retries = (12 * samples * (m + 1)).bit_length()
    tally = 0
    try:
        for _ in range(samples):
            degree = degrees[draw(degree_table, retries, randbits)]
            path = (factors[draw(pauli_table, retries, randbits)] for _ in range(degree))
            value = real_diagonal(basis, path)
            tally += value if coefficients[degree] > 0 else -value
    except DrawLimit:
        return Fraction(0)
    mean = min(1, max(-1, total_mass * tally / samples))
    return Fraction(round(256 * mean), 256)


if __name__ == "__main__":
    result = estimate(json.load(sys.stdin))
    print(json.dumps({"numerator": result.numerator, "denominator": result.denominator}))
