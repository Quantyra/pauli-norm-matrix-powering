# Three-lens review and disposition for v1.0.0

This record accompanies the [inverse-polynomial-precision release](https://github.com/Quantyra/pauli-norm-matrix-powering/tree/v1.0.0). The [fixed-error revision](v1.1.0/disposition.md) has its own source and reviewer reports.

**Grok, Claude and AGY each marked the revised manuscript ready for preprint release.** The reviewers received the full LaTeX source in isolated, single-turn sessions. The initial source was [430cb58](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/430cb5841793a04a2d2add757e61d011f4475681/manuscript.tex). Each reviewer also received the [revised source](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/988f17351b893e803dce674df7e304ec8f345fb4/manuscript.tex) and its own first report. The two source digests are recorded with the reports. All reviews used installed vendor CLIs. The prompts supplied the published question and requested mathematical scrutiny of the manuscript. Literature priority and journal peer review require separate evidence.

| Review | Main issue | Initial verdict | Revised verdict |
| --- | --- | --- | --- |
| [Grok](grok.md) | Full-space clock, spectral mass, small caps and finite-bit decision gap | Ready | Ready |
| [Claude](claude.md) | Uniformity, bit model, classical sampling and quantum membership | Revise | Ready |
| [Google Antigravity](agy.md) | Attribution, scope, resource accounting and journal fit | Ready, minor edits | Ready |

## Mathematical dispositions

**Decision problem.** The source now defines positive integers \(m,r\) in unary and sets the tolerance to \(1/r\). The hardness map writes \(r=16M\) and a polynomial number of symbols for \(m\) at every fixed cap. This removes the ambiguity Claude identified. The passing thresholds follow by direct substitution. With compilation slack the worst scaled YES and NO bounds are \(487/768\) and \(293/768\), respectively. The model reports provide no independent numerical experiment beyond the public verifier.

**Membership.** Section 2 states why phase estimation on a superposition samples its spectral mixture: the system eigenvectors remain orthogonal when the phase registers are traced out. Median amplification within one trial can use fresh phase registers conditional on the same eigenvector. The manuscript now gives the first-order product-formula commutator bound, cites its source, and charges aggregate simulation and synthesis error across a trial. The theorem fixes \(c\); the referee's optional extension of the membership estimate to unrestricted explicitly listed coefficients is unnecessary for this proof.

**Spectral and Pauli conventions.** Section 3 specifies the zero ancillas and writes the odd-phase exclusion directly. It follows from the closing sign; evenness of \(M\) is unnecessary for that exclusion. Section 4 now states \(S=O(M^2)\) for the collected slots including identity. The choice \(d\le1/2\) keeps \(s=d/(2M)\) uniformly small for every cap, including large ones. The full ring carries the sign of the reflection.

**Fixed caps and priority.** Some reviewers suggested extending the result to size-dependent caps. The public theorem concerns fixed \(c\). The text now gives the classical sampling regime \(m\log\lambda(B)=O(\log L)\); inferring hardness for \(1+1/\mathrm{poly}(L)\) without specifying the resource encoding would be unwarranted. Grok's final shorthand about shrinking caps is too strong: fixed weight and logarithmic power can also satisfy the displayed sampling bound. The manuscript states the quantitative condition. The easy side now cites Wang, McArdle and Berta directly. The cyclic clock and its Pauli input come from Janzing–Wocjan and Cifuentes et al. The conditional implication for BPP versus BQP appears after Theorem 1. Reviewer opinions on priority or journal prestige do not establish either.

## Verification and scope

The four-page PDF was rebuilt from a fresh public checkout using Tectonic 0.17.0 and a fixed timestamp. Its bytes matched the committed PDF, SHA-256 `bde8805e28e6a37a17bdd7469b56de077bd3f84900800afb2e192e034e6271c2`. Text extraction and raster comparison matched on all four pages. Twelve small numerical examples (six circuits at two caps) passed the separate [replay](../verify.py). The [Lean certification plan](../lean-certification-plan.md) maps the full proof to staged obligations. No Lean theorem is claimed.
