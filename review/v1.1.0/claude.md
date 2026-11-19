# Claude review of v1.1.0

Automated manuscript review. [Editorial disposition](disposition.md)

## Initial revision

[Reviewed source](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/26c85619d4f86329f6e5f1c5c5ff6854a3c30009/manuscript.tex), SHA-256 `7dd154a8f6793cb2b95200cb69a9ff773a1b82902defda3c1043cbaf92d0cf6c`.

# Referee Report

**Verdict: REVISE** (minor, but two corrections are mandatory)

## Verified independently

I re-derived the load-bearing quantitative claims and they hold.

- **Clock spectrum.** $W$ is unitary (each clock label has a unique predecessor/successor); the Fourier modes $M^{-1/2}\sum_a e^{-ia\theta}\ket a U_a v$ satisfy $e^{iM\theta}=\sigma$ and give $A$-eigenvalue $\cos\theta$. Only $\sigma=+1$ admits $\theta=0$; the next-largest is $\cos(\pi/M)\le 1-2/M^2$ via the chord bound. $U_M=C^\dagger(2\Pi-I)C$ with the stated gate order, and $D+2t+1\le M$ holds since $M\ge 2(2t+1)$.
- **Pre-idling weight.** $U_a=I$ for $a\le D$, overlap $\sqrt{D/M}\langle v|z\rangle$, and $\sum_i|\langle v_i|z\rangle|^2=\bra z\frac{I+R}{2}\ket z=p$, giving exactly $p/2$. Clock Hadamards on the low $\log_2M-1$ bits do map $\ket0\ket z\mapsto\psi$ (MSB $=0$ iff $a<D$), and $H$-conjugation is a signed Pauli permutation, so $\lambda(A')=\lambda(A)$ and the term count is unchanged.
- **Norms.** $\lambda(\ket{a{+}1}\bra a)=1$ ($M$ terms of weight $1/M$), $\lambda(V_a)\le 2$ ($\lambda(H)=\sqrt2$, $\lambda(T)=\cos\frac\pi8+\sin\frac\pi8\approx1.31$, $\lambda(\mathrm{CNOT})=2$), multiplicativity on disjoint registers and subadditivity give $\lambda(A)\le 2M=K$; $\lambda(B_*)\le 1-s+d\le c-s<c$; $\|A\|\le1$ as a Hermitian part of a unitary.
- **Constants.** $s\le1/16$; $m=6M^3/d$ is an integer; $(1-2s/M^2)^m\le e^{-6}<1/256$; $\tau\le1/(256m)$; rounding error $S\cdot\tau/(2S)=\tau/2$, so $\|B-B_*\|\le\frac32\tau$ and $\|B^m-B_*^m\|\le\frac3{512}$ by telescoping two contractions; $\lambda_{\min}(B)>0$ and $\|B\|\le1-\tau/2$. Endpoints: $487/1536>432/1536=9/32$ and $287/1536<336/1536=7/32$, so the $1/32$ tolerance against $1/4$ is strict **on the images**, and $1/64$ decides every promised input including $v=9/32,7/32$ exactly (an additive-$1/32$ estimator does *not* decide the endpoints — the manuscript is correctly worded, but this asymmetry deserves one explicit sentence).
- **QPE budget.** Coherent: Lipschitz bias $m\cdot\epsilon/(8m)=\epsilon/8$; failure bias $2\cdot\epsilon/32=\epsilon/16$; plus $\epsilon/16$ rounding $\Rightarrow$ bias $\le\epsilon/4$; Hoeffding on range $2$ needs $\approx6.4\epsilon^{-2}$ trials for $3\epsilon/4$ at confidence $2/3$. The $\epsilon/128$ simulation/synthesis allowance contributes TV $\le\epsilon/64$, which with ideal failure $\epsilon/64$ meets the $\epsilon/32$ allowance. No aliasing: $\|B\|\le1$ puts eigenphases in $[-1,1]\subset(-\pi,\pi)$ — worth stating. Trotter: $\sum_{a<b}\|[b_aP_a,b_bP_b]\|\le\lambda^2-\sum_a b_a^2\le\lambda^2$; with $u\le O(m/\epsilon)$ the slice count is polynomial because $m$ is unary.

## Mandatory corrections

1. **"The power may equivalently be binary under a specified polynomial resource bound."** As written this is unsupported and, read literally, false: with $m$ binary and unbounded, the containment proof collapses (QPE precision $\Theta(\epsilon/m)$ and simulation time $\Theta((m/\epsilon)^2)$ are exponential in $\log m$), and no PromiseBQP upper bound is given. Either delete the sentence or state the encoding precisely (e.g. $m$ in binary with an explicit $m\le L$ or an accompanying unary bound).
2. **"the variable-precision problem that admits these fixed parameters" is never defined.** Define it (input $\epsilon$ in unary, thresholds $1/4\pm\epsilon$, promises $\|B\|\le1,\lambda(B)\le c$) before claiming hardness transfers.

## Secondary

3. **Uniformity in $c$.** Hardness is per fixed $c$ with $d$ hardwired; say so in the theorem and note the available strengthening: since $m=6M^3/d$ is emitted in unary, the reduction stays polynomial whenever $c-1\ge1/\mathrm{poly}(L)$, so a uniform statement for inverse-polynomially small caps is free. Nothing is claimed for $c-1=2^{-\Omega(L)}$.
4. **Redundancy.** $\|B\|\le\lambda(B)$, so for $c\le1$ the operator-norm promise is vacuous; stating this sharpens the dichotomy.
5. **Rejection sampling** for $\lambda>1$ introduces a failure probability not folded into any error budget; note it is unused by Theorem 1(i).
6. **Encoding conventions** (common label length $n$, $j\in\{0,1\}^n$, relation of $L$ to $n$, $m$, term count) should be fixed in §1, since the later $M$-idle-qubit padding remark is sensitive to exactly this.
7. **Directed rounding in $\mathbb Z[1/2]+\sqrt2\,\mathbb Z[1/2]$**: give the one-line algorithm (binary search plus sign-by-squaring) rather than asserting it.

I do not certify priority or the attribution of the open question to [cif]/[vone]; the AI-assistance acknowledgment is an editorial matter.

## Release candidate

[Reviewed source](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/e6fcbe52c38c61717c87722895402173ec4fb1fe/manuscript.tex), SHA-256 `b7a2bde231a5a576eca8261de259ba04d46187b524dcd84698327d2237e72d18`.

# Referee Report (second round)

**Verdict: READY.** No mandatory correction remains. Both prior blocking items are fixed; the remaining notes are optional polish.

## Prior objections — disposition

1. **Binary power (was mandatory).** The vague "equivalently binary under a polynomial resource bound" is gone, replaced by a precise alternative encoding: $m$ in binary together with a unary bound $1^u$, $m\le u$. This is correct and the interconvertibility claim holds ($m$ unary $\leftrightarrow$ $(m,1^m)$), and containment survives because QPE evolution time $O(m/\epsilon)\le O(u/\epsilon)$ stays polynomial in $L$. **Resolved.**
2. **Variable-precision problem (was mandatory).** Now defined: input additionally carries rational $g$ and unary $r$, thresholds $g\pm1/r$; $g=1/4$, $r=32$ reproduces the reduction. Only hardness is claimed, which is the accurate claim (containment would need $r$ unary, as §2's $\mathrm{poly}(m/\epsilon)$ budget indeed gives). **Resolved.**
3. **Uniformity in $c$.** Theorem now says "with the cap external to the input" and §4 states $d$ is hardwired per $c$. **Resolved** (the inverse-polynomial strengthening remains unclaimed, which is fine).
4–7. $\|B\|\le\lambda(B)$ redundancy stated; rejection sampling now carries an explicit $L^2$ retry cap with $2^{-L^2}$ failure and is flagged as separate from the cap-one sampler, plus the useful caveat that a length-dependent cap needs separate analysis ($m\log\lambda=O(\log L)$ is the right condition); encoding conventions ($n$, $j\in\{0,1\}^n$, duplicate collection, $L$ including the unary power) fixed in §1; the directed-rounding algorithm in $\mathbb Z[1/2]+\sqrt2\,\mathbb Z[1/2]$ is now given (grid $2^{-\lceil\log_2(2S/\tau)\rceil}$, binary search, sign of $a+b\sqrt2$ by comparing $a^2$ with $2b^2$). The endpoint asymmetry is stated explicitly ("accuracy $1/64$ decides every promised input"; at an endpoint an error of exactly $1/32$ may return $1/4$), and the no-aliasing remark ("eigenphases in $[-1,1]$, away from the branch cut") is present. **All resolved.**

## Re-verified this round

Clock unitarity and the $\sigma$-twisted Fourier modes; the wrap phase $\sigma e^{-i(M-1)\theta}=e^{i\theta}$; $\cos(\pi/M)\le1-2/M^2$; $U_M=C^\dagger(2\Pi-I)C$ with $2\Pi-I=-Z_{\rm out}$ and $D+2t+1\le M$; pre-idling weight exactly $p/2$ via $(I+R)/2=C^\dagger\Pi C$; $Q\ket{0}\ket z=\psi$ (MSB $=0$ iff $a<D$) and $\lambda(A')=\lambda(A)$ under signed Pauli permutation. Norms: $M$ clock terms of weight $1/M$, $\lambda(T)=\cos\frac\pi8+\sin\frac\pi8<2$, $\lambda(A)\le2M=K$, $S=O(M^2)$. Constants: $m=6M^3/d\in\mathbb Z$, $(1-2s/M^2)^m\le e^{-6}<1/256$, $\tau\le1/(256m)$, $\|B-B_*\|\le\frac32\tau$, $\|B^m-B_*^m\|\le3/512$, $\lambda_{\min}(B)\ge(1-\tau)(1-2s)-\tau/2>0$, $\|B\|\le1-\tau/2$, $\lambda(B)\le(1-\tau)\lambda(B_*)\le c$. Endpoints: $487/1536>432/1536$ and $287/1536<336/1536$, margins $55/1536$ and $49/1536$ both exceeding $48/1536=1/32$, so the $1/32$-on-images claim is strict. Compiling: $t_0\cdot1/(96t_0)=1/96$ operator error, acceptance shift $\le2/96=1/48$, giving $31/48$ / $17/48$. QPE: bias $\epsilon/8+\epsilon/16+\epsilon/16=\epsilon/4$, plus $\epsilon/64$ from the $\epsilon/128$ simulation allowance, under $\epsilon/2$; Trotter $\sum_{a<b}2|b_a||b_b|\le\lambda^2$. The $M$-idle-qubit padding makes $m=O(n^3)$ for qubit-counted conventions without touching $\lambda$, $\|\cdot\|$, or the diagonal.

## Optional polish (non-blocking)

- §1 defines $\lambda$ only for Hermitian operators, but §4 applies it to $W$, $T$, and clock matrix units; one clause extending it to complex Pauli coefficients would close the gap formally.
- "A classical polynomial-time estimator of additive error $1/32$" should name a success probability (e.g. $\ge2/3$) to make the $\BPP=\BQP$ implication airtight; "at any fixed $c>1$" would read better as "at some fixed $c>1$".
- The padding remark could say $j$ is extended by zeros.

I do not certify literature priority or the attribution of the open question to [cif]/[vone]; the AI-assistance acknowledgment is editorial.
