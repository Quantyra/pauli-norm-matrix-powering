# Grok review of v1.5.0

Automated manuscript review. [Editorial disposition](disposition.md)

## Initial review

[Exact manuscript](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/a3af1686c9981c30b43ebd8e9d9b392b7352999d/manuscript.tex), SHA-256 1ac24c84e822e178270bc5b6c708ac10f3f7e8179fe426378bf20470fa7c9a0d.

**READY.** Theorem 6 is correct. No mandatory change. The single-score total variation is at most \(2^{-q}\), including under a common retry cap, and \(M\ge 2^q/3\) follows for any score-only rule with success at least \(2/3\).

### Trajectory coupling and last returns
The YES/NO pair differs only on the sweep-5 edge \(g\to g+1\) (CNOT versus identity). Both are permutation gates, so they have the same absolute one-step weight. In \(C=B^2\), a two-step reaches at most two layers ahead, so every row at clock time \(t\le g-2\) is identical in the two experiments, including normalizers. The first entrance into times \(\ge g-1\) is therefore made from a common row. Avoiding paths, including their scores, couple exactly. Call this event \(A\) and put \(h=\Pr(D)\) for \(D=A^c\). The value of \(h\) is common.

On the legal line, \(B_{tt}=d_t I\) and \(B_{t+1,t}=a_t U_t\) with \(U_t\in\{I,H_i\}\) after the uniform block rescaling. Absolute row sums of \(I\), \(H\), and \(H_iH_j\) are constant across work strings, so the clock is autonomous. Conditional on a clock path, each Hadamard crossing has kernel
\[
\frac{|H_{y_ix_i}|}{\sqrt2\text{-row sum}}=\frac12,
\]
independent of the incoming bit. Distinct cuts use distinct crossings. Hadamards in one sweep are three layers apart, so one two-step never applies two of them. The non-Hadamard steps are deterministic bijections, and the two-step blocks are products of those one-step maps, so time-line holonomy is trivial. On a path in \(D\) that ends at time 0, the last crossing of each of the \(q\) cuts therefore writes an independent fair bit, and every other bit of \(j\) is restored. Hence
\[
\Pr_{\mathrm{ideal}}(D,X_k=j)=2^{-q}\Pr_{\mathrm{ideal}}(D,t_k=0)\le 2^{-q}.
\]
A nonzero score occurs only on a return to \(j\), so \(\Pr(D,\mathrm{score}\ne 0)\le 2^{-q}\).

### Matched zero submeasure and total variation
Let \(\mu\) be the common score submeasure on \(A\), of mass \(1-h\). Let \(b_\pm\) be the \(D\)-mass of nonzero scores. Then \(b_\pm\le 2^{-q}\) and
\[
P_\pm=\mu+(h-b_\pm)\delta_0+\nu_{\pm,\neq 0}.
\]
Both dominate \(\rho=\mu+(h-\max(b_+,b_-))\delta_0\), which has mass \(1-\max(b_+,b_-)\). The unmatched mass is at most \(2^{-q}\), so
\[
d_{\mathrm{TV}}(P_+,P_-)\le 2^{-q}.
\]

### Cap, products, and the score-only bound
Under any common retry cap, a non-abort path \(\gamma\) has probability \(P_{\mathrm{ideal}}(\gamma)\prod\sigma(x_s)\le P_{\mathrm{ideal}}(\gamma)\), even if the survival factors \(\sigma\) depend on the row. Aborting scores 0. Summing over \(D\)-returns gives \(\Pr(D,\mathrm{score}\ne 0)\le 2^{-q}\) without needing the coins to stay fair after conditioning on survival. Rows with \(t\le g-2\) are identical, so the capped avoid-set still contributes the same \(\mu\). The same total-variation bound holds.

Independent coupling of \(M\) trials yields
\[
d_{\mathrm{TV}}(P_+^{\otimes M},P_-^{\otimes M})\le 1-(1-2^{-q})^M\le M2^{-q}.
\]
A rule, randomized or not, that sees only the scores and succeeds with probability at least \(2/3\) on both inputs has YES-output gap at least \(1/3\). For a \([0,1]\)-valued function that gap is at most the product total variation, so \(M\ge 2^q/3\).

The grid arithmetic that feeds this argument also checks: \(J=49n-10=2^a\), \(F=(1-\tau)s/(512\eta)=\tau^{-1}-1\), Hadamard blocks sit at \(4F\sqrt2\) grid units, and the marked block at \(8F\sqrt T/(T+1)>1\). Equal magnitudes round by one positive scalar, so the \(H\) kernels stay fair. Acceptance probabilities 1 and 0 sit inside the Appendix A margins, and \(\lambda\le 5/4\le 3/2\).

### Mandatory changes
None.

### Optional changes
- Display \(P_\pm=\mu+(h-b_\pm)\delta_0+\nu_{\pm,\neq 0}\) and the pathwise bound \(P_{\mathrm{cap}}(\gamma)\le P_{\mathrm{ideal}}(\gamma)\) as separate lines.
- One sentence would make the trivial holonomy of the deterministic steps explicit, rather than leaving it inside “distinct fair coin.”
- The factor \(1-(1-2^{-q})^M\) already forces about \(\ln(3/2)\,2^q\) trials. The published \(2^q/3\) bound is valid and weaker.
- The two competitor masks \((1,2)\) are not unique, but neither equals the exceptional masks \((2,1)\) and \((5,1)\). A short remark would prevent a false collision reading.

### Elsewhere
No other genuine error shows up that affects this version. The idle-clock weight \(p/2\), the \(e^{-6}\) tails, the constants \(487/1536\) and \(287/1536\), the filter lower bound \(2^{\sqrt A/3-8}\), and the chain identity \(\lambda(B_*)=1+s(\lambda(H)-2\mu)\) all recompute as written.

## Release candidate

[Exact manuscript](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/3311223ececf1f1cf2ff5e9b15916b1a22bf4fd8/manuscript.tex), SHA-256 57db9a2089f44b99cc48308102792527eae476084bf426e5d7aaab1d03041da2.

**READY**

No mandatory change. Theorem 6’s quantifiers hold for every integer \(q\ge 1\): one matched YES/NO pair at cap \(3/2\), ideal draws and every common retry cap, and every score-only rule with success at least \(2/3\) on both inputs. The single-trial bound is \(d_{\mathrm{TV}}(P_+,P_-)\le 2^{-q}\), and therefore \(M\ge 2^q/3\).

### Trajectory coupling
Sweep 5 has \(n-1\) gate moves, indexed \(i=0,\ldots,n-2\). The last move is \(i=n-2\), on wires \((n-1,n)\), at
\[
g=5n(2n+3)+n-2.
\]
A two-step from \(t\le g-2\) uses only edges at most \(g-1\to g\), so it misses \(g\to g+1\). Diagonals of a permutation propagation do not depend on the unitary, and the terminal pin \(|G_0\rangle\langle G_0|\) is idle before time \(T\). Thus every row at \(t\le g-2\) agrees in entries, normalizers, and signed scores. The hit event \(D=\{\text{some clock time}\ge g-1\}\) has a common probability \(h\). Avoiding paths, including scores, couple exactly.

The pin changes only the aligned scalar \(d_T\): after the late gate the output bit is fixed by the clock time, so the penalty is \(1\) on NO and \(0\) on YES while remaining \(d_T I\) on the work string. That discrepancy sits inside \(D\).

### Last returns
Hadamards lie in sweep 1 at times \(D+(3k-1)\) for \(k=1,\ldots,q\), all strictly before \(g\), and three layers apart. One two-step therefore contains at most one. Absolute row sums of \(I\) and of one Hadamard are \(1\) and \(\sqrt 2\), independent of the incoming work string, so the clock law is autonomous. Conditional on the clock path, each Hadamard kernel equals \(1/2\).

On the time path, a walk from \(0\) into \(D\) and back to \(0\) crosses every earlier cut. The last crossing of each of the \(q\) cuts is a distinct fair coin; sweep 0 and the other non-Hadamard steps are deterministic bijections, and a closed walk on the path toggles the YES CNOT an even number of times. Every non-work bit of \(j\) is restored, so
\[
\Pr_{\mathrm{ideal}}(D,X_k=j)=2^{-q}\Pr_{\mathrm{ideal}}(D,t_k=0)\le 2^{-q}.
\]
A nonzero score occurs only on a return to \(j\), hence \(\Pr(D,\mathrm{score}\ne 0)\le 2^{-q}\).

### Matched zero submeasure and total variation
Let \(\mu\) be the common score image on \(D^c\), of mass \(1-h\). Let \(b_\pm=\Pr_\pm(D,\mathrm{score}\ne 0)\le 2^{-q}\). Then \(b_\pm\le h\) and
\[
P_\pm=\mu+(h-b_\pm)\delta_0+\nu_{\pm,\ne 0}.
\]
Both dominate \(\rho=\mu+(h-\max(b_+,b_-))\delta_0\), of mass \(1-\max(b_+,b_-)\). The unmatched mass is at most \(2^{-q}\), so
\[
d_{\mathrm{TV}}(P_+,P_-)\le 2^{-q}.
\]

### Cap, products, score-only bound
A surviving path obeys \(P_{\mathrm{cap}}(\gamma)=P_{\mathrm{ideal}}(\gamma)\prod_s\sigma(x_s)\le P_{\mathrm{ideal}}(\gamma)\) even when the retry survival \(\sigma\) depends on the row. Aborts score \(0\). Summing over \(D\)-returns preserves \(\Pr(D,\mathrm{score}\ne 0)\le 2^{-q}\) without a conditional-fairness claim. Rows at \(t\le g-2\) still match under a common cap, so the avoiding image \(\mu\) is unchanged and the same total-variation bound holds.

For \(M\) independent trials,
\[
d_{\mathrm{TV}}(P_+^{\otimes M},P_-^{\otimes M})\le 1-(1-2^{-q})^M\le M\,2^{-q}.
\]
Success at least \(2/3\) on both inputs forces a YES-output gap at least \(1/3\) for any \([0,1]\)-valued function of the scores. That gap is at most the product total variation, so \(M\ge 2^q/3\).

### Checks that feed the argument
\(2^{11}\equiv 39\pmod{49}\) and \(2^{21}\equiv 1\pmod{49}\), so \(n=(2^a+10)/49\) is an integer. The least such \(n\ge 3q+5\) satisfies \(n=\Theta(q)\). Term count: seven summands on each within-block bond and six on each of the six crossings, plus two open ends and the pin,
\[
J=7(N-1)-6+3=49n-10=2^a.
\]
The largest inverse power of two at most \(\tau/(4S_0)\) is exactly \(\eta=\tau/(2^{19}J)\), because \(4S_0=4+2^{18}J\) lies strictly between \(2^{18}J\) and \(2^{19}J\). A smaller grid would be a different emission. Then
\[
F=\frac{(1-\tau)s}{512\eta}=\tau^{-1}-1,
\]
Hadamard blocks have equal magnitude \(8F/\sqrt 2\) grid units, and the marked block has magnitude \(8F\sqrt T/(T+1)>1\). Equal absolute values round by one positive scalar, so the Hadamard kernels stay fair. Masks from the stated 4-bit codes: gate \((2,1)\), marked \((5,1)\); the six competitors are \((2,2),(1,2),(3,0),(7,4),(0,3),(1,2)\). Neither exceptional mask repeats. For \(n=42\), \(T=21965\) and
\[
m=36{,}424{,}602{,}825{,}523{,}200.
\]
Acceptance probabilities \(1\) and \(0\) lie inside the Appendix A margins \(487/1536>9/32\) and \(287/1536<7/32\). Here \(\lambda(B)\le 5/4\le 3/2\). Any operator supported on sites 1 and 2, rounded or not, is a scalar on each legal layer once those sites hold only wires 1 and 2 or flags; rule 3 shifts data one site to the right, and wires \(4,7,\ldots,3q+1\) never occupy those sites.

### Mandatory changes
None.

### Optional changes
- The factor \(1-(1-2^{-q})^M\) already forces \(M\ge \ln(3/2)/(-\ln(1-2^{-q}))\), about \(\ln(3/2)\,2^q\) trials. The published \(2^q/3\) bound is valid and weaker.
- Mask \((1,2)\) is shared by \(FU\leftrightarrow LV\) and \(FR\leftrightarrow LF\). Neither equals \((2,1)\) or \((5,1)\). One sentence would prevent a false collision reading.
- The identities \(P_\pm=\mu+(h-b_\pm)\delta_0+\nu_{\pm,\ne 0}\) and \(P_{\mathrm{cap}}(\gamma)\le P_{\mathrm{ideal}}(\gamma)\) can be displayed alone.

### Elsewhere
No other genuine error shows up that affects this version. Recomputed as written: the \(e^{-6}\) tails, \(487/1536\) and \(287/1536\), \(\ell^2\ge 2mh/17\ge A/9\) giving \(W_\lambda(f)\ge 2^{\sqrt A/3-8}\), the chain identity \(\lambda(B_*)=1+s(\lambda(H)-2\mu)\ge 1+s(N-13)/32\), and, on the three-wire witness, Hadamards at times \(28,82,136\) with \((XH)^{8u}\) closing to acceptance \(0\).
