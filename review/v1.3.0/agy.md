# Google Antigravity review of v1.3.0

Automated manuscript review. [Editorial disposition](disposition.md)

## Initial revision

[Reviewed source](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/71399c1702bca8920be642bac58dc2c49711c726/manuscript.tex), SHA-256 `c8d0b936d6d66428fa6eee1f3717cae6abba0978b5cc486610ddaf52a442f976`.

### Referee Report

**Recommendation:** **READY**

#### Confirmation of Source and New Results
The candidate manuscript (`manuscript.tex`, SHA-256 `c8d0b936...`) was read in full from `\documentclass` through `\end{document}`. Both newly added numbered results were verified:
1. **Theorem 3** (near-one sampling and lower bound): establishes a classical estimator with bit time $\mathrm{poly}(L)\exp(O(\sqrt{1+A}))$ and proves the matching filter coefficient lower bound $W_\lambda(f) \ge 2^{\sqrt{A}/3 - 8}$ for $A = m\ln\lambda \ge 2$.
2. **Corollary 4** (spin-chain coefficient mass): establishes that for the rounded chain, $m\ln\lambda(B) = \Theta(NT^2)$, requiring a prescribed trial count of $\exp(\Theta(T\sqrt{N}))$.

---

#### Technical Checks

- **Ranks and Identity Mass:** The 2-site rewrite projectors act on 256 levels with rank $\le 4$ (normalized trace $\le 1/64$), while the boundary and terminal pin rules have rank 1 on 16 levels (trace $1/16$). The bound $\mu \le 7(N-1)/64 + 3/16$ is exact, yielding $\lambda(B_*) = 1 + s(\lambda(H) - 2\mu) \ge 1 + s(N-13)/32 \ge 1 + sN/64$ for $N \ge 26$.
- **Alternating Word & Transport Flag:** Evaluating the state $|L_0, F_{\rm left}, L_0, F_{\rm left}, \dots\rangle$ over $\lfloor N/2 \rfloor$ disjoint bonds isolates the transport rule $L_b F_{\rm left} \leftrightarrow F_{\rm left} R_b$, contributing diagonal energy $1/2$ each. By positive semidefiniteness of all other terms, $\|H\| \ge \lfloor N/2 \rfloor / 2$ holds unconditionally on the full space.
- **Rounding Loss:** Inward scaling and $\eta$-grid truncation lose at most $2\tau \le sN/128$ in Pauli mass (since $ms = 36T^2$), guaranteeing the net lower bound $\lambda(B) \ge 1 + sN/128$.
- **Prior Attribution & Scope:** Citations to Sachdeva–Vishnoi for the Chebyshev expectation identity, Wang–McArdle–Berta and Cifuentes et al. for Pauli sampling, and Montanaro–Shao are accurate. Theorem 3 appropriately bounds uniform scalar Chebyshev filters rather than claiming an algorithmic lower bound.
- **Clinical Reading of Corollary 4:** The trial count $\exp(\Theta(T\sqrt{N}))$ is correctly contextualized as an attribute of the generic Chebyshev filter. The author explicitly contrasts this with direct classical path enumeration on the unclocked circuit ($16^N \mathrm{poly}(L_{\rm src})$), highlighting the distinction between coefficient normalization and physical variance.
- **Editorial Integration:** Notation, equation references, and shared-counter numbering (Theorems 1, 3; Corollaries 2, 4) integrate seamlessly.

---

#### Mandatory Corrections
- **None.** The derivations and bounds are mathematically complete and sound.

#### Optional Polish
1. *Roadmap:* Section 1 could briefly mention Theorem 3 and Corollary 4 alongside Theorem 1 and Corollary 2 to preview the near-one sampling results.
2. *Lower Bound Constant:* In the proof of Corollary 4, $m(\lambda-1)/\lambda \ge \frac{9}{40}NT^2$; the text uses the slightly looser but valid constant $\frac{3}{16}NT^2$. A brief note stating $\frac{9}{40} > \frac{3}{16}$ could prevent reader second-guessing.

## Release candidate

[Reviewed source](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/8708b50322448cb437c4764fa2c2260baffdbedc/manuscript.tex), SHA-256 `06fa0bb5acd7fcf55c99a9442009147e3e00bde2888a92a309cdaf90fab7b05e`.

### Referee Report

**Recommendation:** **READY**

#### Confirmation of Source and New Results
The complete manuscript (`manuscript.tex`, SHA-256 `06fa0bb5...`) was read in full from `\documentclass` through `\end{document}`. Both newly added numbered results were independently verified:
1. **Theorem 3** (near-one sampling and lower bound): Establishes a classical estimator with bit time $\mathrm{poly}(L)\exp(O(\sqrt{1+A}))$ achieving error $\le 13/512 < 1/32$ for $A = m\ln\lambda$, and proves the matching scalar filter lower bound $W_\lambda(f) \ge 2^{\sqrt{A}/3 - 8}$ for $A \ge 2$.
2. **Corollary 4** (spin-chain coefficient mass): Establishes that the rounded chain satisfies $\tfrac{3}{16}NT^2 \le m\ln\lambda(B) \le 36KT^2$ (hence $\Theta(NT^2)$), requiring a prescribed Chebyshev trial count of $\exp(\Theta(T\sqrt{N}))$.

---

#### Technical Checks

- **Ranks and Identity Mass:** The 2-site projectors act on 256 levels with rank $\le 4$ (normalized trace $\le 1/64$), and the three 1-site terms have rank 1 on 16 levels (trace $1/16$). The bound $\mu \le 7(N-1)/64 + 3/16$ is exact, giving $\lambda(B_*) = 1 + s(\lambda(H) - 2\mu) \ge 1 + s(N-13)/32 \ge 1 + sN/64$ for $N \ge 26$.
- **Alternating Word & Transport Flag:** Evaluating $|L_0, A, L_0, A, \dots\rangle$ over $\lfloor N/2 \rfloor$ disjoint bonds isolates rule 3 ($LA \leftrightarrow AR$) with diagonal energy $1/2$ each. By positive semidefiniteness of all other projectors, $\|H\| \ge \lfloor N/2 \rfloor / 2$ holds unconditionally on the full space.
- **Rounding Loss:** Inward scaling and $\eta$-grid truncation lose $\le 2\tau \le sN/128$ in Pauli mass (using $ms = 36T^2$), ensuring the net lower bound $\lambda(B) \ge 1 + sN/128$.
- **Prior Attribution & Scope of Optimality:** Citations to Sachdeva–Vishnoi for the Chebyshev expectation identity, Wang–McArdle–Berta and Cifuentes et al. for Pauli sampling, and Montanaro–Shao are accurate. Theorem 3 appropriately bounds uniform scalar Chebyshev filters rather than claiming an algorithmic lower bound.
- **Clinical Reading of Corollary 4:** The trial count $\exp(\Theta(T\sqrt{N}))$ is correctly isolated as a property of the generic Chebyshev filter. The author explicitly contrasts this with direct path enumeration on the unclocked circuit ($16^N \mathrm{poly}(L_{\rm src})$ with $N \le T+1$), correctly highlighting the distinction between coefficient normalization and physical variance.
- **Editorial Integration:** Notation, references, and shared-counter numbering (Theorems 1, 3; Corollaries 2, 4) integrate seamlessly.

---

#### Mandatory Corrections
- **None.** The derivations and proofs are mathematically sound and complete.

#### Optional Polish
1. *Roadmap:* Section 1 could briefly mention Theorem 3 and Corollary 4 to preview the near-one sampling and spin-chain mass results alongside Theorem 1 and Corollary 2.
2. *Lower Bound Constant:* In the proof of Corollary 4, $m(\lambda-1)/\lambda \ge \frac{9}{40}NT^2$; the text uses the slightly looser but valid constant $\frac{3}{16}NT^2$. A passing remark noting $\frac{9}{40} > \frac{3}{16}$ could assist the reader.
