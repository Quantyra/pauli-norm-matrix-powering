# Grok review of v1.2.0

Automated manuscript review. [Editorial disposition](disposition.md)

## Initial revision

[Reviewed source](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/8c567f9bf3977b0ea050c5e6c4c6064b167c03f3/manuscript.tex), SHA-256 `7b8f605792ef5d25babaf28b5a355d1e55078cc295997b48f1f5f14015ec7e1a`.

**READY.** No mandatory correction. Appendix A’s chain reduction supports the corollary: the modified start, the terminal pin, and the moment bounds do not leak into the measured diagonal.

The bond-(1,2) term \(h_\star=(T+1)^{-1}\sum_b|u_b\rangle\langle u_b|\) with \(|u_b\rangle=|SR_b\rangle-\sqrt{T}|L_0G_b\rangle\) is a rank-2 projector. The summands are orthogonal and \(\|u_b\|^2=T+1\), so each summand is already a projector. On a legal line it is the projector onto \(|0\rangle-\sqrt{T}|1\rangle\). Together with the later Kitaev projectors onto \(|i\rangle-|i+1\rangle\), the kernel amplitudes satisfy \(\alpha_0=\sqrt{T}\,\alpha_1\) and \(\alpha_1=\cdots=\alpha_T\), hence \(\pi_0=1/2\) and \(\pi_t=1/(2T)\). The initial product word is exactly time 0, so its zero-energy weight is \(\pi_0\langle z|(I-Q)|z\rangle=p/2\).

Reverse uniqueness is local. \(S\) meets no unmodified rule; passive sites do not complete an old rewrite; the old inverse on bond (1,2) is removed; the new inverse matches \(L_0G_b\) and vanishes on \(L_1G_b\). In the AGIK block layout the gate marker occupies site 2 only on the first right-sweep, so that inverse is not reused. Fact 2.2 covers the remaining moves. The legal history subspace is invariant and contains \(j\). Deleted \(G_0\)-starts, the \(L_1\) branch, and the three unused levels per site may be extra zero modes, but they are orthogonal to \(j\) and do not move the entry. Rounding can couple them; the telescope \(\|B^m-B_*^m\|\le 3/512\) already includes that coupling.

The quadratic forms match the projectors: \(q_0=1/[2(T+1)]\), \(q_i=1/(4T)\), and \(\sum q_i^{-1}=4T^2-2T+2\le 4T^2\). Accepting excitations orthogonal to the flat mode are at least \(1/(4T^2)\). Grounding the reject penalty with edge weight \(\pi_T\) gives at least \(1/(4T^2+2T)\ge 1/(6T^2)\). With \(s=d/(2K)\) and \(m=72KT^2/d\), the visible excited contribution is \(<1/256\). Inward dyadic rounding keeps the Pauli support on at most two consecutive sites, the cap, and positive-definiteness. The same \(1/48\) compilation loss yields \(487/1536>9/32\) and \(287/1536<7/32\), so an additive \(1/32\) estimate compared with \(1/4\) decides the image.

Optional polish: say that each \(u_b\) has squared length \(T+1\), rather than calling it normalized; name the decoupled zero modes in one sentence.

## Release candidate

[Reviewed source](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/e1434f83fe5e7725cce723f143eded0173114b08/manuscript.tex), SHA-256 `db5780cfc13942210ac37d2eea16cd3c5605400f23b0c2c7069814831347526d`.

**READY**

The required revision is in place and holds. The gate marker is indexed at site \(an+1+i\) at time \(aD+i\), open-end rules use the same \((J_{\mathrm{in}}-J_{\mathrm{out}}V)\) projectors as the bond rules, and each summand is shown either to vanish or to exchange only the two incident legal shapes.

**Mandatory corrections:** none.

On bond \((1,2)\), \(h_\star=\frac1{T+1}\sum_b|u_b\rangle\langle u_b|\) with \(|u_b\rangle=|SR_b\rangle-\sqrt T|L_0G_b\rangle\) is a projector: \(\|u_b\|^2=T+1\) and the two values of \(b\) are orthogonal. Its kernel forces \(\alpha_0=\sqrt T\,\alpha_1\), and every later edge forces \(\alpha_t\) constant, so \(\pi_0=1/2\) and \(\pi_t=1/(2T)\). The initial product word therefore carries zero-energy weight \(p/2\). The quadratic form has \(q_0=1/[2(T+1)]\) and \(q_i=1/(4T)\). Mean-zero accepting paths have energy at least \(1/(4T^2)\). Rejecting paths, with the site-\(N\) pin \(|G_0\rangle\langle G_0|\) as one extra edge of weight \(\pi_T\), have energy at least \(1/(4T^2+2T)\ge1/(6T^2)\). For \(s=d/(2K)\) and \(m=72KT^2/d\), the visible tail is at most \(e^{-6}<1/256\).

Inward rounding changes the moment by at most \(3/512\), creates no new Pauli labels, and keeps the coefficient cap. Any coupling out of the legal shapes is covered by that operator-norm bound. The windows \(487/1536\) and \(287/1536\) lie strictly outside \([7/32,9/32]\), and an additive error of \(1/32\) still falls on the correct side of \(1/4\). The guards \(n\ge3\) and \(r\ge2\) separate the marked bond, its first successor, and the terminal site, so the new inverse matches only that successor. The three unused levels stay outside the measured word.

**Optional polish:** display \(\sum_i q_i^{-1}=4T^2-2T+2\) and \(\pi_T^{-1}=2T\); record \(1+d/2\le(c+1)/2\le c\); state that AGIK transport and turn symbols are disjoint from \(G\), making the sweep index a complete list of times site 2 carries \(G\).
