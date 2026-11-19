# Grok review of v1.4.0

Automated manuscript review. [Editorial disposition](disposition.md)

## Initial scientific review

[Exact manuscript](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/73f03401988af404a20146758c8693e9a914a0e4/manuscript.tex), SHA-256 a52babde3c4f08fe017e7cc0e91cccbe180c144f3e9704e295226cc6b915b337.

**Verdict: REVISE**

The new Appendix B is mathematically sound through Theorem 5. Both variance lower bounds hold, and no pre-existing error in the decision reduction, the sampler, or the chain affects this release. One claim after Theorem 5 does not follow from the argument given and should be corrected before release.

## Audit of Appendix B

**Diagonal-word bound.** The alternating basis word meets disjoint rule-3 projectors, so its energy lower-bounds \(d_Z(H)\). The same identity-coefficient algebra as in the chain-cost corollary gives \(d_Z(B)\ge 1+sN/128\) and \(m\ln d_Z(B)=\Theta(NT^2)\) for \(N\ge 26\). For the Pauli sampler of a real filter within \(1/32\) of \(x^m\) on \([0,1]\), every all-\(I,Z\) word scores with absolute value \(W\), the \(\lambda\)-weights cancel, and
\[
\mathbb E|Y|\ge\sum_k|a_k|d_Z(B)^k.
\]
Positive-definiteness and the contraction put the spectrum in \((0,1]\), so \(|\mathbb EY|\le 33/32\). Thus \(\operatorname{Var} Y\ge W_{d_Z}(f)^2-(33/32)^2\). The scalar mass bound of Theorem 2 applies with \(\lambda\) replaced by \(d_Z(B)\le 5/4\), and the variance is \(\exp(\Omega(T\sqrt N))\).

**Restricted Rayleigh quotient.** On the \(p=2\ell\) words in \(U\) (\(\ell=162\)), ideal two-step blocks between consecutive times are exactly \(s(1-s)V_t\). No other length-2 clock path joins those times. The uniform unit vector, both directions, three Hadamard blocks (quadratic form \(\sqrt2\)) and \(\ell-1\) permutation blocks (quadratic form 1) produce
\[
1-2s+2s(1-s)(1+\gamma),\qquad\gamma=[3(\sqrt2-1)-1]/\ell>0.
\]
The missing boundary edge is the \(-1\) in the numerator. Two-step jumps are nonnegative and may be dropped. Entrywise perturbation at most \(3\tau\) changes the form by at most \(3p\tau\). For large \(u\) the largest eigenvalue of \(A_U\) is at least \(1+\gamma s\). The Hadamard times \(28,82,136\) lie in the window and \(190\) does not, so there are exactly three.

**Even powers and marked connectors.** Here \(k=72KT^2\) is even because \(K\) is a power of two, so \(k-2h\) is even. Negative eigenvalues of the symmetric nonnegative matrix \(A_U\) then contribute nonnegative diagonal terms, and a Perron coordinate of mass at least \(1/p\) yields \((A_U^{k-2h})_{ii}\ge p^{-1}(1+\gamma s)^{k-2h}\).

Each ordinary one-step entry is at least \(s/(2\sqrt2)\), and the marked entry is \(s\sqrt T/(T+1)\). For ideal adjacent basis states the two-step entry equals the one-step entry times the sum of the endpoint diagonals, each at least \(1-sK=3/4\). Legal-to-illegal leakage is absent before rounding. After the \(3\tau\) entry error every connector of \(A\) has weight at least \(b=s/(8\sqrt T)\) for large \(u\). Paths that branch at Hadamards, or cross the first Hadamard and return, have length at most \(400\). Since \(b\le 1\) and \(ks=18T^2\),
\[
(A^k)_{jj}\ge p^{-1}b^{2h_0}(1+\gamma s)^{k-2h_0}=\exp(\Omega(T^2)).
\]
The connector contribution is only \(O(\log T)\) in the logarithm. For every full-support proposal, \(\mathbb E|Z|=(A^k)_{jj}\) and \(|\mathbb EZ|\le 1\), so \(\operatorname{Var} Z=\exp(\Omega(T^2))\). This covers every rounding within the paper’s \(3\tau\) budget. The \(XH\) schedule is a \(\pi/4\) rotation, so \((XH)^{8u}=I\) and the output bit is zero.

## Pre-existing material

No genuine error was found that affects Theorems 1–2, the chain corollary, the numerical gap \(487/1536\) versus \(287/1536\), or the \(1/32\) tolerance. The monomial tail \(e^{-6}\), the factor \(3/512\), the propagation weights \(q_0=1/[2(T+1)]\) and \(q_i=1/(4T)\), the gap \(1/(6T^2)\), and \(ms=36T^2\) all check. The Chebyshev sampler, the mass upper bound \(2\cdot 5^D\), and the Markov lower bound \(W_\lambda(f)\ge 2^{\sqrt A/3-8}\) are consistent on the range \(\lambda\le 5/4\) used here. The proof of that lower bound uses the interval \([1-h/2,1]\), which lies in \([0,1]\) for \(\lambda\le 3\). Every application in the paper has \(\lambda\le 5/4\).

## Mandatory correction

The last paragraph of Appendix B says that capping binary rejection leaves at least \(11/12\) of the ideal variance, by minimizing squared distance to a real center. What is proved is weaker. Conditional on success in a row, the draw is unbiased, and each path keeps at least \(11/12\) of its ideal probability, so the second moment retains a factor \(11/12\). Retention still depends on the row, so the implemented score \(Z'\) is not an independent thinning of \(Z\). The signed mean can shift by \(\Theta(\varepsilon\,\mathbb E|Z|)\). Because \(\mathbb E|Z|\) is itself \(\exp(\Omega(T^2))\), that shift can consume the second moment, and the factor \(11/12\) on the variance does not follow. Theorem 5 is unaffected: it is an ideal-sampler statement. Replace the sentence with the second-moment bound, or give a coupling in which the exhaustion event is independent of the path (acceptance probability exactly \(1/2\)).

## Optional changes

- State \(\lambda\le 3\) on the scalar mass lower bound, so that \([1-h/2,1]\subset[0,1]\) is explicit.
- Record the one-line comparison \(1-e^{-1}-10/128>1/2\) that turns the truncated Taylor error into a rise greater than \(1/2\).
- Name an explicit \(u_0\) from \(\gamma\ge s(1+2\gamma)+3p(\tau/s)\) and \(\tau/s\le 1/(9216T^2)\), and note that the longest marked connector used has length far below \(400\).
- In the chain-cost corollary, the proved coefficient lower order is \(9/40\), not only \(3/16\). The \(\Theta\) statement is already correct.

## Final scientific review

[Exact manuscript](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/ea2bbc797621a67ecabf262e9113678adc94610a/manuscript.tex), SHA-256 7681b653c255957031d0a61edfe766091116a1b5f6bfed577379eb86a435a08c.

The revised manuscript is **READY**. Appendix B, including Theorem 5, is correct, and the revised capped-mean argument meets the previous objection. No genuine pre-existing error was found in Theorems 1–2, Corollary 1, the chain-cost corollary, or the numerical gap.

## Appendix B

**Diagonal-word variance.** The alternating word is a computational-basis vector, so its energy lower-bounds \(d_Z(H)\). The same arithmetic as for \(\lambda\) gives \(d_Z(B_*)=1+s(d_Z(H)-2\mu)\ge 1+s(N-13)/32\), and for \(N\ge 26\) the \(2\tau\) rounding loss leaves \(d_Z(B)\ge 1+sN/128\). Thus \(m\ln d_Z(B)=\Theta(NT^2)\). Absolute scores on \(I,Z\) words contribute \(\sum_k|a_k|d_Z(B)^k\). For any real filter within \(1/32\) of \(x^m\) on \([0,1]\), positivity of the rounded contraction puts the signed mean in \([-1/32,33/32]\). Theorem 2 then yields \(\operatorname{Var} Y=\exp(\Omega(T\sqrt N))\).

**Restricted Rayleigh quotient.** On the stated three-wire schedule, \(D=27\), \(T=27(r-1)+2\), \(s=1/(4K)\), and \(k=m/2=72KT^2\). The window of \(\ell=162\) layers contains the Hadamard transitions at times \(28\), \(82\), and \(136\); time \(190\) lies outside, so there are exactly three. For the uniform vector, a permutation block has quadratic form \(1\) and a Hadamard block has quadratic form \(\sqrt 2\). With \(p=2\ell\) and \(\gamma=[3(\sqrt 2-1)-1]/\ell>0\), the \(\ell-1\) interior interfaces produce the off-diagonal mass \(2s(1-s)(1+\gamma)\). Dropping the nonnegative longer jumps and the extra \(s^2\) in the diagonal \((1-s)^2\), and charging an entrywise \(3\tau\) change at most \(3p\tau\) on this fixed set, gives
\[
\lambda_{\max}(A_U)\ge 1-2s+2s(1-s)(1+\gamma)-3p\tau.
\]
The deficit against \(1+\gamma s\) is \(s\bigl(\gamma-2s(1+\gamma)-3p(\tau/s)\bigr)\). Here \(\tau/s\le 1/(9216T^2)\) and \(s=\Theta(1/T)\), so the largest eigenvalue is at least \(1+\gamma s\) for all large \(u\). The bound \(\|B^2-B_*^2\|\le 3\tau\) is the right entrywise budget: \(\|B-B_*\|\le 3\tau/2\) and both matrices are contractions.

**Even powers and marked connectors.** Since \(72\) is even, \(k\) and \(k-2h\) are even. Even powers of the symmetric nonnegative matrix \(A_U\) have nonnegative diagonal spectral terms, and a Perron coordinate of mass at least \(1/p\) yields \((A_U^{k-2h})_{ii}\ge p^{-1}(1+\gamma s)^{k-2h}\).

Before rounding, a \(\Delta t=1\) entry of \(B_*^2\) is the one-step entry times the sum of the endpoint diagonals. Ordinary one-step entries are at least \(s/(2\sqrt 2)\); the marked entry is \(s\sqrt T/(T+1)\). Every basis diagonal is at least \(1-sK=3/4\). Legal-to-illegal leakage is absent before rounding, so after the \(3\tau\) error every connector used has weight at least \(b=s/(8\sqrt T)\) for large \(u\). The Hadamard block is fully nonzero on the two-word sector, so every state in \(U\) has a connector of length at most \(400\). With \(b\le 1\),
\[
(A^k)_{jj}\ge p^{-1}b^{800}(1+\gamma s)^{k-800}.
\]
The connector cost is \(O(\log T)\) in the logarithm, while \(ks=18T^2\) and \(k\ln(1+\gamma s)=18\gamma T^2+o(T^2)\) with \(\gamma>0\). Hence \((A^k)_{jj}=\exp(\Omega(T^2))\). For every full-support trajectory proposal, \(\mathbb E|Z|=(A^k)_{jj}\) and \(|\mathbb EZ|\le 1\), so \(\operatorname{Var} Z=\exp(\Omega(T^2))\). This covers every rounding inside the paper’s \(3\tau\) budget. The schedule multiplies to a rotation by \(\pi/4\), so \((XH)^{8u}=I\) and the output bit is zero.

**Capped mean.** The revised paragraph is right, and it does not assume independent thinning. Conditional on acceptance in a row, the draw is unbiased, and every path keeps a fraction at least \(1-k2^{-R}\ge 11/12\) of its ideal probability. Aborts only add mass at zero, so the capped law \(\nu'\) and the ideal law \(\nu\) satisfy \(\nu'(E)\ge(11/12)\nu(E)\) for every score event \(E\). Thus \(\nu'-(11/12)\nu\) is a nonnegative measure. For the nonnegative integrand \((z-a)^2\),
\[
\operatorname{Var}_{\nu'}Z\ge\tfrac{11}{12}\int(z-a)^2\,d\nu(z)=\tfrac{11}{12}\bigl(\operatorname{Var}_\nu Z+(\mathbb E_\nu Z-a)^2\bigr).
\]
The shift term is nonnegative, so a row-dependent retention factor cannot consume the second moment. The capped single-trial variance remains \(\exp(\Omega(T^2))\). Theorem 5 itself is an ideal-sampler statement. The closing remark correctly leaves fixed-confidence sample complexity open.

## Pre-existing material

The audited constants match the source. In particular, \(487/1536>9/32\) and \(287/1536<7/32\); \(m\cdot(3\tau/2)\le 3/512\); \((1-2s/M^2)^m\le e^{-6}<1/256\); \(q_0=1/[2(T+1)]\), \(q_i=1/(4T)\), and \(\sum q_i^{-1}\le 4T^2\); the rejecting-sector factor \(4T^2+2T\) is at most \(6T^2\); and \(ms=36T^2\) gives tail \(e^{-6}\). The Chebyshev weight \(W\le 2\cdot 5^D\), the sampler error \(13/512\), and the Markov bound \(W_\lambda(f)\ge 2^{\sqrt A/3-8}\) are consistent for the stated range \(\lambda\le 5/4\). The comparison \(1-e^{-1}-10/128>1/2\) is true, as is \([1-h/2,1]\subset[0,1]\) for \(\lambda\le 3/2\). The chain-cost lower estimate \(3/16\) is valid; the same inequalities give the sharper coefficient \(9/40\), and the \(\Theta(NT^2)\) claim is correct either way.

## Mandatory corrections

None.

## Optional changes

- Display \(1-e^{-1}-10/128>1/2\) in the proof of Theorem 2.
- Record that the scalar-mass argument uses \(\lambda\le 3\) to keep \([1-h/2,1]\subset[0,1]\); the applications use \(\lambda\le 5/4\).
- In the chain-cost corollary, the proved lower coefficient is \(9/40\), which is stronger than the printed \(3/16\).
- Name an explicit \(u_0\) from \(\gamma\ge 2s(1+\gamma)+3p(\tau/s)\) and \(\tau/s\le 1/(9216T^2)\). The longest connector used has length well below \(400\).
- The factor \(11/12\) is valid; the chosen cap actually retains at least \(23/24\) on a single trial.

Citations were not re-queried against external databases in this pass. Appendix B defines the walk and proves the moment identities internally, so those variance claims do not depend on an external lemma. The stated bibliographic resolutions for Cifuentes et al. and Montanaro–Shao were taken as prior verification, not rechecked here.
