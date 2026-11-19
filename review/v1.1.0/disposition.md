# Three-lens review of the fixed-error revision

All three vendor CLIs reviewed the same [release-candidate source](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/e6fcbe52c38c61717c87722895402173ec4fb1fe/manuscript.tex), SHA-256 `b7a2bde231a5a576eca8261de259ba04d46187b524dcd84698327d2237e72d18`. The [initial revision](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/26c85619d4f86329f6e5f1c5c5ff6854a3c30009/manuscript.tex) had SHA-256 `7dd154a8f6793cb2b95200cb69a9ff773a1b82902defda3c1043cbaf92d0cf6c`. These are automated manuscript reviews. Human referee review and literature priority remain open.

| Reviewer | Question | Initial revision | Release candidate |
| --- | --- | --- | --- |
| [Grok](grok.md) | Clock spectrum, basis change and error margins | No report before timeout | Ready |
| [Claude](claude.md) | Computational model, finite-bit reduction and all-input estimator | Revise | Ready |
| [Google Antigravity](agy.md) | Attribution, significance and exposition | Ready | Ready |

## Dispositions

**Reduction and thresholds.** Grok reconstructed both ring sectors, the exact idle-half overlap, and the error after directed rounding. The theorem gives hardness for estimating the unnormalized diagonal to additive error 1/32 on the reduction's images. On arbitrary inputs at exactly 9/32 and 7/32, an estimate at that tolerance could return 1/4 from either side. The all-input decision algorithm uses 1/64 accuracy. The finite-bit reduction has strict slack of 55/1536 and 49/1536 beyond the two decision thresholds.

**Encoding and algorithms.** Claude's two required corrections were implemented. The input charges the unary power; an alternative binary encoding includes a unary upper bound. The variable-precision formulation now specifies its rational threshold and its unary reciprocal tolerance. The revision also specifies fixed-point coefficient bits and common label length, a grid comparison algorithm over dyadic pairs, the signed phase interval, and the simulation contribution to the final bias. The theorem is per fixed cap. The optional claim about caps depending on input size is outside its scope. The classical implication uses the usual bounded-error success convention. Intermediate gate and clock-unit expansions use the absolute values of their complex Pauli coefficients. Padding extends the index by zero bits.

**Attribution.** The paper credits Janzing and Wocjan for the periodic clock, Cifuentes et al. for the Pauli-access construction and the capped-norm question, the guided-Hamiltonian papers for pre-idling, and the earlier version for inverse-polynomial accuracy. Cifuentes et al.'s constant-error local measurement uses a normalized state. Their Chebyshev entry result estimates a different polynomial. The manuscript now spells out the binary factorization of the clock transition and the spectral estimator's error budget. These comparisons support the stated distinctions. An absence of an earlier exact theorem in this search cannot certify priority. [Matrix functions](https://doi.org/10.1103/g5x4-jcsz) · [Guided Hamiltonians](https://doi.org/10.4230/LIPIcs.ICALP.2023.32)

**Verification.** The Python verifier reproduced all ten archived numerical examples, five circuits at each of two caps, in 25.39 seconds under a 60-second cap. The small cases check the projector, signed Clifford permutation and rounded diagonal; the proof covers arbitrary circuits. Tectonic 0.17.0 rebuilt the five-page PDF from the committed source with an identical SHA-256 of `5b9610d8b9b8316d57875a5db33268726124e4fe38e0a58ea80eae1666909aa5`. PDF text extraction and layout bounds were checked on all pages. The [Lean plan](../../lean-certification-plan.md) targets the strengthened theorem. Formal certification is prospective.
