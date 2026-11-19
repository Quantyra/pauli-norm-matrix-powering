# A fixed Pauli-norm threshold for diagonal matrix powering

Daniel Fredriksen · Quantyra Inc. · [ORCID](https://orcid.org/0009-0002-9123-7435)

For every fixed Pauli coefficient-norm cap $c>1$, distinguishing whether a single unnormalized diagonal entry of a polynomial matrix power is at least $9/32$ or at most $7/32$ is PromiseBQP-complete. An estimate accurate to $1/32$ decides the reduced instances. The reduction produces explicitly listed, positive definite Hermitian contractions with dyadic Pauli coefficients. At cap one an efficient classical sampler is known.

[Manuscript (PDF)](manuscript.pdf) · [LaTeX source](manuscript.tex) · [Review and dispositions](review/v1.1.0/disposition.md) · [Lean certification plan](lean-certification-plan.md)

[Cite the fixed-error preprint (v1.1.0)](https://doi.org/10.5281/zenodo.24373235) · [All versions on Zenodo](https://doi.org/10.5281/zenodo.24362437) · [Earlier inverse-polynomial result (v1.0.0)](https://doi.org/10.5281/zenodo.24362438)

## Reproduce the manuscript and numerical examples

The PDF was built with Tectonic 0.17.0. From this directory, run `tectonic manuscript.tex` with the environment variable `SOURCE_DATE_EPOCH` set to `1794960000` for the recorded build timestamp. A fresh environment may download the standard TeX bundle.

Run `python verify.py` with Python 3.10 or later. The script checks five small circuits at each of two caps, $3/2$ and $1+2^{-10}$. It compares the clock-averaged projector with $p/2$, checks the signed Pauli permutation against direct Hadamard conjugation, and powers the rounded matrix to check the resulting diagonal. These are floating-point reproducibility checks. The uniform bounds are proved in the manuscript. The [v1.0.0 verifier](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/v1.0.0/verify.py) reproduces that version’s twelve examples.

## Sources and license

The reduction builds on the [Janzing–Wocjan cyclic clock](https://doi.org/10.4086/toc.2007.v003a004) and answers the constant-Pauli-norm question in [Cifuentes et al.](https://doi.org/10.1103/g5x4-jcsz). Manuscript and supporting material are licensed under [CC BY 4.0](LICENSE).
