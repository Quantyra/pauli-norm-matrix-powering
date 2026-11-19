# Grok review of v1.3.0

Automated manuscript review. [Editorial disposition](disposition.md)

## Initial revision

[Reviewed source](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/71399c1702bca8920be642bac58dc2c49711c726/manuscript.tex), SHA-256 `c8d0b936d6d66428fa6eee1f3717cae6abba0978b5cc486610ddaf52a442f976`.

**READY.** Mandatory corrections: none. The checked source matches SHA-256 `c8d0b936d6d66428fa6eee1f3717cae6abba0978b5cc486610ddaf52a442f976`.

Theorem 3 holds in both directions for every degree. For the algorithm, the largest \(b\) with \(\lambda^b\le 2\) gives \(q\le 2A/\ln 2\). The Chebyshev tail uses \(D=\min(q,\lceil\sqrt{12q}\rceil)\). Hoeffding supplies an omitted mass of at most \(2e^{-6}<1/128\), and \(|T_k|\le 1\) on \([-1,1]\), so \(f(x)=x^r p(x^b)\) is within \(1/128\) of \(x^m\) there. The recurrence gives \(W_2(T_{k+1})\le 4W_2(T_k)+W_2(T_{k-1})\), and \(4\cdot 5^k+5^{k-1}\le 5^{k+1}\). With \(\lambda^r\le 2\), one gets \(W\le 2\cdot 5^D\). Chebyshev’s inequality at \(M=\lceil 6\cdot 64^2 W^2\rceil\) leaves failure at most \(1/6\); the stated rejection cap adds at most \(1/12\). Clipping, the \(1/128\) function error, and rounding to \(1/256\) total at most \(13/512<1/32\), with success probability at least \(3/4\). The running time is \(\mathrm{poly}(L)\exp(O(\sqrt{1+A}))\), hence polynomial for \(A=O(\log^2 L)\).

For the coefficient lower bound, \(h=\lambda-1\le 1/2\) places \(I=[1-h/2,1]\) inside \([0,1]\). The triangle inequality gives \(\sum |d_j|h^j\le W_\lambda(f)\). Truncation at \(\ell=\lceil\log_2(128W)\rceil\) costs at most \(2^{-(\ell+1)}W\le 1/256\le 1/128\) on the whole of \(I\), including the left endpoint. Thus \(g\) is within \(5/128\) of \(x^m\) and \(\|g\|_{\infty,I}\le 17/16\). Since \(m(\lambda-1)\ge A\ge 2\), the point \(1-1/m\) lies in \(I\), and \((1-1/m)^m<e^{-1}\) makes \(g\) rise by more than \(1/2\). The mean value theorem and the scaled Markov bound \(\|g'\|\le (4/h)\ell^2\|g\|\) give \(\ell^2\ge 2mh/17\). The inequality \(18(\lambda-1)\ge 17\ln\lambda\) on \((1,3/2]\) yields \(\ell^2\ge A/9\), while \(\ell\le\log_2 W+8\). Therefore \(W_\lambda(f)\ge 2^{\sqrt A/3-8}\). If \(\deg f<\ell\), Markov’s upper bound with degree \(\ell\) remains valid.

Corollary 4 also checks. For \(N\ge 26\), \(\|H\|\ge\lfloor N/2\rfloor/2\) and \(\mu\le 7(N-1)/64+3/16\) give \(\lambda(B_*)\ge 1+sN/64\). Scaling and inward rounding remove at most \(2\tau\le sN/128\), so \(1+sN/128\le\lambda(B)\le 5/4\). With \(ms=36T^2\) and \((\lambda-1)/\lambda\le\ln\lambda\le\lambda-1\), one gets \(\tfrac{3}{16}NT^2\le m\ln\lambda(B)\le 36KT^2\). The filter from Theorem 3 then has trial count \(\exp(\Theta(T\sqrt N))\).

Optional polish: restate in Theorem 3 that \(B\) is a Hermitian contraction, since the tail, clipping, and spectral step use spectrum in \([-1,1]\). The constants \(5^D\), \(17/16\), \(A/9\), and \(+8\) are valid with slack. Corollary 4 can name the hypothesis \(N\ge 26\).

## Release candidate

[Reviewed source](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/8708b50322448cb437c4764fa2c2260baffdbedc/manuscript.tex), SHA-256 `06fa0bb5acd7fcf55c99a9442009147e3e00bde2888a92a309cdaf90fab7b05e`.

**READY.** Mandatory corrections: none.

The block split is valid for every \(m\). The largest \(b\le m\) with \(\lambda^b\le 2\) gives \(q=1\) when \(b=m\). Otherwise \(b>(\ln 2)/(2\ln\lambda)\), so \(q\le m/b<2A/\ln 2\). The identity \(y^q=\mathbb E\,T_{|S_q|}(y)\) is exact. For \(D=\min(q,\lceil\sqrt{12q}\rceil)\), the omitted mass is \(0\) or at most \(2e^{-D^2/(2q)}\le 2e^{-6}<1/128\). With \(|T_k|\le 1\) on \([-1,1]\), \(f(x)=x^r p(x^b)\) lies within \(1/128\) of \(x^m\) there, and the spectral theorem carries this to the diagonal.

The recurrence yields \(W_2(T_{k+1})\le 4W_2(T_k)+W_2(T_{k-1})\), and \(4\cdot 5^k+5^{k-1}=21\cdot 5^{k-1}\le 5^{k+1}\). With the bases \(T_0,T_1\), one gets \(W_2(T_k)\le 5^k\). Since \(\lambda^b\le 2\) and \(\lambda^r\le 2\), \(W_\lambda(f)\le 2\cdot 5^D\). At \(M=\lceil 6\cdot 64^2 W^2\rceil\), Chebyshev leaves failure at most \(1/6\); the rejection cap adds at most \(1/12\). Projection onto \([-1,1]\) does not increase distance to \(v\), and
\[
1/64+1/128+1/512=13/512<1/32,
\]
with success probability at least \(3/4\). The bit cost is \(\mathrm{poly}(L)\exp(O(\sqrt{1+A}))\), hence polynomial for \(A=O(\log^2 L)\). An estimate this close to \(v\), compared with \(1/4\), separates \(9/32\) from \(7/32\).

For the converse, \(h=\lambda-1\le 1/2\) puts \(I=[1-h/2,1]\) inside \([0,1]\), and \(\sum|d_j|h^j\le W\). Truncation at \(\ell=\lceil\log_2(128W)\rceil\) costs at most \(2^{-(\ell+1)}W\le 1/256\le 1/128\) on all of \(I\), including the left endpoint. Thus \(g\) is within \(5/128\) of \(x^m\) and \(\|g\|_{\infty,I}\le 17/16\). Since \(mh\ge A\ge 2\), one has \(1-1/m\in I\). The rise of \(x^m\) exceeds \(1-e^{-1}\), and \(1-e^{-1}-5/64>1/2\), so \(g\) rises by more than \(1/2\). The scaled Markov bound \(\|g'\|\le(4/h)\ell^2\|g\|\) gives \(\ell^2\ge 2mh/17\). From \(mh\ge A\) and \(2/17\ge 1/9\), \(\ell^2\ge A/9\), while \(\ell\le\log_2 W+8\). Therefore \(W_\lambda(f)\ge 2^{\sqrt A/3-8}\). If \(\deg f<\ell\), then \(\deg g\le\ell\), so the same Markov factor applies.

Corollary 4 also checks. For \(N\ge 26\), \(\|H\|\ge\lfloor N/2\rfloor/2\) and \(\mu\le 7(N-1)/64+3/16\) give \(\lambda(B_*)=1+s(\lambda(H)-2\mu)\ge 1+sN/64\). Inward rounding removes at most \(2\tau\le sN/128\), so \(1+sN/128\le\lambda(B)\le 5/4\). With \(ms=36T^2\) and \((\lambda-1)/\lambda\le\ln\lambda\le\lambda-1\),
\[
\tfrac{3}{16}NT^2\le m\ln\lambda(B)\le 36KT^2.
\]
The filter from the sampling theorem then has trial count \(\exp(\Theta(T\sqrt N))\).

Optional polish: display \(1-e^{-1}-5/64>1/2\), \(2/17\ge 1/9\), and the sum \(13/512\) in the proof. The factors \(5^D\), \(17/16\), \(A/9\), and \(+8\) are valid with slack. Hermiticity of \(B\) and the hypothesis \(N\ge 26\) are already stated.
