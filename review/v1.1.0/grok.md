# Grok review of v1.1.0

Automated manuscript review. [Editorial disposition](disposition.md)

## Release candidate

[Reviewed source](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/e6fcbe52c38c61717c87722895402173ec4fb1fe/manuscript.tex), SHA-256 `b7a2bde231a5a576eca8261de259ba04d46187b524dcd84698327d2237e72d18`.

**READY**

No mandatory correction. The spectrum, the factor \(p/2\), Clifford preservation of the Pauli norm, leakage, rounding, and both rational thresholds close under adversarial saturation of every stated inequality. Literature priority is not certified.

The cyclic clock is unitary, and \(A=(W+W^\dagger)/2\) is a Hermitian contraction. For \(Rv=\sigma v\) with \(\sigma=\pm1\), the mode \(M^{-1/2}\sum_a e^{-ia\theta}\lvert a\rangle U_a v\) is a \(W\)-eigenvector of phase \(e^{i\theta}\) if and only if \(e^{iM\theta}=\sigma\), hence an \(A\)-eigenvector of phase \(\cos\theta\). Thus \(\theta=0\) occurs only for \(\sigma=+1\). Every other eigenphase is at least \(\pi/M\) in absolute value. The chord bound \(\sin x\ge 2x/\pi\) on \([0,\pi/2]\) gives \(1-\cos(\pi/M)=2\sin^2(\pi/(2M))\ge 2/M^2\), so those eigenvalues are at most \(1-2/M^2\).

The idle state \(\psi=D^{-1/2}\sum_{a<D}\lvert a\rangle\lvert z\rangle\) sees \(U_a=I\). Its squared overlap with the eigenvalue-1 subspace is \((D/M)\langle z\rvert(I+R)/2\lvert z\rangle\). Here \(D=M/2\) and \((I+R)/2=C^\dagger\Pi C\), so the weight is exactly \(p/2\). Hadamards on the low \(\log_2 M-1\) clock bits send \(\lvert 0\rangle\lvert z\rangle\) to \(\psi\). Hadamard conjugation swaps \(X\) with \(Z\) and sends \(Y\) to \(-Y\), a signed permutation of Pauli strings, so \(\lambda(A')=\lambda(A)\).

Each clock edge has Pauli weight 1. Each allowed gate has weight at most 2, so \(\lambda(A)\le K=2M\). With \(s=d/K\le 1/16\), one has \(0<s\le 1/4\), \((1-2s)I\le B_*\le I\), and \(\lambda(B_*)\le 1-s+d\le c\). Eigenvalue 1 is fixed. Every other eigenvalue of \(B_*\) lies in \([1-2s,1-2s/M^2]\subset[0,1)\). The choice \(m=3M^2/s=6M^3/d\) is an integer for the hardwired dyadic \(d\), and
\[
(1-2s/M^2)^m\le e^{-6}<1/256.
\]
Hence \(p/2\le\langle j\rvert B_*^m\lvert j\rangle\le p/2+1/256\).

Rounding \((1-\tau)B_*\) toward zero on a grid of spacing at most \(\tau/(2S)\), with \(\tau\le 1/(256m)\), moves the operator by at most \(3\tau/2\). Telescoping two contractions yields \(\lVert B^m-B_*^m\rVert\le 3/512\). Also \(\lambda(B)\le c\), \(\lVert B\rVert\le 1-\tau/2\), and the least eigenvalue is at least \((1-\tau)(1-2s)-\tau/2>0\).

Compiled acceptance \(31/48\) or \(17/48\) (native \(2/3\) and \(1/3\) are safer) therefore gives
\[
v_{\mathrm{YES}}\ge\frac{31}{96}-\frac{3}{512}=\frac{487}{1536}>\frac{9}{32}=\frac{432}{1536},
\]
\[
v_{\mathrm{NO}}\le\frac{17}{96}+\frac{1}{256}+\frac{3}{512}=\frac{287}{1536}<\frac{7}{32}=\frac{336}{1536}.
\]
The slacks are \(55/1536\) and \(49/1536\). Against \(1/4=384/1536\) the slacks are \(103/1536\) and \(97/1536\). A closed error of \(1/32=48/1536\) leaves \(55/1536\) and \(49/1536\), so the estimate stays strictly above \(1/4\) on YES images and strictly below \(1/4\) on NO images. Endpoints of the promise need a stricter tolerance; \(1/64\) does decide them, as claimed. The cap-one sampler and the \(\varepsilon\) phase-estimation budget (\(17\varepsilon/64<\varepsilon/2\) before sampling) are consistent with the same bounds.
