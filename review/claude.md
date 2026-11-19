# Claude manuscript review

Complexity and input encoding. These are AI-generated reports. [Disposition and mathematical responses](disposition.md)

## Initial manuscript

[Reviewed source](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/430cb5841793a04a2d2add757e61d011f4475681/manuscript.tex), SHA-256 `8a6021f3adfabd84ffb318ef2c5f7e508ce452adea9d911a4d443e5e28ec724c`.

**Reconstructed claims.** (i) λ(B)≤1 ⇒ BPP via Pauli-path sampling (unbiased: dummy mass 1−λ, score Re⟨j|P₁⋯P_m|j⟩·∏sgn b_P, range [−1,1]). (ii) Membership: phase estimation of e^{iB}, phases in [−1,1] single-valued, x↦x^m is m-Lipschitz, error budget ε/8+2ε/32+ε/16. (iii) Hardness: W=Σ|a+1⟩⟨a|⊗V_a with ordered product R=C†(2Π−I)C, A=(W+W†)/2; rings give mass exactly p/M at +1, rest ≤cos(π/M)≤1−2/M²; B\*=(1−s)I+sA with s=d/K, K=2M, d≤min(½,c−1) gives λ(B\*)≤1+d≤c, positive definite, m=(M³/d)⌈log₂64M⌉ (integer, M and 1/d powers of two) suppressing the complement to 1/(64M); dyadic rounding with τ≤1/(128mM) keeps ‖B^m−B\*^m‖≤3/(256M).

I checked each step numerically; the chain g=1/(2M), ε=1/(16M), scaled diagonal >7/12 / <5/12 (including the 1/48 compilation slack) holds with margin. λ(A)≤2M, the coefficient field ℤ[1/2]+√2ℤ[1/2] for the Hermitian part (T contributes ½±√2/4), and sin(π/2M)≥1/M all verify. The Pauli-weight question is correctly separated from the induced 1-norm.

**Issues.**

1. **Moderate — bit model.** "Both m and 1/ε polynomially bounded … with a fixed polynomial bound or unary resource limits" is a disjunction, not a definition. Completeness is only meaningful once one convention is fixed (I recommend: m and ⌈1/ε⌉ in unary). With m in binary and unbounded, membership fails. Pin this down in the problem statement; the reduction already emits m=Θ(t³log t) and 1/ε=16M, both fine in unary.
2. **Moderate — PE on a superposition.** "Conditional on an eigenstate … on |j⟩ it samples the spectral mixture" needs one line: cross terms vanish because eigenvector registers stay orthogonal, and median amplification within a trial is legitimate because the first measurement collapses to a near-eigenstate. As written a referee will read it as an unjustified exchange of linearity and median-taking.
3. **Minor — missing hypothesis.** M even (forced by the power-of-two choice) is what keeps the odd modes cos((2k+1)π/M) away from +1. State it where the mass p/M is claimed.
4. **Minor — Trotter accounting.** Give the commutator-bound constant and its source, and note λ(B)≤S (each |b_P|≤‖B‖), so membership holds for *every* cap, not just fixed c. Currently λ is silently treated as O(1).
5. **Minor — framing.** A "threshold" between cap 1 and cap >1 is a genuine complexity separation only if BPP≠BQP; say so.

**Optional.** The construction survives d=1/poly, so hardness actually holds for caps 1+1/poly(n) — strengthening the abstract's "fixed cap" and narrowing the unclassified regime to 1+o(1/poly). Also: cite [cif] by section for the sampling bound and the question; remark that non-dyadic rational inputs only cost approximate sampling.

No mathematical error found; the defects are definitional and expository.

**Verdict: REVISE.**

## Revised manuscript

[Reviewed source](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/988f17351b893e803dce674df7e304ec8f345fb4/manuscript.tex), SHA-256 `40fa75257749535764f800cc894bc1a05284393a94d758fcf8eea0aca351742c`.

**Referee report (round 2)**

All five prior defects are addressed.

1. **Bit model — resolved.** $m,r$ are now unary with $\epsilon=1/r$, and $L$ is defined. The emitted $m=M^3\lceil\log_2 64M\rceil/d$ and $r=16M$ are polynomial for fixed $d$, so the reduction respects the convention it assumes.
2. **Phase estimation on $\ket j$ — resolved.** Fresh ancilla registers, conditional independence given an eigenvector, and tracing out orthogonal eigencomponents are now stated; the within-trial median is thereby legitimate. Degeneracy is harmless (PE acts identically on an eigenspace).
3. **Odd rings — resolved**, and better than requested: parity of $2k+1$ versus $2M$ excludes phase zero for any $M$, so evenness is not needed; $\cos(\pi/M)\le1-2/M^2$ follows from $\sin(\pi/2M)\ge1/M$.
4. **Trotter — resolved.** The commutator bound is sourced to [trotter], and $\sum_{a<b}2|b_a||b_b|\le\lambda(B)^2$ is correct.
5. **Framing — resolved** by the explicit $\BPP=\BQP$ consequence.

Re-verified independently: $\lambda(A)\le 2M$ with $O(M^2)$ slots; $\lambda(B_*)\le1-s+d\le c$; spectrum in $[1-2s,\,1-2s/M^2]\cup\{1\}$; tail $\le e^{-\lceil\log_2 64M\rceil}\le1/(64M)$; $\tfrac32 m\tau\le3/(256M)$; positive definiteness; and the gap $M\bra jB^m\ket j\ge0.63$ versus $\le0.39$ against $g\pm\epsilon=(0.5\pm0.0625)/M$, with the $1/48$ slack. Sampler unbiasedness and the $[-1,1]$ range hold; the $m\log\lambda=O(\log L)$ caveat is correctly fenced off.

Non-blocking polish: note $|b_P|\le\norm B$, hence $\lambda(B)\le S\le L$, so membership extends beyond fixed caps; cite a source for the $1/48$ gate-set compilation.

No mathematical error remains; the fixed-cap claim verifies.

**Verdict: READY.**
