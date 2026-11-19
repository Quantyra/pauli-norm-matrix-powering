# Grok manuscript review

Clock spectrum and finite precision. These are AI-generated reports. [Disposition and mathematical responses](disposition.md)

## Initial manuscript

[Reviewed source](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/430cb5841793a04a2d2add757e61d011f4475681/manuscript.tex), SHA-256 `8a6021f3adfabd84ffb318ef2c5f7e508ce452adea9d911a4d443e5e28ec724c`.

The cyclic-clock argument holds, including at the small-\(M\), \(c\downarrow 1\), and \(p\in\{1/3,2/3\}\) endpoints.

\(M=2^{\lceil\log_2\max(4,2t+1)\rceil}\) and \(R=C^\dagger(2\Pi-I)C\) with \(2\Pi-I=-Z_{\rm out}\). \(W\) is unitary, so \(A=(W+W^\dagger)/2\) is a Hermitian contraction on the whole space. For \(Rv=\sigma v\), the ring \(\{W^a\ket{0,v}\}\) is orthonormal, and the eigenvalues of \(A\) are \(\cos(2\pi k/M)\) or \(\cos((2k+1)\pi/M)\). Only \(\sigma=+1\), \(k=0\) gives \(+1\). Each mode overlaps \(\ket{0,v}\) in squared mass \(1/M\), and \(\bra z(I+R)/2\ket z=p\), so \(A\) has mass exactly \(p/M\) at \(+1\) on \(\ket j\). Every other eigenvalue is at most \(\cos(\pi/M)\). From \(1-\cos u=2\sin^2(u/2)\) and \(\sin x\ge 2x/\pi\) on \([0,\pi/2]\), this is at most \(1-2/M^2\).

Each clock edge has Pauli weight \(1\) and each gate weight at most \(2\), so \(\lambda(A)\le K=2M\). For fixed dyadic \(d\le\min(1/2,c-1)\), \(s=d/K\le 1/(4M)\) and \(B_*=(1-s)I+sA\) fixes \(+1\), stays in \([(1-2s)I,I]\), and has \(\lambda(B_*)\le 1-s+d\le c\). All other eigenvalues lie in \([0,1-2s/M^2]\). The choice \(m=(M^2/(2s))\lceil\log_2(64M)\rceil\) makes the tail at most \(e^{-\lceil\log_2(64M)\rceil}\le 1/(64M)\). Hence \(p/M\le\bra j B_*^m\ket j\le p/M+1/(64M)\).

With \(\tau\le 1/(128mM)\), directed rounding of \((1-\tau)B_*\) to spacing \(\tau/(2S)\) gives dyadic positive definite \(B\), \(\lambda(B)\le c\), and \(\lVert B\rVert\le 1-\tau/2\). Telescoping gives \(\lVert B^m-B_*^m\rVert\le\tfrac32 m\tau\le 3/(256M)\).

For acceptance \(p\ge 2/3-1/48\) versus \(p\le 1/3+1/48\), the scaled diagonal is at least \(487/768>7/12\) on YES and at most \(293/768<5/12\) on NO. With \(g=1/(2M)\) and \(\epsilon=1/(16M)\), these lie outside \([g-\epsilon,g+\epsilon]\) because \(7/12>9/16\) and \(5/12<7/16\). Accuracy \(1/(32M)\) decides. For \(c\le 1\), Pauli sampling is an unbiased \([-1,1]\) estimator, so \(O(\epsilon^{-2})\) samples put the problem in \(\mathsf{BPP}\). The slack \(d>0\) is necessary for this shift; the proof does not cover caps \(1+o(1)\).

The cap is the Pauli weight \(\sum|b_P|\). That is the constant-coefficient-weight question, and it is distinct from a constant induced matrix \(1\)-norm.

Optional: state that \(V_0,\ldots\) are \(G_1,\ldots,G_t\) in application order and that the full cycle, not one edge, contributes \(\sigma\); state that \(\epsilon/128\) is a per-trial trace-distance budget, since \(\epsilon/64+\epsilon/128<\epsilon/32\); \(d\le 1/2\) is spare because \(M\ge 4\) already forces \(s\le 1/(4M)\).

Verdict: READY

## Revised manuscript

[Reviewed source](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/988f17351b893e803dce674df7e304ec8f345fb4/manuscript.tex), SHA-256 `40fa75257749535764f800cc894bc1a05284393a94d758fcf8eea0aca351742c`.

The cyclic-clock argument holds at the small-\(M\), \(c\downarrow 1\), and \(p\in\{1/3,2/3\}\) endpoints, including compilation slack \(1/48\).

\(M=2^{\lceil\log_2\max(4,2t+1)\rceil}\) makes \(W\) unitary on the whole space, so \(A=(W+W^\dagger)/2\) is a Hermitian contraction. For \(Rv=\sigma v\) the ring \(\{W^a\ket{0,v}\}\) is orthonormal. Eigenvalues of \(A\) are \(\cos(2\pi k/M)\) or \(\cos((2k+1)\pi/M)\). Only \(\sigma=+1\), \(k=0\) yields \(+1\), with mass \(p/M\) on \(\ket j\). Every other eigenvalue is at most \(\cos(\pi/M)\le 1-2/M^2\).

Clock edges have Pauli weight \(1\) and gates at most \(2\), so \(\lambda(A)\le K=2M\). For fixed dyadic \(d\le\min(1/2,c-1)\), \(s=d/K\le 1/(4M)\) and \(B_*=(1-s)I+sA\) fixes \(+1\), obeys \(\lambda(B_*)\le c\), and places the rest of the spectrum in \([0,1-2s/M^2]\). Unary \(m=(M^2/(2s))\lceil\log_2(64M)\rceil\) makes the tail at most \(1/(64M)\).

Directed rounding of \((1-\tau)B_*\), with \(\tau\le 1/(128mM)\), produces a dyadic positive definite \(B\) with \(\lambda(B)\le c\) and \(\lVert B\rVert\le 1-\tau/2\). Telescoping gives \(\lVert B^m-B_*^m\rVert\le 3/(256M)\). Scaled diagonals are at least \(487/768>7/12\) on YES and at most \(293/768<5/12\) on NO, hence outside \([7/16,9/16]\). Accuracy \(1/(32M)\) decides. For \(c\le 1\) the \([-1,1]\) Pauli estimator is in \(\mathsf{BPP}\). The cap is \(\sum|b_P|\), distinct from the induced matrix \(1\)-norm. The \(m\log\lambda\) sampler stays polynomial only for shrinking caps.

Unary \(m,r\), fixed \(d\), rounding, spectral mixtures, median amplification, the commutator and sampling citations, identity slots, and zero ancillas are in place. No scientific blocker remains.

READY
