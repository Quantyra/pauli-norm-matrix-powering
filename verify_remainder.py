"""Exact finite checks for the endpoint estimator and the Appendix D family."""

from fractions import Fraction
from itertools import product


def enumerate_scores(degree):
    """Average over all proposed paths starting in (|00> + i|11>)/sqrt(2)."""
    phases = {0: 0, 3: 1}
    real_part = (1, 0, -1, 0)
    average = Fraction()
    for start, start_phase in phases.items():
        for word in product(("D", "-XI", "YX"), repeat=degree):
            x, phase, score = start, 0, Fraction(1)
            probability = Fraction(1, 2)
            for step in word:
                if step == "D":
                    score *= Fraction((4, 2, 0, -2)[x], 8)
                    probability *= Fraction(8, 10)
                elif step == "-XI":
                    phase += 2
                    x ^= 2
                    probability *= Fraction(1, 10)
                else:
                    phase += 1 if x < 2 else -1
                    x ^= 3
                    probability *= Fraction(1, 10)
            if x in phases:
                exponent = phase + start_phase - phases[x]
                average += probability * score * real_part[exponent % 4]
    return Fraction(10, 8) ** degree * average


def check_moments():
    # Real and imaginary matrices of 8A. Multiply their integer blocks
    # independently of the path enumerator, deferring normalization.
    real = ((4, 0, -1, 0), (0, 2, 0, -1),
            (-1, 0, 0, 0), (0, -1, 0, -2))
    imag = ((0, 0, 0, -1), (0, 0, -1, 0),
            (0, 1, 0, 0), (1, 0, 0, 0))
    re, im = [1, 0, 0, 0], [0, 0, 0, 1]
    for degree in range(6):
        moment = Fraction(re[0] + im[3], 2 * 8 ** degree)
        assert enumerate_scores(degree) == moment, degree
        re, im = (
            [sum(a * r - b * s for a, b, r, s in zip(row, col, re, im))
             for row, col in zip(real, imag)],
            [sum(b * r + a * s for a, b, r, s in zip(row, col, re, im))
             for row, col in zip(real, imag)],
        )


def check_family():
    ell = 12
    n = 2 ** ell
    m = n ** 2
    eta = Fraction(ell ** 2, m)
    alpha = Fraction(1, 2)
    weights = [Fraction(n + 2 * i - 1, 2 * n ** 2) for i in range(1, n + 1)]
    assert sum(weights) == 1
    deletion = 3 * alpha * eta / 4
    assert (1 - eta) * alpha * min(weights) / 4 > 2 * deletion
    assert m * deletion == Fraction(3 * ell ** 2, 8)
    # (1-a)^m <= 1/(1+ma) by Bernoulli applied to (1-a)^(-m).
    loss = alpha * eta / 4
    assert Fraction(1, 2) - 1 / (1 + m * loss) > Fraction(1, 32)
    row_change = 9 * eta / 4
    assert 1 + alpha / 2 - row_change >= Fraction(9, 8)
    assert 1 + alpha - alpha ** 2 - Fraction(5, 2) * row_change >= Fraction(9, 8)


if __name__ == "__main__":
    check_moments()
    check_family()
    print("Exact endpoint means agree for degrees 0 through 5. "
          "Cover, deletion gap and row bounds checked at 4096 data bits.")
