# Google Antigravity review of v1.2.0

Automated manuscript review. [Editorial disposition](disposition.md)

## Initial revision

[Reviewed source](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/8c567f9bf3977b0ea050c5e6c4c6064b167c03f3/manuscript.tex), SHA-256 `7b8f605792ef5d25babaf28b5a355d1e55078cc295997b48f1f5f14015ec7e1a`.

### Recommendation: **READY**

### Mandatory Corrections
**None.** The mathematical construction is complete and correct, the error budgets close with strict constant margins, and the reduction is strictly polynomial-time.

---

### Concrete Reasoning & Technical Evaluation

1. **Attribution to Prior Work:**
   * **AGIK [8]:** Properly credited for the 1D clock transitions and deterministic routing (Fact 2.2). The addition of boundary symbol $S$ on bond $(1,2)$ cleanly isolates the transition history.
   * **Bausch–Crosson [9]:** Accurately credited for the weighted history-state construction (Lemma 4). Weighting $\pi_0 = 1/2$ and $\pi_{t \ge 1} = 1/(2T)$ is the crucial mechanism allowing half the spectral weight to concentrate at the product input $j$ without requiring global clock Hadamards.
   * **Janzing–Wocjan–Zhang [10]:** Appropriately cited in Appendix~\ref{sec:chain}. The text clearly differentiates their approach (resolved energy estimation on translation-invariant chains) from this work (unnormalized diagonal moment estimation on position-dependent chains).

2. **Claim for a Raw Monomial:**
   The manuscript unambiguously targets an unnormalized diagonal matrix element $\bra j B^m \ket j$ of a raw monomial power. It clearly differentiates this result from Cifuentes et al. [2], where constant-error estimation required either state-norm division (Appendix A) or Chebyshev polynomials rather than pure matrix powering.

3. **Site Dimension & Position Dependence:**
   The claim of 16-dimensional sites ($4$ qubits) is exact: the 12 AGIK states plus the start symbol $S$ require 13 levels, embedding into $\mathbb{C}^{16}$ with unused levels projected out. The interactions are explicitly and correctly identified as position-dependent, matching the non-uniform sweep schedule of AGIK.

4. **Completeness Proof & Error Budgeting:**
   * **Upper bound:** Contained in $\mathsf{PromiseBQP}$ via Trotterized phase estimation on $e^{iB}$ followed by classical scalar exponentiation.
   * **Spectral gap:** The weighted path inequality bounds the positive energy penalty by $1/(6T^2)$. The operator-norm difference $\|B^m - B_*^m\| \le 3/512$ under dyadic grid rounding is sound, yielding well-separated acceptance windows ($v_{\rm YES} > 9/32$, $v_{\rm NO} < 7/32$) resolvable within $1/32$ additive tolerance.

---

### Optional Polish
* In Appendix~\ref{sec:chain}, explicitly mention that Bausch–Crosson weighting is introduced precisely to avoid the clock Hadamards used in Section 3, which would otherwise destroy the 2-local 1D geometry.
* Note explicitly that the 3 unused computational levels per site are annihilated by the local projectors.

## Release candidate

[Reviewed source](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/e1434f83fe5e7725cce723f143eded0173114b08/manuscript.tex), SHA-256 `db5780cfc13942210ac37d2eea16cd3c5605400f23b0c2c7069814831347526d`.

### Recommendation: **READY**

### Mandatory Corrections
**None.** All mathematical proofs are sound, error bounds close with explicit constant margins, and the previous revision suggestions have been seamlessly incorporated.

---

### Concrete Reasoning & Technical Evaluation

1. **Attribution to Prior Literature:**
   * **AGIK [8]:** Properly credited for the 12-state clock transitions and deterministic routing (Fact 2.2). The inclusion of marker symbol $S$ on bond $(1,2)$ cleanly isolates the initial transition and makes the domain of the inverse rewrite explicit.
   * **Bausch–Crosson [9]:** Accurately cited (Lemma 4). The revision explicitly notes that the weighted history-state construction ($\pi_0 = 1/2$, $\pi_{t \ge 1} = 1/(2T)$) places constant spectral weight on the initial product state, successfully dispensing with the global clock Hadamards from Section 3 that would otherwise destroy the 2-local 1D geometry.
   * **Janzing–Wocjan–Zhang [10]:** Appropriately contrasted in Appendix~\ref{sec:chain}, distinguishing their resolved energy estimation on translation-invariant chains from this work’s unnormalized diagonal moment estimation on position-dependent chains.

2. **Claim for a Raw Monomial:**
   The paper unambiguously establishes hardness for an unnormalized diagonal entry $v = \bra j B^m \ket j$ of a raw monomial power. The contrast with Cifuentes et al.\ [2] is sharp: their constant-error results required dividing by the output state norm or employing Chebyshev matrix polynomials, whereas this construction achieves BQP-completeness with pure matrix powering.

3. **Site Dimension & Position Dependence:**
   The 1D corollary correctly specifies 16-dimensional sites ($4$ qubits each). The 13 physical symbols embed into $\mathbb{C}^{16}$, and the text now explicitly verifies that local projectors annihilate the 3 unused computational levels per site. Interactions are correctly identified as position-dependent, governed by the non-uniform AGIK sweep schedule and localized boundary terms ($h_\star$ and terminal rejection).

4. **Completeness & Spectral Gap Proof:**
   * **Upper bound:** Contained in $\mathsf{PromiseBQP}$ via Trotterized phase estimation on $e^{iB}$ followed by classical scalar exponentiation with bounded error propagation.
   * **Spectral analysis:** The weighted path inequality establishes the $1/(6T^2)$ positive energy lower bound. Dyadic inward rounding bounds operator-norm deviation by $\|B^m - B_*^m\| \le 3/512$. Combined with a $1/48$ compilation budget, the acceptance thresholds ($v_{\rm YES} > 9/32$, $v_{\rm NO} < 7/32$) are strictly separated and resolvable within $1/32$ additive tolerance.

---

### Optional Polish
**None.** The presentation and references are rigorous, compact, and publication-ready.
