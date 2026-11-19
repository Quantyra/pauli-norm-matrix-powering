# Google Antigravity manuscript review

Attribution, significance and presentation. These are AI-generated reports. [Disposition and mathematical responses](disposition.md)

## Initial manuscript

[Reviewed source](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/430cb5841793a04a2d2add757e61d011f4475681/manuscript.tex), SHA-256 `8a6021f3adfabd84ffb318ef2c5f7e508ce452adea9d911a4d443e5e28ec724c`.

### Reconstruction of Key Claims
The manuscript establishes a sharp complexity phase transition for estimating a diagonal entry $\bra{j}B^m\ket{j}$ of a powered Hermitian contraction $B = \sum_P b_P P$ ($\norm{B}\le 1$) to inverse-polynomial additive precision:
1. For Pauli 1-norm cap $\lambda(B) = \sum_P |b_P| \le 1$, the problem is in $\BPP$ via classical Pauli-path Monte Carlo sampling.
2. For any fixed constant cap $c > 1$, the problem is $\mathsf{PromiseBQP}$-complete under deterministic classical polynomial-time many-one reductions, even restricted to strictly positive definite instances with dyadic rational coefficients.

The reduction couples an affine contraction $B_* = (1-s)I + sA$ ($s = d/(2M)$) with a Janzing–Wocjan cyclic clock Hamiltonian $A$. This preserves an isolated eigenvalue $+1$ with spectral weight $p/M$ (encoding circuit acceptance $p$), while mapping all other eigenvalues into $[0, 1 - 2s/M^2]$. A polynomial power $m = \widetilde{O}(M^3/d)$ damps non-distinguished modes to $\le 1/(64M)$.

---

### Audit
- **Attribution & Explicit Question**: Directly and affirmatively resolves the open question posed by Cifuentes et al. (*PRX Quantum*, Discussion p. 11) regarding whether Pauli-access monomial BQP-hardness holds at constant Pauli weight. The manuscript correctly distinguishes the Pauli 1-norm $\lambda(B)$ from the induced matrix 1-norm (column sums in the computational basis). Janzing–Wocjan (2007) is properly credited.
- **Significance & Novelty**: High. It proves that any constant norm slack $c > 1$ above the classical simulation threshold $c = 1$ is sufficient for quantum computational universality.
- **Scientific Assertions & Finite Precision**: Rigorous and correct. Eigenvalues of the cyclic clock, the spectral gap $1-\cos(\pi/M) \ge 2/M^2$, and positive definiteness $(1-2s)I \le B_*$ are mathematically verified. The finite-precision treatment via directed dyadic rounding toward zero with grid spacing $\tau/(2S)$ preserves $\norm{B}\le 1$, $\lambda(B)\le c$, and controls telescoping power error to $\le 3/(256M)$.
- **Terminology & Presentation**: Clear, compact, and technically precise.
- **Journal Suitability**: Highly suitable for publication in leading quantum information and theoretical computer science journals (*PRX Quantum*, *Quantum*, *IEEE TIT*).

---

### Actionable Issues

1. **Explicit Bound on Coefficient Slots (Minor)**:
   *Rationale*: Section 4 introduces $S$ as the number of coefficient slots without an upfront bound.
   *Action*: State explicitly that $S \le O(M^2)$ before the truncation step to clarify the bit-length bound $O(\log(SmM))$.
2. **Sub-constant Scaling (Optional)**:
   *Rationale*: Stating whether the reduction extends to $c(n) = 1 + 1/\mathrm{poly}(n)$ would contextualize the boundary.
3. **Ancilla Registers (Optional)**:
   *Rationale*: Explicitly noting that initial ancillae are fixed within $\ket{z}$ improves completeness.

---

**Verdict: READY**

## Revised manuscript

[Reviewed source](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/988f17351b893e803dce674df7e304ec8f345fb4/manuscript.tex), SHA-256 `40fa75257749535764f800cc894bc1a05284393a94d758fcf8eea0aca351742c`.

### Review & Audit

**Attribution & Explicit Question:** The manuscript affirmatively resolves the open question posed by Cifuentes et al. (*PRX Quantum*, Discussion p. 11), strictly isolating the Pauli 1-norm $\lambda(B) = \sum_P |b_P|$ from the induced matrix 1-norm. Foundational citations (Janzing–Wocjan, Wang–McArdle–Berta, Childs et al.) are accurate and complete.

**Significance, Novelty Scope & Presentation:** Novelty and scope are sharp: establishing $\mathsf{PromiseBQP}$-completeness for any fixed cap $c > 1$ under unary $m, r$ delineates the boundary against the $c \le 1$ classical sampling regime. Terminology and presentation are rigorous, compact, and lucid.

**Scientific Assertions & Finite Precision:** All mathematical claims are verified. The cyclic-clock construction, preservation of eigenvalue $+1$ with spectral weight $p/M$, suppression of non-distinguished modes via $m = O(M^3 \log M / d)$, and spectral mixture/median amplification in phase estimation are sound. Directed dyadic rounding toward zero with grid spacing $\tau/(2S)$ rigorously bounds telescoping error ($\le 3/(256M)$), ensures positive definiteness, and preserves $\|B\| \le 1$ and $\lambda(B) \le c$.

**Journal Suitability:** Highly suitable for top-tier venues (*PRX Quantum*, *Quantum*, *IEEE TIT*).

**Resolution of Concerns & Blockers:** All prior concerns are resolved. The revision bounds coefficient slots $S = O(M^2)$, specifies zero ancillas, explicitly defines unary $m, r$, accounts for fixed $d$, and distinguishes fixed caps from the $m \log \lambda(B) = O(\log L)$ regime. No scientific blockers remain.

**Verdict: READY**
