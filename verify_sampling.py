"""Finite checks for the weighted sampling results. The success probability and asymptotic bounds are analytic."""

from fractions import Fraction as F
from itertools import product
from math import comb, isqrt
from pathlib import Path
from random import Random
import json
import subprocess
import sys

from verify_chain import installed_rules
from estimate_pauli_power import estimate, power_filter, read_instance, real_diagonal, signed_pauli


def check_filters():
    count = truncated = 0
    for lam in (F(1), F(1025, 1024), F(9, 8), F(5, 4), F(3, 2)):
        for m in (1, 2, 3, 8, 17, 32, 65, 95, 128, 257):
            block, coeff = power_filter(m, lam)
            q = m // block
            cutoff = min(q, isqrt(12 * q - 1) + 1) if lam > 1 else q
            assert max(coeff) <= m
            if lam > 1:
                assert lam**block <= 2 and (block == m or lam**(block + 1) > 2)
            tail = sum(F(comb(q, a), 2**q) for a in range(q+1) if abs(2*a-q) > cutoff)
            assert 1 - sum(coeff.values()) == tail < F(1, 128)
            truncated += bool(tail)
            for x in (F(-1), F(-5, 8), F(0), F(3, 4), F(1)):
                assert abs(sum(v * x**k for k, v in coeff.items()) - x**m) <= tail
            assert sum(abs(a) * lam**k for k, a in coeff.items()) <= 2 * 5**cutoff
            count += 1
    return count, truncated


def check_paths():
    # A = (X - Y + Z)/2 is a contraction, A^2 = 3I/4.
    terms = [signed_pauli(p, c) for p, c in zip("XYZ", [1, -1, 1])]
    checked = 0
    for basis, m in product((0, 1), range(1, 6)):
        _, coeff = power_filter(m, F(3, 2))
        actual = sum(a * F(sum(real_diagonal(basis, path) for path in product(terms, repeat=k)), 2**k)
                     for k, a in coeff.items())
        expected = F(3, 4)**(m//2) * (F((-1)**basis, 2) if m % 2 else 1)
        assert actual == expected
        checked += 1
    # Y tensor Y sends |01> to |10> with positive sign.
    assert real_diagonal(1, [signed_pauli("YY", 1), signed_pauli("XX", 1)]) == 1
    assert real_diagonal(0, [signed_pauli("YY", 1), signed_pauli("XX", 1)]) == -1
    return checked


def check_reduction():
    cases = 0
    for n, r in product((3, 4, 6, 9), (2, 5, 10)):
        size = n*r
        raw = installed_rules(n, r, True)
        word = ("LA" * size)[:size]
        mu = F(1, 16)  # terminal projector
        energy = F(0)
        rank_by_bond = [0] * (size - 1)
        transport_bonds = []
        for i, orig, dest in raw:
            rank = 2**sum(tag in "RLGF" for tag in orig)
            mu += F(rank, 16**len(orig))
            if len(orig) == 2:
                rank_by_bond[i] += rank
            if (orig, dest) == ("LA", "AR"):
                transport_bonds.append(i)
            if word[i:i+len(orig)] in (orig, dest):
                assert orig != "SR"
                energy += F(1, 2)
        assert transport_bonds == list(range(size - 1))
        assert rank_by_bond[0] == 14  # the rank-two marked gate replaces a rank-four gate
        for i in range(1, size - 1):
            assert rank_by_bond[i] == (12 if (i + 1) % n == 0 else 16)
        assert energy >= F(size//2, 2)
        assert mu <= F(7*(size-1),64) + F(3,16)
        assert energy - 2*mu >= F(size-13,32)
        if size >= 26:
            j = len(raw)+1
            K = 1 << (256*j - 1).bit_length()
            steps = n*(2*n+3)*(r-1)+n-1
            s = F(1,4*K)
            m = 36*steps**2/s
            assert m.denominator == 1
            tau = F(1, 1 << (256*m.numerator - 1).bit_length())
            assert s*(energy-2*mu) - 2*tau >= s*size/128
        cases += 1
    return cases


def main():
    filters, truncated = check_filters()
    paths = check_paths()
    chains = check_reduction()
    data = {"basis": "1", "power_unary": "11",
            "terms": [["X", "0.11"], ["X", "-0.001"], ["Z", "0.101"]]}
    assert read_instance(data)[2] == {"X": F(5, 8), "Z": F(5, 8)}
    result = estimate(data, Random(317).getrandbits)
    target = F(25, 32)
    assert abs(result - target) <= F(1, 32)
    # Deterministic answer for every possible fair draw, including the CLI.
    exact_data = {"basis": "10", "power_unary": "111", "terms": [["ZI", "1"]]}
    run = subprocess.run([sys.executable, "-B", str(Path(__file__).with_name("estimate_pauli_power.py"))],
                         input=json.dumps(exact_data), text=True, capture_output=True, check=True)
    assert json.loads(run.stdout) == {"numerator": -1, "denominator": 1}
    assert estimate({"basis": "0", "power_unary": "1", "terms": []}) == 0
    # Repeatedly return the largest random word so rejection exhausts its cap.
    abort = {"basis": "0", "power_unary": "1", "terms": [["I","0.1"],["Z","0.01"]]}
    assert estimate(abort, lambda k: (1 << k)-1) == 0
    print(json.dumps(dict(filter_cases=filters, strictly_truncated=truncated, exhaustive_moments=paths,
                          rewrite_installations=chains, seeded_estimate=str(result), true_diagonal=str(target),
                          cli_result=-1, retry_exhaustion_return=0), indent=2))


if __name__ == "__main__":
    main()
