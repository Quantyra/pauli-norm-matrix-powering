# Claude review of v1.2.0

Automated manuscript review. [Editorial disposition](disposition.md)

## Initial revision

[Reviewed source](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/8c567f9bf3977b0ea050c5e6c4c6064b167c03f3/manuscript.tex), SHA-256 `7b8f605792ef5d25babaf28b5a355d1e55078cc295997b48f1f5f14015ec7e1a`.

## Referee report — verdict: **REVISE** (minor; no mathematical error found)

**What I verified independently.** The corollary's quantitative chain holds. λ(h) ≤ 2^k√(2^{-k}tr h²) ≤ 2^k ≤ 256 is correct for the two-site projectors (each (J_in−J_outV)(·)†/2 is a projector, M†M = 2I), so K ≥ 256J gives both 0 ≤ H ≤ KI (via ‖H‖ ≤ J) and λ(H) ≤ K; hence B\* = I−sH satisfies (1−d/2)I ≤ B\* ≤ I and λ(B\*) ≤ 1+d/2 ≤ c for d ≤ min(1/2, c−1) — global positivity, not merely positivity on legal shapes, which matters because unused levels of the 13-symbol/16-level encoding carry no penalty. The weighted clock is consistent: h\* reproduces q₀ = 1/[2(T+1)], q_i = 1/(4T), kernel weights π₀ = 1/2, π_t = 1/(2T), so the zero-energy weight at j is exactly p/2. Σ q_i^{-1} ≤ 4T²+2T gives visible positive energies ≥ 1/(6T²), and m = 72KT²/d (an integer, K a power of two, d an inverse power of two) yields e^{-6} < 1/256. Inward rounding on the η-grid gives ‖B−B\*‖ ≤ 3τ/2, hence 3/512, and 487/1536 > 9/32, 287/1536 < 7/32. Runtime is uniformly polynomial: J = O(N), T = O(n²r), S₀ = 1+4⁸J, m = poly, coefficients O(log mS₀) bits, and sign tests in Q(√2, √T) by bisection are polynomial.

**Mandatory corrections.**
1. Prove, not assert, that the installed list (transition terms, h\*, the single site-N penalty) leaves the legal-shape span invariant; no illegal-configuration penalties are installed, so the entire "visible energy" gap — and therefore the corollary — rests on exact invariance. One explicit appeal to AGIK Fact 2.2 in both directions, covering the open-end one-site rules, closes it.
2. Give explicit AGIK site/time indices for "the gate marker visits site 2 exactly once" and "reaches site N only at the terminal time," and tie T = n(2n+3)(r−1)+n−1 to the cited figure. h\*'s inverse domain and the correctness of a single rejection penalty both depend on these; state where n ≥ 3, r ≥ 2 are used.

**Optional polish.** Say which clause of Theorem 1 the corollary inherits (the c > 1 completeness and 1/32 tolerance, not the c ≤ 1 sampler). Clarify that "the algorithms in Section 2 apply" means containment via the quantum estimator — the λ^m-rescaled classical sampler is exponential at m = Θ(KT²). Note that collecting duplicates can only decrease λ.

## Release candidate

[Reviewed source](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/e1434f83fe5e7725cce723f143eded0173114b08/manuscript.tex), SHA-256 `db5780cfc13942210ac37d2eea16cd3c5605400f23b0c2c7069814831347526d`.

# Referee report — verdict: **READY**

**Both mandatory corrections are addressed.**

*(1) Invariance of the legal-shape span.* The revision now argues it rather than asserting it: Fact 2.2 is invoked for every unmodified bond **and** the open-end one-site rules, "with the missing directions at the endpoints" covering both directions; the diagonal blocks of (J_in−J_outV)(·)†/2 are shown to test identical source/target tags while the off-diagonal blocks transport data by V and V†, so each summand either annihilates a shape or maps into the two incident shapes; the marked summand inherits this from the first-bond tag analysis; the terminal |G₀⟩⟨G₀| at site N vanishes on all earlier shapes. The closing clause — invariance for arbitrary nonspectator w, plus Hermiticity making the subspace reducing — is exactly what the visible-energy argument needed, since no illegal-configuration penalty is installed. Correct as written.

*(2) Explicit indices.* The marker now occupies site an+1+i at time aD+i (0 ≤ i < n, 0 ≤ a < r), with the marked start replacing a=0, i=0. Checks out: a=r−1, i=n−1 gives site rn = N at time (r−1)D+n−1 = T, and site 2 forces a=0, i=1, the unique first successor on which h⋆'s inverse fires. D = n(2n+3) and T = (r−1)D+n−1 are now tied to the text following AGIK Fig. 1, and r ≥ 2 is used where needed (final block distinct from the marked one).

**Re-verified in the final text.** λ(h) ≤ 2^k√(2^{-k}tr h²) ≤ 256 for k ≤ 8; K ≥ 256J gives 0 ≤ H ≤ KI globally and λ(H) ≤ K, so B⋆ = I−sH with s = d/(2K) satisfies (1−d/2)I ≤ B⋆ ≤ I and λ(B⋆) ≤ 1+d/2 ≤ c — positivity on the whole 16-level space, not only legal shapes. Zero-energy weight π₀⟨z|C†ΠC|z⟩ = p/2; Σq_i^{-1} ≤ 4T²(+2T rejecting) gives visible gap ≥ 1/(6T²); m = 72KT²/d is an integer and yields e^{-6} < 1/256. Inward η-rounding (η ≤ τ/(4S₀), ≤ 2η per slot) gives ‖B−B⋆‖ ≤ 3τ/2, hence 3/512, and 487/1536 > 9/32, 287/1536 < 7/32 — including coupling off the legal subspace. Runtime polynomial; sign/enclosure tests in Q(√2,√T) by bisection.

**Optional polish only.** (i) "Since n ≥ 3, site 2 carries G only at a=0, i=1" — the index arithmetic needs only n ≥ 2; n ≥ 3 is genuinely used for the leftmost spectator plus output routing. Attribute it there. (ii) One clause noting that the λ^m-rescaled classical sampler is exponential at m = Θ(KT²), so containment is via the quantum estimator. (iii) Note that collecting duplicates can only decrease λ.
