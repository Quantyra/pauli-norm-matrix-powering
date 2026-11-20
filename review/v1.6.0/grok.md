# Grok review of v1.6.0

Automated manuscript review. [Editorial disposition](disposition.md)

## Release candidate

[Reviewed manuscript](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/1eeddebcc7e0306ed109593a3980c2d8c999ee24/manuscript.tex), SHA-256 17461fd7e2d54c45475c357b89b47957ea88514ae659db3280f7e742f9e48dc2.

I'll review the manuscript as given, focusing on Corollary 3.1, Appendix D, and the cap-only hardness remark, and I'll derive the sampling identities independently before assigning a verdict.**READY.** The manuscript at SHA-256 `17461fd7e2d54c45475c357b89b47957ea88514ae659db3280f7e742f9e48dc2` matches the supplied text. Corollary 3.1, Appendix D, and the cap-only hardness remark are correct, including the endpoint cases \(\beta_*=0\) and states with proper support. No mandatory fix.

## Corollary 3.1 and Appendix D

The 2-approximate cover is valid, and moving every diagonal Pauli into \(D\) only decreases the off-diagonal weight, so \(\beta\le 2\beta_*\). The hypothesis \(\beta_*\le 1/4\) gives \(w=1+\beta\le 3/2\). The monomial walk below is unbiased, \(|Z_k|\le 1\), and the Chebyshev filter of Theorem 2 therefore transfers. On a success event of probability at least \(3/4\), the additive error is at most \(3/128<1/32\).

### Unbiased score

Let \(|\psi\rangle=U|j\rangle\) and \(A=UBU^\dagger=D+\sum r_PP\), with \(D\) every diagonal term. For \(x\) in the support of \(\psi\) and \(y=x\oplus v\),

\[
\rho(x,y)=\frac{\overline{\psi(y)}}{\overline{\psi(x)}},\qquad |\psi(x)|^2\rho(x,y)=\overline{\psi(y)}\,\psi(x).
\]

Hence \(\langle\psi|M|\psi\rangle=\mathbb E_{x\sim|\psi|^2}\sum_y M_{yx}\rho(x,y)\). Sample \(D\) with probability \(1/w\) and \(P\) with probability \(|r_P|/w\). The accumulated scalar \(a(x)\) is the product of the current diagonal entries \(d(x_t)\) and of \(\mathrm{sign}(r_P)\) times the Pauli basis phase. Each sequence of choices has probability \(w^{-k}\) times the product of the \(|r_P|\) along Pauli steps, while the operator matrix element carries those factors inside, so

\[
w^k\mathbb E[a\rho]=\langle\psi|A^k|\psi\rangle=\bra j B^k\ket j.
\]

The right-hand side is real, so the same identity holds for \(Z_k=\operatorname{Re}(a\rho)\).

**Zero support.** Stabilizer support is a single nonempty affine coset of the flip space \(V\). Off-support inputs are not sampled and contribute nothing to the quadratic form. If the walk ends off that coset, \(v\notin V\), the algorithm sets \(\rho=0\), and both sides of the amplitude identity vanish. Intermediates outside the support are allowed: only the endpoints enter \(\rho\).

**\(\beta=0\).** Then \(w=1\), \(A=D\), and the only stabilizer lift of \(v=0\) is the identity, so \(\rho(x,x)=1\). The score is the real number \(d(x)^m\), and \(\mathbb E d(x)^m=\bra j B^m\ket j\). The separate choice \(f(x)=x^m\), \(W=1\), is the right specialization of the filter.

### Bounded conjugate endpoint ratio

On the support, \(|\psi|\) is constant. A Hermitian stabilizer lift \(\gamma X^v Z^p\), with the action \((\gamma X^v Z^p)|x\rangle=\gamma(-1)^{p\cdot x}|x\oplus v\rangle\), fixes \(|\psi\rangle\) and satisfies \(\gamma^2=(-1)^{p\cdot v}\). Therefore

\[
\rho(x,y)=\overline{\gamma}\,(-1)^{p\cdot x}\in\{\pm1,\pm i\}
\]

when \(v\in V\), and \(\rho=0\) otherwise. In particular \(|\rho|\le 1\). Checked on \(SH|0\rangle\): \(Y=iXZ\), \(\gamma=i\), \(v=p=1\), and \(\overline{\psi(1)}/\overline{\psi(0)}=-i=\overline{\gamma}\).

### Signed product

Each \(D\)-step multiplies by the real diagonal entry. Each Pauli step multiplies by a sign and a fourth root coming from \(I,X,Y,Z\) on the current basis word. Thus \(a\) is a real dyadic times a fourth root, \(|a|\le 1\) because \(|d(x)|\le 1\) by contraction, and \(|Z_k|\le 1\).

### Exact dyadic bit cost

If every input coefficient has denominator dividing \(2^F\), Clifford signs preserve that denominator and \(d(x)\in 2^{-F}\mathbb Z\). A product of at most \(m\) such factors has denominator \(2^{mF}\). Multiplication by a fourth root and extraction of the real part stay in \(2^{-mF}\mathbb Z\), including the score \(0\). The streamed sum of \(M\) signed scores, signs of the \(a_k\) included, has denominator \(2^{mF}\) and numerator length \(mF+\lceil\log_2 M\rceil+O(1)\). With \(W\le 2\cdot 5^D\), \(D\le\lceil\sqrt{12q}\rceil\) and \(q\le 2m\ln w/\ln 2\), one has \(\log_2 M=O(\sqrt{1+m\ln w})\). For \(w\le 1+2\beta_*\) and \(\beta_*\le 1/4\), with \(m,F\le L\), that length is polynomial, which is the space claim.

### Capped failure budget

Binary rejection accepts with probability at least \(1/2\). With

\[
R=\lceil\log_2(12M(m+1))\rceil+1
\]

and at most \(M(m+1)\) categorical draws, the union bound on exhaustion is at most \(1/24\), hence at most the stated \(1/12\). Chebyshev with \(M=\lceil 6\cdot 64^2 W^2\rceil\) contributes at most \(1/6\). On the coupled event that no draw aborts, the scores equal the ideal scores. That event and the Chebyshev event together have probability at least \(3/4\). Filter bias at most \(1/128\) plus sampling error at most \(1/64\) gives total error at most \(3/128\). Exhaustion is scored as zero and is charged to the failure budget, not to the error on the success event. The same arithmetic covers \(\beta=0\), where the only categorical masses are trivial.

The two-local family also checks: \(\sum p_i=1\), \(\lambda(B)=5/4\), \(\beta_*=3\alpha\eta/4\), \(m\beta_*=3\ell^2/8\), deletion drops the diagonal from at least \(1/2\) to at most \(e^{-\alpha\ell^2/4}\), and the symmetric nonnegative comparison gives variance \(\exp(\Omega(m))\) for both row samplers.

## Cap-only hardness

For \(c=5/4\) and \(d=1/4\), \(s=d/K\) and \(m=6M^3/d=24M^3\). The identity coefficient of \(A\) is zero because the clock shift is traceless, and Hadamard conjugation preserves it. After the factor \(1-\tau\) and inward rounding, the nonidentity mass is at most \((1-\tau)s\lambda(A')\le d=1/4\), and what remains is a positive scalar multiple of \(I\). Thus \(\beta_*\le 1/4\) on the same images that already satisfy the strict bounds \(487/1536>9/32\) and \(287/1536<7/32\). For membership, \(\lVert B\rVert\le 1\) gives \(|b_P|=2^{-n}|\operatorname{Tr}(PB)|\le 1\), so \(\lambda(B)\) is at most the number of listed terms and the Section 2 estimator is polynomial at error \(1/64\). These images have \(m\beta_*=\Theta(M^3)\), outside the polynomial range of Corollary 3.1, so there is no collapse.

## Rest of the manuscript

The cyclic gap \(\cos(\pi/M)\le 1-2/M^2\), the idle-half weight \(p/2\), the tail \(e^{-6}\), the rounding telescope \(m\cdot(3\tau/2)\le 3/512\), and the compiled thresholds \(31/48\) and \(17/48\) all match the displayed fractions. Theorem 2’s filter, Markov converse, and \(13/512\) budget are consistent: clipping onto \([-1,1]\) does not increase distance to a value in that interval, and rounding to a multiple of \(1/256\) adds at most \(1/512\). The chain weight \(p/2\), the visible gap \(1/(6T^2)\), \(m\ln\lambda(B)=\Theta(NT^2)\), the two-step Rayleigh lower bound with \(\gamma=[3(\sqrt2-1)-1]/\ell\), and the total-variation bound \(M\ge 2^q/3\) were rederived. For the first confidence width, \(n=42\) gives \(m=36424602825523200\).

## Optional observations

These do not affect the claims. The attempt cap is one larger than a sharp \(1/12\) union bound; the proof’s \(1/12\) still holds. Corollary 3.1 states \(1/32\) where the proof gives \(3/128\). The phrase “scalar identity” means a scalar multiple of \(I\), here \((1-\tau)(1-s)\) after inward rounding. In the two-step witness, \(XH=e^{-i(\pi/4)Y}\) and eight pairs return the target to \(|0\rangle\); acceptance zero is what the argument uses. The exponent constants \(5\) and \(1/3\) are not optimized.
