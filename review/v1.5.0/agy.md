# Google Antigravity review of v1.5.0

Automated manuscript review. [Editorial disposition](disposition.md)

## Initial review

[Exact manuscript](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/a3af1686c9981c30b43ebd8e9d9b392b7352999d/manuscript.tex), SHA-256 1ac24c84e822e178270bc5b6c708ac10f3f7e8179fe426378bf20470fa7c9a0d.

# Referee Report on `manuscript.tex`

**Recommendation:** **READY**

---

### Confirmation of File Read
I confirm that I have read the complete manuscript `manuscript.tex` (from line 1 `\documentclass[11pt]{article}` to line 366 `\end{document}`) in the working directory using only the built-in file reader without external commands or hash utilities.

Confirmation is anchored explicitly in **Theorem 6** (`\label{thm:confidence}`, lines 259–265) and two specific mathematical steps in its proof:
1. **The exact grid alignment and integer multiplier step** (lines 271–274): With $J = 49n - 10 = 2^a$, $K = 256J$, $s = 1/(4K)$, and grid spacing $\eta = \tau / (2^{19}J)$, the integer multiplier evaluates exactly to:
   $$F = \frac{(1-\tau)s}{512\eta} = \tau^{-1} - 1,$$
   ensuring that all ordinary normalized Pauli traces lie on the $\eta$-grid and that exceptional off-diagonal blocks (with magnitudes $8F/\sqrt{2}$ and $8F\sqrt{T}/(T+1)$ grid units) scale uniformly under inward rounding.
2. **The return-path Markov cut conditioning step** (lines 298–303): On any ideal clock path visiting $D$ (clock time $\ge g-1$) and returning to $t_k = 0$, each of the $q$ work-bit cuts is crossed in reverse, with the final crossing of each cut generating an independent fair coin flip, giving:
   $$\Pr_{\rm ideal}(D, X_k = j) = 2^{-q} \Pr_{\rm ideal}(D, t_k = 0) \le 2^{-q},$$
   which governs the score coupling and establishes $d_{\rm TV}(P_+, P_-) \le 2^{-q}$.

---

## 1. Skeptical Mathematical Referee Audit of Appendix C (Theorem 6)

### A. Quantifier Audit
* **Circuits & Dimension:** For every integer $q \ge 1$, the author sets $a = 11 + 21u$ ($u \ge 0$) and takes the least integer width $n = (2^a + 10)/49$ satisfying $n \ge 3q + 5$.
  * *Arithmetic verification:* $2^{11} = 2048 \equiv 39 \pmod{49}$ and $2^{21} = 2097152 \equiv 1 \pmod{49}$. Thus $2^a + 10 \equiv 39 + 10 = 49 \equiv 0 \pmod{49}$, guaranteeing that $n$ is an integer for all $u \ge 0$. Successive ratios of $2^a$ are $2^{21}$, ensuring $n = \Theta(q)$ with constructive existence for every $q \ge 1$.
  * *Disjoint register allocation:* Wires 1 and 2 are spectators ($0$); work bits occupy wires $4, 7, \dots, 3q+1$; control wire $n-1$ and target wire $n$ satisfy $n-1 \ge 3q+4 > 3q+1$. All registers are disjoint.
* **Admissible Rounding & Schedule:** Both YES and NO instances share the identical clock schedule ($N = 7n$ sites, $T = 6n(2n+3) + n - 1$), the same marked word $j$, the same power $m = 144KT^2$, and the identical dyadic rounding grid spacing $\eta$.
* **Decoder & Trial Cap:** The sample lower bound $M \ge 2^q/3$ quantifies over *all* common decision rules (arbitrary hypothesis tests $\delta: \mathbb{R}^M \to \{\text{YES}, \text{NO}\}$) achieving worst-case success probability at least $2/3$, holding both for ideal draws and under any positive retry cap $R \ge 1$ with exhaustion returning score zero.

### B. Claimed Advance over Appendix B and Janzing–Wocjan
* **Advance over Appendix B:** Appendix B (Theorem 5) proves exponential single-trial variance $\operatorname{Var}(Z) \ge \exp(\Omega(T^2))$ for a returning-path sampler on a 3-wire family. Variance lower bounds alone do not rule out non-mean decoders (e.g., median-of-means, threshold/tail statistics). Theorem 6 establishes a genuine information-theoretic lower bound: $d_{\rm TV}(P_+, P_-) \le 2^{-q}$. This limits *every* possible classical test processing $M$ row-sampled scores.
* **Advance over Janzing–Wocjan [36]:** Janzing and Wocjan (2006) proved classical walk hardness on mixing problems where the true underlying endpoint distribution difference was exponentially small. In Fredriksen's Theorem 6, the actual matrix powers have a **constant separation gap** ($v_{\rm YES} \ge 9/32$ vs $v_{\rm NO} \le 7/32$, gap $\ge 1/16$), and the sampler observes *signed path scores* whose expectation equals the matrix element. Theorem 6 proves that despite this constant gap, the single-score laws observed by this two-step row sampler remain within total variation distance $2^{-q}$. The manuscript honestly clarifies that the source circuits are easily distinguished by directly inspecting the final gate (line 314); the lower bound specifically restricts the row-sampling algorithm.

### C. Audit of Both Promises
* **Contraction & Positivity:** The rounded matrix satisfies $\norm{B} \le 1 - \tau/2 < 1$ and is strictly positive definite.
* **Pauli Cap:** $\lambda(B) \le 1 + sK \le 5/4 \le 3/2 = c$.
* **Separation Promise:** In the YES circuit, wire $n-1$ is $1$, wire $n$ starts at $0$, and the penultimate gate of sweep 5 is CNOT, setting wire $n$ to $1$ ($p_{\rm YES} = 1$). In the NO circuit, identity is applied ($p_{\rm NO} = 0$). With the conservative finite-precision allowances from Appendix A:
  $$v_{\rm YES} \ge \frac{487}{1536} > \frac{9}{32} = \frac{432}{1536}, \qquad v_{\rm NO} \le \frac{287}{1536} < \frac{7}{32} = \frac{336}{1536}.$$
  Both promises are strictly satisfied with additive margins exceeding $1/32$.

### D. Size Convention Audit
* In Section 1, the power $m$ is given in unary, and input length is $L$. In Theorem 6, $T = \Theta(n^2)$ and $K = 256J = \Theta(n)$, so $m = 144KT^2 = \Theta(n^5) = \Theta(q^5)$.
* The number of sites is $N = 7n = \Theta(q)$, each encoded in 4 qubits ($4N = 28n$ qubits).
* Total written input length $L$ scales as $\Theta(m + N \log n) = \Theta(q^5)$. The lower bound $M \ge 2^q/3 = \exp(\Omega(L^{1/5}))$ is superpolynomial in $L$ and exponential in $q$, adhering strictly to the unary power input convention.

### E. Audit of Substantive Rounding & Coupling Calculations
1. **Coefficient Grouping and Block Invariance:**
   * High 3-bit XOR masks for transitions on physical sites: $GR \leftrightarrow LG$ has mask $(2,1)$ and marked transition $SR \leftrightarrow L_0G$ has mask $(5,1)$. Competing transitions have masks $(2,2), (1,2), (3,0), (7,4), (0,3), (1,2)$. Since all gate rewrites flip both sites, they cannot share Pauli labels with single-site terms or with other bonds.
   * Hadamard off-diagonal Pauli coefficients in $(1-\tau)B_*$ have magnitude $\frac{(1-\tau)s}{64\sqrt{2}} = \frac{8F}{\sqrt{2}}\eta$. All nonzero terms in the block share identical magnitude, so rounding toward zero on the $\eta$-grid scales the entire block by a positive scalar, preserving zeros, signs, and unitarity up to scale.
   * Sites 1 and 2 carry only spectators fixed at $0$, so diagonal corrections act as exact scalars on the work bits. Hence, blocks of $C = B^2$ on the work space satisfy $C_{tt} \propto I$, $C_{t+1,t} \propto U_t$, and $C_{t+2,t} \propto U_{t+1}U_t$, where $U_t \in \{I, H\}$.
2. **Autonomous Clock Walk & TV Coupling:**
   * Absolute row sums in each block of $C$ are independent of the input work string (row sums are $1$ for identity and $\sqrt{2}$ for Hadamard). Clock transitions are autonomous.
   * Consecutive Hadamards are separated by two identity sweeps, so any two-step jump crosses at most one Hadamard.
   * Differing gate occurs at edge $g \leftrightarrow g+1$ (last gate of sweep 5). For $t \le g-2$, two-step jumps reach at most $t+2 \le g$ and only involve edges up to $g-1 \leftrightarrow g$. Rows $t \le g-2$ are identical in YES and NO.
   * Visiting $D$ (time $\ge g-1$) and returning to $0$ requires crossing all $q$ Hadamard cuts in reverse. The final crossing of each cut produces an independent fair coin flip. Thus, $\Pr(D, X_k = j) \le 2^{-q}$.
   * Score distribution decomposes into common measure $\mu$ (mass $1-h$) on paths avoiding $D$, and mass at zero on abort/nonreturn. Unmatched mass is at most $\max(b_+, b_-) \le 2^{-q}$.
   * Total variation distance satisfies $d_{\rm TV}(P_+, P_-) \le 2^{-q}$.
   * For $M$ independent trials:
     $$d_{\rm TV}(P_+^{\otimes M}, P_-^{\otimes M}) \le 1 - (1 - 2^{-q})^M \le M 2^{-q}.$$
     Succeeding with probability $\ge 2/3$ requires gap $\ge 1/3 \le M 2^{-q} \implies M \ge 2^q/3$.

---

## 2. Manuscript-Wide Audit (Sections 1–4, Appendices A & B)

* **Section 1 & 2:** Theorem 1 and Theorem 3 bounds are correct. Truncation of the Chebyshev series at degree $D = \min(q, \lceil\sqrt{12q}\rceil)$ gives error $\le 2e^{-6} < 1/128$. The converse using Markov’s inequality on interval $[1-h/2, 1]$ correctly yields $W_\lambda(f) \ge 2^{\sqrt{A}/3 - 8}$.
* **Section 3 & 4:** Pre-idling cyclic clock construction, Hadamard clock conjugation, finite dyadic grid rounding, and error accumulation to $3/512$ are mathematically consistent. YES/NO acceptance margins ($487/1536$ vs $287/1536$) leave the required $> 1/32$ margin from $1/4$.
* **Appendix A & B:** AGIK clock analysis, spectral gap of grounded history state ($\ge 1/(6T^2)$), rank bounds for $\mu$, and returning-path variance bound $\operatorname{Var}(Z) \ge \exp(\Omega(T^2))$ on the 3-wire alternating Hadamard construction are solid.

No genuine mathematical errors, invalid bounds, or quantifier flaws were found in the manuscript.

---

## 3. Mandatory Changes
* **None.** The manuscript is mathematically rigorous and complete as written.

---

## 4. Optional Changes (Expositional Suggestions)
1. **Clarification of Control Ancilla Initial State:** In line 269, note explicitly that basis state $\ket{j}$ has wire $n-1$ set to $\ket{1}$ in the computational basis (which is fully admissible under Corollary 2).
2. **Explicit Labeling of the Differing Transition Index:** In line 300, explicitly stating that $g = 5D + 2(n-1)$ is the time of the sweep-5 terminal gate would make the boundary check for row $g-2$ immediately apparent to casual readers.
3. **Notation for Trial Count in Appendix C:** In Theorem 6 (line 264), consider using $M_{\rm trials}$ instead of $M$ to prevent any potential visual confusion with the cyclic clock dimension $M$ defined in Section 3, though within Appendix C the context is unambiguous.

## Release candidate

[Exact manuscript](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/3311223ececf1f1cf2ff5e9b15916b1a22bf4fd8/manuscript.tex), SHA-256 57db9a2089f44b99cc48308102792527eae476084bf426e5d7aaab1d03041da2.

### Recommendation: **READY**

---

### Candidate Confirmation
I confirm that I have read the complete `manuscript.tex` (lines 1–366, from `\documentclass[11pt]{article}` to `\end{document}`) in the working directory using only the built-in file reader. The text includes the complete statement and proof of **Theorem 6** (lines 259–312). Specifically:
1. **Mathematical Step 1 (Rounding of Off-Diagonal Hadamard Pauli Coefficients, lines 282–285):** Nonzero coefficients of $(E+E^\dagger)\otimes I\otimes(X+Z)/\sqrt{2}$ in $(1-\tau)B_*$ have exact magnitude $\frac{(1-\tau)s}{64\sqrt{2}} = \frac{8F}{\sqrt{2}}\eta$. Because all nonzero terms in the block share identical magnitude, rounding toward zero on the $\eta$-grid rescales the entire block uniformly by the positive factor $\frac{\lfloor 4\sqrt{2}F\rfloor}{4\sqrt{2}F}$, preserving zeros, signs, and unitarity up to scale.
2. **Mathematical Step 2 (Autonomous Reversal Coupling and TV Bound, lines 300–311):** Paths visiting $D$ ($t \ge g-1$) that return to clock time $0$ must traverse all $q$ Hadamard cuts in reverse. The final crossing of each cut produces an independent fair coin flip on the corresponding work bit, bounding the return probability by $\Pr(D, X_k = j) \le 2^{-q}$. Decomposing into the common measure $\mu$ on paths avoiding $D$ and unmatched mass $\le 2^{-q}$ yields $d_{\rm TV}(P_+, P_-) \le 2^{-q}$, which establishes $d_{\rm TV}(P_+^{\otimes M}, P_-^{\otimes M}) \le M 2^{-q}$ and the sample lower bound $M \ge 2^q/3$.

---

### 1. Mathematical Referee Audit of Appendix C (Theorem 6)

#### A. Quantifiers
* **Family Existence:** For every integer $q \ge 1$, width $n = (2^a + 10)/49$ is guaranteed an integer for all $a = 11 + 21u$ ($u \ge 0$) by the congruences $2^{11} \equiv 39 \pmod{49}$ and $2^{21} \equiv 1 \pmod{49}$. Choosing the minimal $u \ge 0$ satisfying $n \ge 3q + 5$ uniquely fixes the instance. The universal quantifier $\forall q \ge 1$ is constructively satisfied.
* **Decoder Lower Bound:** The lower bound covers *all* decoders (deterministic or randomized) receiving $M$ independent scalar scores from the row sampler with score zero on abort/exhaustion. Under Le Cam's two-point testing lemma, any decision rule achieving worst-case success probability $\ge 2/3$ must have an output probability gap $\ge 1/3$. The coupling bound $d_{\rm TV}(P_+^{\otimes M}, P_-^{\otimes M}) \le 1 - (1 - 2^{-q})^M \le M 2^{-q}$ implies $M \ge 2^q/3$ unconditionally.

#### B. Claimed Advance over Appendix B and Janzing–Wocjan
* **Over Appendix B:** Theorem 5 established an exponential variance lower bound $\operatorname{Var}(Z) \ge \exp(\Omega(T^2))$ for a single returning-path trial on a 3-wire family. High variance alone does not formally preclude decision algorithms based on medians, quantiles, or higher moments. Theorem 6 advances this to an information-theoretic total variation bound $d_{\rm TV}(P_+, P_-) \le 2^{-q}$, precluding *any* classical decision rule using fewer than $2^q/3$ samples from this sampler.
* **Over Janzing–Wocjan (2006):** In Janzing and Wocjan's random walk mixing problem, the distinguishing signal lay in exponentially small variations of raw endpoint transition probabilities. Here, the raw matrix diagonals differ by a constant $\ge 1/16$ ($v_{\rm YES} \ge 487/1536$ vs $v_{\rm NO} \le 287/1536$), and each trial returns a reweighted, signed matrix-product score. Theorem 6 proves that even with signed path reweighting, the score distributions remain within $2^{-q}$ in total variation distance.

#### C. Verification of Both Promises
* **Norm and Pauli Weight Promise:** For $K = 256J$ and $s = 1/(4K)$, $B_* = I - sH$ satisfies $\lambda(B_*) \le 1 + sK = 5/4 \le 3/2 = c$, with $(3/4)I \le B_* \le I$. The inward rounding loss satisfies $\|\Delta B\| \le \tau/2$, ensuring $\lambda(B) \le 5/4 \le c$, $\|B\| \le 1 - \tau/2 < 1$, and positive definiteness.
* **YES/NO Separation Promise:** Circuits have ideal acceptance $p_{\rm YES} = 1$ and $p_{\rm NO} = 0$. Accounting for the pre-idling weighting, compilation tolerance, and inward rounding perturbation ($\le 3/512$), the diagonal values strictly satisfy $v_{\rm YES} \ge 487/1536 > 9/32$ and $v_{\rm NO} \le 287/1536 < 7/32$, retaining the required $> 1/32$ decision margin from $1/4$.

#### D. Size Conventions and Structural Parameters
* **Width and Site Count:** $N = 7n$ sites across $r = 7$ sweeps.
* **Term Count:** Within-block bonds carry 7 terms; the 6 block-crossing bonds carry 6 terms; 2 open-end terms and 1 terminal pin give $J = 7(7n - 1) - 6 + 3 = 49n - 10 = 2^a$ exact terms.
* **Late-Edge Index $g$:** Each sweep contains $n-1$ gate moves. In sweep 5 (starting at time $5D = 5n(2n+3)$), the gates occur at transitions $5D + i \leftrightarrow 5D + i + 1$ for $i = 0, \ldots, n-2$. The final gate move is therefore precisely at $g = 5n(2n+3) + n - 2$, connecting time $g$ to $g+1$.
* **First Width and Unary Size:** For $u = 0$, $a = 11$, width is $n = (2048 + 10)/49 = 42$.
  * $J = 2048$, $K = 256 \times 2048 = 524{,}288$.
  * $T = 6(42)(87) + 41 = 21{,}924 + 41 = 21{,}965$.
  * $m = 144 K T^2 = 144 \times 524{,}288 \times 21{,}965^2 = 75{,}497{,}472 \times 482{,}461{,}225 = 36{,}424{,}602{,}825{,}523{,}200$.
  The stated unary power matches exactly.

#### E. Contextual Clarifications in the Release Draft
* **Physical Gate vs Work-Coordinate Terminal Penalty:** In the physical computational basis, the YES and NO matrices differ only at the local gate transition $g \leftrightarrow g+1$ on bond $(n-1, n)$. In work-string coordinates (pulling the circuit unitaries through), the terminal pin at time $T = 6D + n - 1$ produces a differing diagonal at time $T$. Because $T - g = D + 1 \gg 2$, this diagonal difference is separated by an entire sweep from $g$ and cannot be reached by two-step jumps from $t \le g-2$.
* **Two Exceptional Within-Block Masks:** In the 4-bit site encoding, $GR \leftrightarrow LG$ has high-3-bit XOR mask $(2, 1)$, and marked $SR \leftrightarrow L_0G$ has mask $(5, 1)$. The competing within-block masks are $(2, 2)$, $(1, 2)$, $(3, 0)$, $(7, 4)$, $(0, 3)$, and $(1, 2)$. Neither $(2, 1)$ nor $(5, 1)$ coincides with any competing within-block mask. Because they flip both sites on their bond, they cannot share Pauli labels with single-site terms or with other bonds, isolating them completely in global collection.
* **AGIK Data Order and Spectator Wires 1 & 2:** Sites 1 and 2 only ever hold data from wires 1 and 2 or fixed flags. Since wires 1 and 2 are spectators permanently fixed at $\ket{0}$, the diagonal corrections supported on sites 1 and 2 act as exact scalars on the active work space, preserving $B_{tt} = d_t I$.

---

### 2. Manuscript-Wide Audit (Sections 1–4, Appendices A & B)

* **Sections 1–2:** Chebyshev series truncation at degree $D = \min(q, \lceil\sqrt{12q}\rceil)$ ensures truncation error $\le 2e^{-6} < 1/128$. Markov's derivative inequality applied to translated polynomial $g$ on $I = [1-h/2, 1]$ yields $W_\lambda(f) \ge 2^{\sqrt{A}/3 - 8}$.
* **Sections 3–4:** Clock Hadamard conjugation preserves Pauli weight ($\lambda(A') = \lambda(A)$) while concentrating weight $p/2$ on computational input $j$. Dyadic grid rounding with spacing $\le \tau/(2S)$ preserves positive definiteness and keeps cumulative operator error $\le 3/512$.
* **Appendices A & B:** Weighted history-state construction on AGIK chain maintains spectral gap $\ge 1/(6T^2)$. The Rayleigh quotient lower bound on submatrix $A_U$ ($1 + \gamma s$) correctly drives the returning-path variance bound $\operatorname{Var}(Z) \ge \exp(\Omega(T^2))$.

No mathematical errors, invalid bounds, or quantifier inconsistencies were found.

---

### 3. Mandatory Changes
* **None.** The manuscript is mathematically rigorous, sound, and ready for publication.

---

### 4. Optional Changes (Minor Expositional Polish)
1. **Definition of $g$ in Appendix C (line 269):** Adding a brief parenthetical note explicitly recalling that $5n(2n+3)$ is the start of sweep 5 and $n-2$ corresponds to the $(n-1)$-th gate move would make the transition index $g$ instantly transparent to readers without requiring back-referencing to Section 2 of AGIK.
2. **Clarification on Decoder Lower Bound (line 264):** In Theorem 6, explicitly mentioning that $M$ denotes the number of independent trials (e.g., $M_{\rm trials}$) could prevent any momentary visual ambiguity with the cyclic clock dimension $M$ defined in Section 3.
