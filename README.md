# A fixed Pauli-norm threshold for diagonal matrix powering

Daniel Fredriksen · Quantyra Inc. · [ORCID](https://orcid.org/0009-0002-9123-7435)

For every fixed Pauli coefficient-norm cap $c>1$, distinguishing whether a single unnormalized diagonal entry of a polynomial matrix power is at least $9/32$ or at most $7/32$ is PromiseBQP-complete. An estimate accurate to $1/32$ decides the reduced instances. The reduction produces explicitly listed, positive definite Hermitian contractions with dyadic Pauli coefficients. At cap one an efficient classical sampler is known. Corollary 2 proves the same fixed-error hardness on an open chain of 16-dimensional sites with position-dependent interactions. Each site encodes four qubits and every listed Pauli string acts on at most two consecutive sites.

For a Hermitian contraction with actual Pauli weight $1<\lambda\le3/2$, Theorem 3 gives polynomial-time classical estimation to additive error $1/32$ whenever $m\ln\lambda=O(\log^2 L)$ in the written input length $L$. The upper and lower exponents match for the weighted coefficient mass of uniformly accurate scalar filters. On the rounded spin chains, Corollary 4 shows that the prescribed number of trials grows as $\exp(\Theta(T\sqrt N))$ for chain length $N$ and clock length $T$. Appendix B proves large actual variance for the signed Pauli trial. Theorem 5 gives a three-wire example where a walk that sums two steps before sampling has single-trial variance at least $\exp(\Omega(T^2))$ at the marked input, after rounding. The source circuit is easy to simulate. On a different YES/NO pair with $q$ work bits, Theorem 6 bounds the total variation distance between the two single-score laws by $2^{-q}$. Any decoder receiving only independent scores from the specified two-step row sampler needs at least $2^q/3$ trials for success $2/3$ on both inputs. The proof uses one explicit permitted rounding and includes nonreturns and rejection-cap aborts. The bound is exponential in the number of work bits and superpolynomial in the written input length.

[Manuscript (PDF)](manuscript.pdf) · [LaTeX source](manuscript.tex) · [Review and dispositions](review/v1.5.0/disposition.md) · [Lean certification plan](lean-certification-plan.md)

[Cite the fixed-confidence revision (v1.5.0)](https://doi.org/10.5281/zenodo.24379198) · [Cite the variance revision (v1.4.0)](https://doi.org/10.5281/zenodo.24378072) · [Cite the sampling revision (v1.3.0)](https://doi.org/10.5281/zenodo.24376878) · [Spin-chain reduction (v1.2.0)](https://doi.org/10.5281/zenodo.24375191) · [All versions on Zenodo](https://doi.org/10.5281/zenodo.24362437) · [Fixed-error theorem (v1.1.0)](https://doi.org/10.5281/zenodo.24373235) · [Inverse-polynomial result (v1.0.0)](https://doi.org/10.5281/zenodo.24362438)

## Reproduce the manuscript and numerical examples

The PDF was built with Tectonic 0.17.0. From this directory, run `tectonic manuscript.tex` with the environment variable `SOURCE_DATE_EPOCH` set to `1794960000` for the recorded build timestamp. A fresh environment may download the standard TeX bundle.

Run `python verify.py` with Python 3.10 or later. The script checks five small circuits at each of two caps, $3/2$ and $1+2^{-10}$. It compares the clock-averaged projector with $p/2$, checks the signed Pauli permutation against direct Hadamard conjugation, and powers the rounded matrix to check the resulting diagonal. These are floating-point reproducibility checks. The uniform bounds are proved in the manuscript. The [v1.0.0 verifier](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/v1.0.0/verify.py) reproduces that version’s twelve examples.

Run `python verify_chain.py` to reproduce the finite checks for Appendix A. It enumerates the forward and reverse moves on the original and modified clock paths for twelve choices of width and sweep count, checks both weighted quadratic forms by exact rational elimination for path lengths 1 through 12, and verifies the two decision margins.

Run `python verify_sampling.py` to check filter construction, exact Pauli-product means and rank counts for the chain. The reference estimator `estimate_pauli_power.py` reads one JSON instance on standard input. For example, save the following as `instance.json` and run `Get-Content -Raw instance.json | python estimate_pauli_power.py` in PowerShell, or `python estimate_pauli_power.py < instance.json` in a POSIX shell.

```json
{"basis":"0","power_unary":"11","terms":[["X","0.101"],["Z","0.101"]]}
```

Coefficients are signed binary fixed-point strings, so both coefficients above equal $5/8$. The exact diagonal is $25/32$. The program returns an estimated rational numerator and denominator. Its confidence guarantee assumes a Hermitian contraction and independent fair random bits.

Run `python verify_return.py` to check the two-step row constructor, a complete small walk, and the clock window used in Theorem 5. `two_step_walk.py` accepts the same JSON format and prints the exact squared-matrix row at the supplied basis word. Each entry gives its real and imaginary parts. The analytic proof covers the growing family and all allowed roundings.

Run `python verify_confidence.py` to reconstruct the collected and rounded Pauli coefficients of both 294-site inputs at two work bits. It checks the marked start, the complete two-step rows at isolated crossings, the change at the late gate, and the two-bit reset calculation. Theorem 6 gives the bound for every positive number of work bits.

## Sources and license

The reduction builds on the [Janzing–Wocjan cyclic clock](https://doi.org/10.4086/toc.2007.v003a004) and answers the constant-Pauli-norm question in [Cifuentes et al.](https://doi.org/10.1103/g5x4-jcsz). Manuscript and supporting material are licensed under [CC BY 4.0](LICENSE).
