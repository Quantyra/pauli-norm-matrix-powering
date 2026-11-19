# Google Antigravity review of v1.1.0

Automated manuscript review. [Editorial disposition](disposition.md)

## Initial revision

[Reviewed source](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/26c85619d4f86329f6e5f1c5c5ff6854a3c30009/manuscript.tex), SHA-256 `7dd154a8f6793cb2b95200cb69a9ff773a1b82902defda3c1043cbaf92d0cf6c`.

### Verdict: READY

---

### Reasoned Findings

#### 1. Evaluation of Novelty, Attribution, and Prior Art
The manuscript resolves an open question posed by Cifuentes et al.~\cite[Sec.~IV\,A and Discussion]{cif} regarding whether Promise$\BQP$-completeness for matrix powering persists when the Pauli-coefficient 1-norm $\lambda(B) = \sum_P |b_P|$ is bounded by a fixed constant $c > 1$. The theoretical positioning is sound, accurate, and free of overclaims:
* **Relation to Cifuentes et al.~\cite{cif}:** Cifuentes et al.\ established constant-error $\BQP$-hardness for Chebyshev polynomials $T_m(A)$ and bounded computational-basis induced matrix 1-norms (column sums). For monomials $A^m$, their constant-error result (Appendix~A) requires evaluating a local measurement normalized by the squared output state norm $\bra\psi A^m M A^m \ket\psi / \norm{A^m \ket\psi}^2$. Theorem~\ref{thm:main} differs decisively by establishing hardness for an unnormalized single diagonal entry $\bra j B^m \ket j$ under a Pauli-basis norm cap $\lambda(B) \le c$.
* **Relation to Janzing–Wocjan~\cite{jw}:** Janzing and Wocjan showed Promise$\BQP$-completeness for sparse matrices with an inverse-polynomial precision requirement ($1/\mathrm{poly}$ gap). Theorem~\ref{thm:main} restricts the input to explicit Pauli linear combinations with a constant Pauli norm and achieves a constant gap ($v_{\rm YES} \ge 9/32$ vs.\ $v_{\rm NO} \le 7/32$), decidable with additive tolerance $1/32$.
* **Relation to Prior Pre-Idling~\cite{glg,cade}:** Pre-idling was introduced in Guided Local Hamiltonian reductions to concentrate ground-state weight on an idle history clock superposition. The author’s key innovation is setting the idle duration to exactly half of a power-of-two clock ($D = M/2$). This makes the clock superposition an unentangled tensor product $\ket 0_{\rm MSB} \otimes \ket{+}^{\otimes (\log_2 M - 1)}$, which is mapped to the single basis state $\ket 0 \ket z$ by transversal clock Hadamards $Q$. Because single-qubit Hadamards act by signed permutation on Pauli strings, $Q$ preserves the Pauli 1-norm ($\lambda(Q^\dagger A Q) = \lambda(A)$), translating a clock superposition into a computational basis diagonal entry without norm inflation.
* **Relation to Version 1.0~\cite{vone}:** The earlier version obtained an inverse-polynomial gap using a localized clock initialization $\ket 0 \ket z$ (yielding spectral weight $O(1/M)$). The conjugated pre-idling scheme boosts the distinguished spectral weight to $p/2$, enabling a constant promise gap.

#### 2. Technical Soundness & Mathematical Verification (Ranked by Severity)
* **Gap Preservation and Rounding (Sound):** The spectrum shift $B_* = (1-s)I + sA'$ with $s \le 1/4$ places all non-unit eigenvalues in $[1-2s, 1-2s/M^2] \subset [0, 1-2s/M^2]$, eliminating sign oscillations under powering. The directed dyadic rounding toward zero rigorously ensures $\lambda(B) \le c$, $\norm{B} < 1$, and positive definiteness ($\lambda_{\min}(B) > 0$). The telescoping bound $m\norm{B - B_*} \le \frac{3}{512}$ rigorously preserves the separation ($v_{\rm YES} \ge 487/1536 > 9/32$ and $v_{\rm NO} \le 287/1536 < 7/32$).
* **Phase Estimation Presentation (Low Severity / Presentation):** Section~2 describes taking the median across fresh phase registers within a trial on the same system register conditional on an eigenvector. While statistically valid across the eigenmixture, standard phase estimation using $O(\log(m/\epsilon))$ ancilla bits in a single execution directly suppresses the failure probability below $\epsilon/64$ without invoking sequential register arguments. Noting this would enhance readability.
* **Clock Transition Expansion (Low Severity / Readability):** In Section~4, the statement that each transition has $M$ Pauli terms of total weight one is correct, but explicitly stating that the computational projector $\ket{a+1 \bmod M}\bra a$ factors into $\log_2 M$ single-qubit rank-1 units $\ket{x_k}\bra{y_k}$ (each having 2 Pauli terms of weight $1/2$) would make the bound $\lambda(A) \le 2M$ immediately transparent.

## Release candidate

[Reviewed source](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/e6fcbe52c38c61717c87722895402173ec4fb1fe/manuscript.tex), SHA-256 `b7a2bde231a5a576eca8261de259ba04d46187b524dcd84698327d2237e72d18`.

### Verdict: READY

---

### Reasoned Findings

#### 1. Evaluation of Novelty, Attribution, and Prior Art
The manuscript resolves the open question posed by Cifuentes et al.~\cite[Sec.~IV\,A and Discussion]{cif} regarding whether Promise$\BQP$-completeness for matrix powering persists under a constant Pauli-coefficient 1-norm cap $\lambda(B) = \sum_P |b_P| \le c$ for any fixed $c > 1$. The theoretical positioning is accurate, rigorous, and free of overclaims:
* **Relation to Cifuentes et al.~\cite{cif}:** Cifuentes et al.\ established constant-error $\BQP$-hardness for Chebyshev polynomials $T_m(A)$ and bounded computational-basis induced 1-norms (column sums). For monomials $A^m$, their constant-error result (Appendix~A) requires evaluating a local measurement normalized by the powered state norm, $\bra\psi A^m M A^m \ket\psi / \norm{A^m \ket\psi}^2$. Theorem~\ref{thm:main} differs decisively by establishing hardness for an *unnormalized single diagonal entry* $\bra j B^m \ket j$ of the monomial under a Pauli-basis norm cap $\lambda(B) \le c$.
* **Relation to Janzing–Wocjan~\cite{jw}:** Janzing and Wocjan established Promise$\BQP$-completeness for powering sparse matrices with an inverse-polynomial precision requirement ($1/\mathrm{poly}$ gap). Theorem~\ref{thm:main} restricts the input to an explicit linear combination of Pauli strings with a constant Pauli 1-norm and achieves a constant promise gap ($v_{\rm YES} \ge 9/32$ vs.\ $v_{\rm NO} \le 7/32$), decidable within additive tolerance $1/32$.
* **Relation to Prior Pre-Idling~\cite{glg,cade}:** Pre-idling was originally introduced in Guided Local Hamiltonian complexity to concentrate ground-state weight on an idle clock history. The author adapts this to matrix powering by setting the idle duration to exactly half of a power-of-two clock ($D = M/2$). This makes the clock superposition an unentangled tensor product $\ket 0_{\rm MSB} \otimes \ket{+}^{\otimes (\log_2 M - 1)}$, which is mapped to the single computational basis state $\ket 0 \ket z$ via transversal clock Hadamards $Q$. Because single-qubit Hadamards act by signed permutations on Pauli strings, $Q$ preserves the Pauli 1-norm ($\lambda(Q^\dagger A Q) = \lambda(A)$), translating a clock superposition into a computational basis diagonal entry without norm inflation.
* **Relation to Version 1.0~\cite{vone}:** The earlier version obtained an inverse-polynomial gap using a localized clock initialization $\ket 0 \ket z$ (yielding spectral weight $O(1/M)$). The conjugated pre-idling scheme boosts the distinguished spectral weight to $p/2$, enabling a constant promise gap.

#### 2. Technical Soundness & Mathematical Verification (Ranked by Severity)
* **Gap Preservation, Rounding, and Spectrum (Sound):** The spectrum shift $B_* = (1-s)I + sA'$ with $s = d/(2M) \le 1/16$ maps all non-unit eigenvalues into $[1-2s, 1-2s/M^2] \subset (0, 1)$, eliminating sign oscillations under powering. Dyadic rounding toward zero with grid spacing $\le \tau/(2S)$ strictly guarantees $\lambda(B) \le c$, $\norm{B} < 1$, and positive definiteness ($\lambda_{\min}(B) > 0$). The telescoping bound $m\norm{B - B_*} \le \frac{3}{512}$ rigorously preserves the separation ($v_{\rm YES} \ge 487/1536 > 9/32$ and $v_{\rm NO} \le 287/1536 < 7/32$).
* **Completeness and Soundness Bounds (Sound):** Compiling to operator error $1/96$ up to phase shifts acceptance by at most $1/48$, mapping native circuit bounds $\{2/3, 1/3\}$ to $\{31/48, 17/48\}$. Accounting for non-unit eigenvalue leakage ($e^{-6} < 1/256$) and rounding error ($\pm 3/512$), the promise thresholds $9/32$ and $7/32$ are rigorously satisfied with positive slack.

#### 3. Assessment of Previous Objections and Journal Readability
The revised manuscript successfully incorporates prior presentation suggestions:
* Section~4 now explicitly details the binary factorization of clock transition projectors into $\log_2 M$ single-qubit rank-1 units $\ket{x_k}\bra{y_k}$ (each having 2 Pauli terms of weight $1/2$), making the bound $\lambda(A) \le 2M$ immediate and transparent.
* Section~2 clearly specifies the phase estimation register conditioning and error budgeting for the upper bound.

No technical or presentation gaps remain. The manuscript is complete, self-contained, and ready for publication.
