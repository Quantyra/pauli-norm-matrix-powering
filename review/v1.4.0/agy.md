# Google Antigravity review of v1.4.0

Automated manuscript review. [Editorial disposition](disposition.md)

## Initial scientific review

[Exact manuscript](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/73f03401988af404a20146758c8693e9a914a0e4/manuscript.tex), SHA-256 a52babde3c4f08fe017e7cc0e91cccbe180c144f3e9704e295226cc6b915b337.

# Independent Peer Review Report

**Manuscript Title:** *A fixed Pauli-norm threshold for diagonal matrix powering*
**Author:** Daniel Fredriksen (Quantyra Inc.)
**File Reviewed:** `manuscript.tex` (Lines 1–297; `\documentclass` through `\end{document}`)
**Candidate SHA-256:** `a52babde3c4f08fe017e7cc0e91cccbe180c144f3e9704e295226cc6b915b337`
**Verdict:** **REVISE**

---

## 1. Confirmation of Reading & Proof Verification

The complete preprint has been read from line 1 to line 297 using only the built-in reader. As requested, reading is confirmed by explicitly examining **Theorem 5** (`\ref{thm:twostep}`, lines 223–225) and two central mathematical steps in its proof (lines 226–247):

1. **Spectral Rayleigh Quotient on the Core Submatrix $A_U$ (Lines 230–236):**
   For the core layer set $U$ over times $t \in \{2, \ldots, \ell+1\}$ with $\ell = 162$ ($p = 2\ell = 324$ basis words across spectator $0$, control $1$, and target $\{0, 1\}$), the interior diagonal is bounded by $(1-s)^2 \ge 1 - 2s$, and ordinary adjacent blocks equal $s(1-s)V_t$. On a uniform two-component vector, permutations evaluate to $1$, while the three internal Hadamards at $t = 28, 82, 136$ evaluate to $\sqrt{2}$. Accounting for the missing boundary edge yields excess parameter $\gamma = [3(\sqrt{2}-1)-1]/\ell > 0$ ($\approx 0.001498$). Applying the uniform unit vector on $U$ to $A_U = |C_U|$ with entry perturbation $3\tau$ rigorously yields:
   $$\lambda_{\max}(A_U) \ge 1 - 2s + 2s(1-s)(1+\gamma) - 3p\tau \ge 1 + \gamma s$$
   for all sufficiently large $u$.

2. **Even-Power Spectral Positivity and Connector Lower Bound on $(A^k)_{jj}$ (Lines 239–246):**
   The designated computational basis input $j$ connects to the coordinate $i \in U$ maximizing the top eigenvector coordinate ($(v_1)_i^2 \ge 1/p$) via a connector path of length $h \le h_0 = 400$ having edge weights at least $b = s/(8\sqrt{T})$. Because $k = 72KT^2$ is even, $k - 2h$ is strictly even. Therefore, every term in the diagonal spectral expansion $(A_U^{\,k-2h})_{ii} = \sum_r \lambda_r^{k-2h} (v_r)_i^2$ is non-negative ($(\lambda_r^2)^{(k-2h)/2} \ge 0$). Keeping the connector and this walk yields:
   $$(A^k)_{jj} \ge b^{2h}(A_U^{\,k-2h})_{ii} \ge p^{-1} b^{2h_0}(1+\gamma s)^{k-2h_0} = \exp(\Omega(T^2))$$
   since $ks = 18T^2$ dominates $2h_0 \ln b = -O(\log T)$, establishing $\operatorname{Var} Z \ge ((A^k)_{jj})^2 - 1 = \exp(\Omega(T^2))$.

---

## 2. In-Depth Audit of Appendix B & Theorem 5

### Exact Scope
- **Target of Lower Bound:** The lower bound strictly targets the *single-trial variance* of a two-step collected computational-basis importance sampler scoring returning paths ($x_0 = x_k = j$).
- **Proposal Invariance:** Crucially, the expectation of the absolute score $\mathbb{E}[|Z|] = (A^k)_{jj}$ is an invariant of the matrix power graph and does *not* depend on the proposal distribution $P(\gamma)$ (as long as $P(\gamma) > 0$ on the support of $w(\gamma)$). By Jensen’s inequality, $\mathbb{E}[Z^2] \ge (\mathbb{E}[|Z|])^2 = ((A^k)_{jj})^2$ holds for *every* full-support proposal.
- **Boundaries:** The theorem explicitly does *not* claim a computational hardness lower bound for all classical algorithms. As the manuscript notes in line 248, the circuit itself is classically tractable, and variance lower bounds leave open multi-step contractions, tensor networks, and estimators without bounded second moments.

### Primary-Source Attribution (Montanaro-Shao vs. Stahlke)
- **Stahlke [294]:** Correctly cited in line 227 for the path interference quantity $(A^k)_{jj} = (|C|^k)_{jj}$. Stahlke (Phys. Rev. A 90, 022302, 2014) introduced path interference and analyzed path-sampling variance driven by absolute path sums.
- **Montanaro-Shao [292]:** Line 221 cites `\cite[Prop.~5.5]{ms}` for "computational-basis importance sampling". This is an attribution error. Montanaro and Shao (STOC 2024 / arXiv:2311.06999) investigate quantum and classical query complexity in the black-box sparse-access model; Section 5 specifically addresses classical query *lower bounds*. Proposition 5.5 is a lower bound result, not the foundational algorithmic definition of computational-basis path/importance sampling.

### Audit of the Promised Circuit
- The family uses $n=3$ wires (spectator $0$, control $1$, target $0$) with $8u$ pairs of sweeps alternating target Hadamard and control-to-target CNOT ($u \ge 1$).
- On the active subspace, the operation on the target qubit is $(XH)^{8u} = (R_y(\pi/2))^{8u} = (I)^{u} = I$. The output qubit remains in $\ket{0}$.
- Because $\Pi$ projects onto $\ket{1}$, the acceptance probability is $p = 0 \le 1/3$ (a valid promised NO instance).

### Constants & Designated Return Check
- **Designated Return:** The designated return is $(A^k)_{jj} = (|C|^k)_{jj}$ at the problem's designated basis input $j$ (time $t=0$, state $\ket{0, 1, 0}$). All connector steps correctly start and end at $j$.
- **Constants:**
  - $D = n(2n+3) = 27$ for $n=3$, $T = 27(r-1)+2$.
  - Sweep second-slot transition times $27a+1$ place Hadamards at $t = 28$ ($a=1$), $t = 82$ ($a=3$), and $t = 136$ ($a=5$). All three fall strictly inside $U$ ($2 \le t \le 163$ for $\ell = 162$), while the fourth Hadamard at $t = 190$ is outside.
  - $\gamma = [3(\sqrt{2}-1)-1]/162 > 0$ correctly accounts for the boundary loss.
  - $s = 1/(4K)$, $m = 144KT^2$, $k = m/2 = 72KT^2$, $ks = 18T^2$, and $b = s/(8\sqrt{T})$ are completely consistent with Appendix A.

### Does the Result Legitimately Strengthen the Paper?
**Yes.** The central theme of the paper is the demarcation between classical samplability and quantum hardness under a constant Pauli-norm cap. While Theorem 3 and Corollary 4 establish the limits of classical *Pauli-basis* sampling (showing the trial budget grows as $\exp(\Theta(T\sqrt{N}))$), Appendix B and Theorem 5 demonstrate that switching to a *computational-basis* random walk—even with exact two-step term consolidation—cannot escape an even worse exponential variance explosion $\exp(\Omega(T^2))$ caused by destructive path interference. This provides valuable theoretical insight into the sign problem inherent in diagonal matrix powering.

---

## 3. Pre-Existing Errors Affecting This Release

1. **Corrupted DOI for Reference [cif] (Line 257):**
   Reference `\bibitem{cif}` specifies:
   `\href{https://doi.org/10.1103/g5x4-jcsz}{doi:10.1103/g5x4-jcsz}`
   This DOI identifier (`g5x4-jcsz`) is malformed. The standard APS PRX Quantum DOI schema (matching reference `\bibitem{wang}` on line 262) is:
   `https://doi.org/10.1103/PRXQuantum.7.020364` (or the appropriate volume/article identifier).
2. **Citation Misattribution in Appendix B (Line 221):**
   Attributing computational-basis importance sampling to `\cite[Prop.~5.5]{ms}` misidentifies the primary literature. Montanaro-Shao Prop. 5.5 is a classical query lower bound, whereas the path importance-sampling estimator and its variance analysis originate in the quantum walk literature and Stahlke [294].

---

## 4. Mandatory Corrections

1. **Fix Reference [cif] DOI (Line 257):** Replace `doi:10.1103/g5x4-jcsz` with the official APS PRX Quantum DOI (`doi:10.1103/PRXQuantum.7.020364` or registered CrossRef DOI).
2. **Correct Attribution in Line 221:** Revise `"This is computational-basis importance sampling~\cite[Prop.~5.5]{ms} applied after exact two-step collection"` to cite Stahlke~\cite{stahlke} (or standard path-sampling literature) for the algorithm, reserving `\cite{ms}` for sparse-access query complexity.

---

## 5. Optional Changes

1. **Clarification in Line 224 (Theorem 5 Statement):** Mention explicitly in the theorem statement or immediately after that $Z$ denotes the estimator for the returning path sum to $j$, and that the lower bound applies to single-trial variance rather than total classical sample complexity.
2. **Explicit Mention of NO-Instance Context (Line 229):** Explicitly note that the $8u$-pair schedule realizes a NO instance ($p = 0$) within the PromiseBQP gap.

## Bibliographic clarification

[Exact manuscript](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/a91e2771177a310165abf776e2b6cebe28131d54/manuscript.tex), SHA-256 85e4ecc7c485090f66b2433f57c1c8b8f20c4c64d648b23ae5e47a51c2d67897.

# Independent Peer Review Report

**Manuscript Title:** *A fixed Pauli-norm threshold for diagonal matrix powering*
**Author:** Daniel Fredriksen (Quantyra Inc.)
**File Reviewed:** [`manuscript.tex`](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/a91e2771177a310165abf776e2b6cebe28131d54/manuscript.tex#L1-L297) (Lines 1–297; `\documentclass` through `\end{document}`)
**Candidate SHA-256:** `85e4ecc7c485090f66b2433f57c1c8b8f20c4c64d648b23ae5e47a51c2d67897`
**Verdict:** **READY**

---

## 1. Confirmation of Reading & Proof Verification

The complete preprint has been read from line 1 to line 297 using exclusively the built-in file reader without executing external commands or modifying files. Reading is confirmed by auditing **Theorem 5** (`\ref{thm:twostep}`, [lines 223–225](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/a91e2771177a310165abf776e2b6cebe28131d54/manuscript.tex#L223-L225)) and two central mathematical steps in its proof ([lines 226–247](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/a91e2771177a310165abf776e2b6cebe28131d54/manuscript.tex#L226-L247)):

1. **Spectral Rayleigh Quotient on the Core Submatrix $A_U$ ([Lines 230–236](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/a91e2771177a310165abf776e2b6cebe28131d54/manuscript.tex#L230-L236)):**
   For the core time set $U$ over times $t \in \{2, \ldots, \ell+1\}$ with $\ell = 162$ ($p = 2\ell = 324$ basis words across spectator $0$, control $1$, and target $\{0, 1\}$), the diagonal of $B_*^2$ is bounded below by $(1-s)^2 \ge 1 - 2s$, and ordinary adjacent blocks equal $s(1-s)V_t$. Tested against the uniform two-component vector $w = \frac{1}{\sqrt{2}}(1, 1)^T$, permutations evaluate to $w^T |P| w = 1$, while the three internal Hadamards at $t = 28, 82, 136$ evaluate to $w^T |H| w = \sqrt{2}$. Accounting for the missing boundary edge yields the positive excess parameter:
   $$\gamma = \frac{3(\sqrt{2}-1)-1}{\ell} \approx 0.001498 > 0.$$
   Applying the uniform unit vector on $U$ to $A_U = |C_U|$ with entry perturbation bounded by $3\tau$ rigorously yields:
   $$\lambda_{\max}(A_U) \ge 1 - 2s + 2s(1-s)(1+\gamma) - 3p\tau \ge 1 + \gamma s$$
   for all sufficiently large $u$, because the linear excess $2\gamma s$ strictly dominates $2(1+\gamma)s^2 + 3p\tau = O(s^2)$.

2. **Even-Power Spectral Positivity and Connector Lower Bound on $(A^k)_{jj}$ ([Lines 239–246](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/a91e2771177a310165abf776e2b6cebe28131d54/manuscript.tex#L239-L246)):**
   The designated computational basis input $j$ connects to the coordinate $i \in U$ maximizing the top eigenvector coordinate ($(v_1)_i^2 \ge 1/p$) via a connector path of length $h \le h_0 = 400$ having edge weights at least $b = s/(8\sqrt{T})$. Because $k = 72KT^2$ is an even integer, $k - 2h$ is strictly even. Therefore, every term in the diagonal spectral expansion of the real symmetric submatrix:
   $$(A_U^{\,k-2h})_{ii} = \sum_{r=1}^p \lambda_r^{k-2h} (v_r)_i^2$$
   is non-negative ($(\lambda_r^2)^{(k-2h)/2} \ge 0$). Retaining only the connector and the top mode on $U$ yields:
   $$(A^k)_{jj} \ge b^{2h}(A_U^{\,k-2h})_{ii} \ge p^{-1} b^{2h_0}(1+\gamma s)^{k-2h_0} = \exp(\Omega(T^2)),$$
   since $ks = 18T^2$ dominates $2h_0 \ln b = -O(\log T)$. By Jensen's inequality, $\mathbb{E}[Z^2] \ge (\mathbb{E}[|Z|])^2 = ((A^k)_{jj})^2$, establishing $\operatorname{Var} Z \ge ((A^k)_{jj})^2 - 1 = \exp(\Omega(T^2))$.

---

## 2. In-Depth Audit of Appendix B & Theorem 5

### Exact Scope
- **Target of Lower Bound:** The lower bound targets the *single-trial variance* of a computational-basis importance sampler scoring returning paths ($x_0 = x_k = j$) on the contracted operator $C = B^2$.
- **Proposal Invariance:** Crucially, the absolute score expectation $\mathbb{E}[|Z|] = (A^k)_{jj} = (|C|^k)_{jj}$ is an algebraic invariant of the matrix power graph and does *not* depend on the proposal distribution $P(\gamma)$ (provided $P(\gamma) > 0$ on the support of $w(\gamma)$). By Jensen's inequality, $\mathbb{E}[Z^2] \ge (\mathbb{E}[|Z|])^2 = ((A^k)_{jj})^2$ holds for *every* full-support proposal.
- **Boundaries:** The theorem explicitly does *not* claim computational hardness for all classical algorithms. As noted in [line 248](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/a91e2771177a310165abf776e2b6cebe28131d54/manuscript.tex#L248), the underlying 3-wire circuit is classically tractable, and single-trial variance lower bounds leave open multi-step contractions, tensor networks, and estimators without bounded second moments.

### Primary-Source Attribution (Montanaro-Shao and Stahlke)
- **Reassessment of First-Round Objections:** The first-round objection against `\cite[Prop.~5.5]{ms}` was unfounded. Independent verification against the primary source (arXiv:2311.06999v3, Section 5.2, Proposition 5.5 and eqs. 5.4 ff.) confirms that Montanaro and Shao explicitly construct and analyze the classical sparse-matrix polynomial estimator via importance-sampled random walks. Line 221 accurately credits this algorithmic formulation.
- **Stahlke [294]:** Correctly credited in [line 227](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/a91e2771177a310165abf776e2b6cebe28131d54/manuscript.tex#L227) for the path interference quantity $(A^k)_{jj} = (|C|^k)_{jj}$ and the path-importance sampling framework.
- **Cifuentes et al. [257]:** Crossref independently confirms that DOI `10.1103/g5x4-jcsz` is valid and resolves to *PRX Quantum* **7**, 020364 (2026).

### Audit of the Promised Circuit
- **Circuit Specification:** $n=3$ wires (spectator 0, control 1, target initialized to 0). Between initial and final identity sweeps, $8u$ pairs of sweeps alternate a target Hadamard and a control-to-target CNOT in the second slot of each sweep ($u \ge 1$).
- **Coherent Action:** On the subspace with spectator 0 and control 1, the gate pair acts on the target qubit as $XH = \begin{pmatrix} \cos(\pi/4) & -\sin(\pi/4) \\ \sin(\pi/4) & \cos(\pi/4) \end{pmatrix}$, an exact rotation by $\pi/4$ in $\mathbb{R}^2$. Applying $8u$ pairs results in a net rotation of $8u \times (\pi/4) = 2\pi u$, which is the identity. The target qubit returns exactly to $|0\rangle$, yielding acceptance probability $p = 0$ (a promised NO instance).

### Audit of Constants and Designated Return
- **Layering and Hadamards:** In AGIK clock sweeps of width $n=3$, $D = n(2n+3) = 27$. The second slot of sweep $a$ occurs at time $27a+1$. Sweep 0 is identity. Sweeps 1, 3, and 5 place Hadamards at $t = 28, 82, 136$. Sweeps 2, 4, and 6 place CNOTs (permutations).
- **Core Length:** $\ell = 162 = 6 \times 27$ covers exactly six complete sweeps. The interior layers $t \in \{2, \ldots, 163\}$ contain precisely the 3 Hadamards at $t = 28, 82, 136$.
- **Designated Return:** Paths begin and end at the computational basis state $j$ ($x_0 = x_k = j$), with non-returning paths scored as zero. The mean is $\mathbb{E}[Z] = (C^k)_{jj} = (B^m)_{jj}$, matching the designated moment.

### Legitimacy of Strengthening the Manuscript
Theorem 5 legitimately strengthens the manuscript. While Corollary 4 and Section 4 show that Pauli-product sampling exhibits exponential variance on the rounded chain instances, Theorem 5 proves that transitioning to classical computational-basis path importance sampling (even after exact two-step block collection $C = B^2$) remains susceptible to an exponential single-trial variance barrier $\exp(\Omega(T^2))$. This demonstrates that the barrier is intrinsic to the path interference structure rather than an artifact of the Pauli basis.

---

## 3. Audit of Pre-Existing Errors Across the Preprint

A comprehensive audit of the entire text revealed no genuine mathematical, logical, or bibliographic errors:
1. **Decision Promises and Gaps ([Lines 28–32, 126–133](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/a91e2771177a310165abf776e2b6cebe28131d54/manuscript.tex#L28-L32)):** The separation between $v_{\rm YES} \ge 487/1536 \approx 0.3171 > 9/32 = 0.28125$ and $v_{\rm NO} \le 287/1536 \approx 0.1868 < 7/32 = 0.21875$ guarantees that any estimate within $1/32$ compared to the midpoint $1/4$ correctly decides the instance.
2. **Classical Chebyshev Filter ([Lines 51–72](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/a91e2771177a310165abf776e2b6cebe28131d54/manuscript.tex#L51-L72)):** The upper bound error analysis (truncation $1/128$ + sampling $1/64$ + rounding $1/512 = 13/512 < 1/32$) and the Markov inequality converse ($W_\lambda(f) \ge 2^{\sqrt{A}/3 - 8}$) are completely sound.
3. **Hamiltonian History State and Chain Encoding ([Lines 140–176](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/a91e2771177a310165abf776e2b6cebe28131d54/manuscript.tex#L140-L176)):** The boundary modification $h_\star$, the legal ground state distribution $\pi_0 = 1/2, \pi_t = 1/(2T)$, the spectral gap $1/(6T^2)$, and dyadic rounding parameter bounds are verified.

---

## 4. Verdict and Recommended Actions

- **Verdict:** **READY**
- **Mandatory Corrections:** None (0).
- **Optional Changes:** None required for publication. (Optionally, a brief parenthetical in line 229 noting $(XH)^8 = I$ could offer quick intuition to casual readers).

## Final scientific review

[Exact manuscript](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/ea2bbc797621a67ecabf262e9113678adc94610a/manuscript.tex), SHA-256 7681b653c255957031d0a61edfe766091116a1b5f6bfed577379eb86a435a08c.

# Independent Review Report: Pauli-Norm Threshold for Diagonal Matrix Powering

**Verdict:** **READY**
**Evaluated Document:** [manuscript.tex](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/ea2bbc797621a67ecabf262e9113678adc94610a/manuscript.tex) (Lines 1–303, SHA-256 `7681b653c255957031d0a61edfe766091116a1b5f6bfed577379eb86a435a08c`)

---

## 1. Confirmation of Candidate & Theorem 5 Proof Steps

The complete candidate [manuscript.tex](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/ea2bbc797621a67ecabf262e9113678adc94610a/manuscript.tex) was read from `\documentclass` ([L1](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/ea2bbc797621a67ecabf262e9113678adc94610a/manuscript.tex#L1)) to `\end{document}` ([L303](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/ea2bbc797621a67ecabf262e9113678adc94610a/manuscript.tex#L303)). Appendix B and Theorem 5 ([L223–L254](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/ea2bbc797621a67ecabf262e9113678adc94610a/manuscript.tex#L223-L254)) were audited in full.

Specific mathematical confirmation steps from the proof of Theorem 5:
1. **Spectral Lower Bound on $A_U$ ([L234–L236](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/ea2bbc797621a67ecabf262e9113678adc94610a/manuscript.tex#L234-L236)):**
   $$\lambda_{\max}(A_U) \ge 1-2s+2s(1-s)(1+\gamma)-3p\tau \ge 1+\gamma s$$
   derived using the uniform unit vector on the $p = 2\ell = 324$ words of $U$ ($\ell = 162$), where internal Hadamards at times $t \in \{28, 82, 136\}$ contribute quadratic form $\sqrt{2}$ vs. $1$ for permutations, giving boundary-corrected gain $\gamma = [3(\sqrt{2}-1)-1]/162 > 0$.
2. **Designated Return & Capped Score Domination ([L243–L244](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/ea2bbc797621a67ecabf262e9113678adc94610a/manuscript.tex#L243-L244), [L250–L253](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/ea2bbc797621a67ecabf262e9113678adc94610a/manuscript.tex#L250-L253)):**
   $$(A^k)_{jj} \ge b^{2h}(A_U^{\,k-2h})_{ii} \ge p^{-1} b^{2h_0}(1+\gamma s)^{k-2h_0} = \exp(\Omega(T^2))$$
   with connector bound $b = s/(8\sqrt{T})$, length $h_0 = 400$, and power $ks = 18T^2$. Under binary rejection capping at $R = \lceil\log_2(12kM)\rceil+1$, every score event satisfies $\nu'(E) \ge \frac{11}{12}\nu(E)$, yielding the variance bound at shifted capped mean $a = \mathbb{E}_{\nu'} Z$:
   $$\operatorname{Var}_{\nu'} Z \ge \tfrac{11}{12} \int (z-a)^2\,d\nu(z) = \tfrac{11}{12} \big(\operatorname{Var}_\nu Z + (\mathbb{E}_\nu Z - a)^2\big)$$
   without requiring an independent thinning assumption.

---

## 2. Reassessment of First-Round Objections

1. **DOI for Reference `[cif]` ([L264](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/ea2bbc797621a67ecabf262e9113678adc94610a/manuscript.tex#L264)):**
   - *Status:* **False Objection (No Error).**
   - *Findings:* Crossref resolves `10.1103/g5x4-jcsz` directly to S. Cifuentes et al., *Quantum computational complexity of matrix functions*, *PRX Quantum* **7**, 020364 (2026). The short alphanumeric handle format is registered and valid.
2. **Attribution to Montanaro-Shao and Stahlke ([L221](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/ea2bbc797621a67ecabf262e9113678adc94610a/manuscript.tex#L221)):**
   - *Status:* **False Objection (Attribution is Accurate).**
   - *Findings:* Montanaro & Shao (arXiv:2311.06999v3, Section 5.2, Proposition 5.5 and eqs. 5.4ff) explicitly define and analyze the sparse-matrix polynomial estimator via importance-sampled random walks. Line 221 accurately cites Montanaro-Shao for the sparse-matrix walk estimator applied to the collected matrix $C = B^2$ while properly citing Stahlke~\cite{stahlke} for the general path-importance framework and the path interference quantity $(A^k)_{jj}$.

---

## 3. Audit of Appendix B and Theorem 5

- **Promised Circuit:**
  The 3-wire circuit family (spectator 0, control 1, target 0) executes $8u$ pairs of sweeps alternating target Hadamard and control-to-target CNOT ($u \ge 1$). On the active subspace, the target qubit undergoes $(XH)^{8u} = (R_y(\pi/2))^{8u} = I^u = I$, remaining in $\ket{0}$. The measurement $\Pi$ tests output bit 1; thus $p = 0 \le 1/3$, creating a valid $\text{PromiseBQP}$ NO instance.
- **Constants & Designated Return:**
  - For $n=3$, $D = n(2n+3) = 27$ and $T = 27(r-1)+2$.
  - Second-slot transition times $27a+1$ locate Hadamards at $t = 28$ ($a=1$), $t = 82$ ($a=3$), and $t = 136$ ($a=5$), which lie strictly within $U$ ($2 \le t \le 163$ for $\ell = 162$). The fourth Hadamard at $t = 190$ ($a=7$) is outside.
  - Boundary loss constant $\gamma = [3(\sqrt{2}-1)-1]/162 > 0$ is correct.
  - $s = 1/(4K)$, $m = 144KT^2$, $k = m/2 = 72KT^2$, $ks = 18T^2$, and $b = s/(8\sqrt{T})$ are completely consistent with Appendix A.
  - Designated return $(A^k)_{jj} = (|C|^k)_{jj}$ starts and terminates at basis index $j$ ($t=0$, state $\ket{0, 1, 0}$).
- **Legitimate Strengthening:**
  **Yes.** While Theorem 3 and Corollary 4 demonstrate the failure of classical *Pauli-basis* sampling (growth $\exp(\Theta(T\sqrt{N}))$), Theorem 5 shows that switching to a *computational-basis* random walk—even with exact two-step term consolidation—faces an even worse exponential variance explosion $\exp(\Omega(T^2))$ from destructive path interference.

---

## 4. Pre-Existing Errors Affecting This Release

**None.** A complete audit of the text, constants, proofs, reductions, and references revealed no genuine pre-existing mathematical, logical, or bibliographic errors.

---

## 5. Mandatory Corrections

**None.** The candidate is ready for release as-is.

---

## 6. Optional Changes

1. **Clarification on Estimator Scope ([L224](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/ea2bbc797621a67ecabf262e9113678adc94610a/manuscript.tex#L224)):** Optionally restate in the body of Theorem 5 that $Z$ denotes the estimator for the returning path sum to $j$.
2. **NO-Instance Reminder ([L229](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/ea2bbc797621a67ecabf262e9113678adc94610a/manuscript.tex#L229)):** A brief parenthetical explicitly noting that $p = 0$ is a valid PromiseBQP NO instance could provide additional context for readers.
