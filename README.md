# A fixed Pauli-norm threshold for diagonal matrix powering

Daniel Fredriksen · Quantyra Inc. · [ORCID](https://orcid.org/0009-0002-9123-7435)

Given an explicit sum of Pauli operators, how hard is it to estimate a single diagonal entry of a high matrix power? A known classical sampler runs in polynomial time when the coefficient weight is at most one. This paper proves that, for every fixed cap above one, the threshold decision problem is PromiseBQP-complete at inverse-polynomial precision. The construction works with a positive definite contraction and finite dyadic coefficients.

[Manuscript (PDF)](manuscript.pdf) · [LaTeX source](manuscript.tex) · [Review and dispositions](review/disposition.md) · [Lean certification plan](lean-certification-plan.md)

[Cite the reviewed preprint, v1.0.0](https://doi.org/10.5281/zenodo.24362438) · [All versions on Zenodo](https://doi.org/10.5281/zenodo.24362437)

## Reproduce the manuscript and numerical examples

The PDF was built with Tectonic 0.17.0. From this directory, run `tectonic manuscript.tex` with the environment variable `SOURCE_DATE_EPOCH` set to `1794960000` for the recorded build timestamp. A fresh environment may download the standard TeX bundle.

Run `python verify.py` with Python 3.10 or later. The script checks six small circuit examples at each of two fixed Pauli-norm caps, $3/2$ and $1+2^{-10}$. It uses the Python standard library and reports the clock period, power, coefficient mass and recovered probability. These are floating-point checks of the formulas. The manuscript gives the proof for arbitrary circuits.

## Sources and license

The reduction builds on the [Janzing–Wocjan cyclic clock](https://doi.org/10.4086/toc.2007.v003a004) and answers the constant-Pauli-norm question in [Cifuentes et al.](https://doi.org/10.1103/g5x4-jcsz). Manuscript and supporting material are licensed under [CC BY 4.0](LICENSE).
