# Claude review of v1.5.0

Automated manuscript review. [Editorial disposition](disposition.md)

## Initial review

[Exact manuscript](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/a3af1686c9981c30b43ebd8e9d9b392b7352999d/manuscript.tex), SHA-256 1ac24c84e822e178270bc5b6c708ac10f3f7e8179fe426378bf20470fa7c9a0d.

# Review report: Appendix C, Theorem 6

I worked from the pasted source only. I did not verify the SHA-256, run code or touch any files.

## Verdict: READY

I found no mathematical error in Theorem 6, Appendix C, or elsewhere in this version that invalidates a claim. The mandatory list is empty. The optional items below are clarity and robustness fixes, and one fidelity check against AGIK that I could not do from the source alone.

## What I checked in Appendix C, and its status

**Seven-sweep paired circuits.**
- The two circuits differ only in the last gate of sweep 5: CNOT versus identity.
- The control is wire n−1 fixed at 1 and the output is wire n, initially 0. This gives acceptance exactly 1 (YES) and 0 (NO), so the Appendix B margins (487/1536 and 287/1536) apply with room to spare.
- Hadamards on wires 4, 7, …, 3q+1 are q distinct bits, and n ≥ 3q+5 keeps them clear of wires n−1 and n.
- Spacing of three wires gives H, I, I, H on consecutive transitions, so any two consecutive edges contain at most one Hadamard.

**Dyadic grid and counts.**
- The term count J = 7(N−1) − 6 + 3 = 49n − 10 matches the table: 7 terms per within-block bond, 6 per crossing bond, 3 one-site terms.
- 2^11 ≡ 39 and 2^21 ≡ 1 (mod 49), so n = (2^a+10)/49 is an integer, starting at 42.
- K = 256J is a power of two. 2^18·J < 4S_0 ≤ 2^19·J holds, so η = τ/(2^19 J) is correct.
- F = (1−τ)s/(512η) = τ^{-1} − 1 is an integer, so ordinary coefficients (normalized traces in (1/512)ℤ) land exactly on the grid.
- The margins 487/1536 > 9/32 and 287/1536 < 7/32 are arithmetically correct.

**Pauli mask separation and normalization.**
- I recomputed all high-three-bit XOR masks under the stated encoding. They agree with the paper: (2,1), (5,1), (2,2), (1,2), (3,0), (7,4), (0,3), (1,2).
- For the two exceptional groups, Hadamard (2,1) and marked (5,1), no other term on the same bond shares the mask.
- Terms on other bonds cannot share a label, because the exceptional masks flip both sites of their own bond.
- The coefficient 2/64 for E+E† is right. The Hadamard magnitude (1−τ)s/(64√2) = 8F/√2 grid units is right. The marked magnitude 8F√T/(T+1) is right and far above one grid unit.
- Rounding scales each exceptional block by one positive scalar and keeps its signs and zeros.
- Rounding is decidable in polynomial time: the surd comparison a² vs 2b² works, and the distance to the grid is bounded below by an inverse polynomial.

**Exceptional blocks and the two boundary sites.**
- The nongrid marked diagonal lives on sites 1 and 2. Wires 1 and 2 are both zero, and AGIK preserves data order. Sites 1 and 2 therefore hold only the first two data bits or fixed flags.
- So the correction is a scalar d_t on each layer.
- I checked the coordinate reduction: B_tt = d_t I, B_{t+1,t} = a_t U_t, C_{tt}, C_{t+1,t} and C_{t+2,t} are all computed correctly.
- Hadamard rows have equal-magnitude entries, so the transition kernel is uniform. The clock law is autonomous.

**The TV bound.**
- Given a clock path, each Hadamard crossing refreshes its bit with a fair coin, and a two-step jump crosses at most one Hadamard.
- So Pr(D, X_k = j) = 2^{-q} Pr(D, t_k = 0) ≤ 2^{-q}.
- Under the retry cap, surviving-path probabilities are at most ideal, so Pr(D, score ≠ 0) ≤ 2^{-q}.
- The domination by μ + (h − max b)δ_0 is valid, and the TV bound follows.
- The product coupling 1−(1−2^{-q})^M ≤ M·2^{-q} then gives M ≥ 2^q/3. The conclusion is sound.

**Elsewhere, spot-checked.**
- Theorem 3: the Chebyshev bounds, the 13/512 budget, and the Markov-inequality converse (ℓ² ≥ 2mh/17 ≥ A/9).
- Section 3's clock spectrum and Section 4's norm bookkeeping.
- Corollary 4's constants: N ≥ 26, 3/16, 36K.
- Theorem 5's quadratic-form computation, including γ, and the (XH)^{8u} = I period.
- The variance inequality after the retry cap.

## Mandatory changes

None.

## Optional changes

1. **Say which edge actually differs.** In the (t, w) coordinates the g→g+1 edge is identical for YES and NO. The output bit is fixed by t, so CNOT acts as identity there. The real matrix difference is the terminal penalty d_T, plus the output relabeling. The text "only effect … is the local difference at that transition" is therefore misleading. D (visit time ≥ g−1) still covers T, so the proof stands. I recommend stating this explicitly, or defining D by reaching T−1.
2. **Narrow the mask sentence.** "Each gate mask flips both sites" is false for (3,0) and (0,3), and (1,2) appears twice. Restrict the claim to the exceptional masks (2,1) and (5,1). State that both bonds are within-block. Note that crossing-bond VR↔XG also has (2,1) but cannot coexist with a within-block bond.
3. **Make the boundary-site claim explicit.** Cite the AGIK data-order fact for "sites 1 and 2 hold only wires 1 and 2 or fixed flags" at all legal times, including transport phases. Say that the nongrid labels are rounded within the τ/2 budget and that YES and NO share the same rounding.
4. **Drop the 2^a congruence.** J = 2^a is only used to make η dyadic. Defining η = τ/(2^11·K) for any K ≥ 256J gives the same F and the same bounds. It also removes the 2^21 jumps in n. Currently the next admissible width after 42 is n = 87,652,394, so q ≥ 13 needs n ≈ 8.8×10^7.
5. **State the constants.** For n = 42, m ≈ 3.6×10^16 (unary). "Explicit" is asymptotic only. One sentence would say so.
6. **Note the rescaled Hadamard block.** After rescaling, a_t for the Hadamard edge differs from ordinary a_t. Entries remain dyadic, with magnitude 32⌊4√2F⌋η. The row-sum argument only needs independence of w, which holds.
7. **Verify the AGIK rule table once.** The counts 7 and 6, the ranks, and the masks follow from the paper's table. I could not check that table against AGIK's rules from this source. J = 49n−10 and the mask separation depend on it.

## Release candidate

[Exact manuscript](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/3311223ececf1f1cf2ff5e9b15916b1a22bf4fd8/manuscript.tex), SHA-256 57db9a2089f44b99cc48308102792527eae476084bf426e5d7aaab1d03041da2.

# Review of Appendix C, Theorem 6

## Verdict: READY

I found no mathematical error in Theorem 6, or in anything else that affects this version. The remaining items are wording and scope. I did not check the AGIK rule table against the PDF; I relied on your statement that it was verified.

## What I checked independently

**Widths, indices and grid**
- 2^11 = 2048 ≡ 39 and 2^21 ≡ 1 (mod 49), and 2048 + 10 = 49·42. So n = 42 is the first width, and consecutive admissible widths differ by a factor of about 2^21.
- The next width after 42 is 87,652,394. So q ≤ 12 uses n = 42, and q = 13 already needs n ≈ 8.8×10^7.
- Bond count: 7(7n−7) + 6·6 + 3 = 49n − 10 = J. The marked term replaces an existing term, so J is unchanged.
- T = 6D + n − 1 with D = n(2n+3). The gate on pair (j, j+1) of sweep a is the move aD+j−1 → aD+j. The last gate of sweep 5 is therefore the move g → g+1 with g = 5D + n − 2. This matches n−1 gate moves per sweep, and g < T.
- Grid: 4S_0 = 2^18 J + 4 lies in (2^18 J, 2^19 J]. So η = τ/(2^19 J) is the largest inverse power of two at most τ/(4S_0). Then (1−τ)s/(512η) = (1−τ)/τ · 2^10 sJ = τ^{-1} − 1 = F, an integer, since sJ = 2^{-10}.
- At n = 42, m = 144·K·T² = 144·2^19·21965² = 36,424,602,825,523,200. This matches the text exactly.

**Mask separation**
- The high-three-bit masks are the tag codes G = 0, R = 1, L = 2, F = 3, U = X = 4, A = 5, V = 6, S = 7. I recomputed the table.
  - Gate rule GR↔LG gives (2,1) on a within-block bond.
  - Marked SR↔L₀G gives (5,1).
  - The six competing within-block rules give (2,2), (1,2), (3,0), (7,4), (0,3), (1,2).
  - No competing within-block rule has (2,1) or (5,1).
- The one rule outside the list with (2,1) is crossing-bond VR↔XG. A bond is either within-block or crossing, and labels on different bonds have different supports. So no collision is possible.
- Each exceptional group is exactly (E+E†) ⊗ (low-bit Paulis).
  - Coefficients of E+E† are ±2/64 on the 32 even-Y strings.
  - Hadamard gives (1−τ)s/(64√2) = 4√2 F grid units.
  - The marked group gives (1−τ)s√T/(64(T+1)) = 8F√T/(T+1) grid units.
  - Rounding scales each block by one positive scalar and preserves signs and zeros.
- Ordinary projector entries lie in ½ℤ, so their normalized Pauli traces lie in 2^{-9}ℤ. After the (1−τ)s factor these are integer multiples of Fη.
- F is polynomial in n, so the surd distance bound (|32F² − N²| ≥ 1 for the Hadamard coefficient, and the analogous integer bound for the marked one) gives inverse-polynomial separation.

**Boundary sites and coordinates**
- The marked diagonal has entries 1/(T+1) and T/(T+1), and its support is sites 1 and 2.
- With data order preserved, sites 1 and 2 hold wires 1 and 2 (both zero) or fixed flags at every legal time. Any diagonal label on those sites is therefore a scalar on each layer.
- Squaring the coordinate blocks reproduces the stated C_tt, C_{t+1,t} and C_{t+2,t}.
- Hadamard edges are at least 3 apart, so a two-step jump crosses at most one.
- Row-sum independence and the uniform Hadamard kernel are correct.

**TV bound**
- Pr(D, X_k = j) = 2^{-q} Pr(D, t_k = 0) is exact. Every cut is crossed on the return, and the last-crossing coins are independent of the autonomous clock path.
- A surviving capped path has at most its ideal probability.
- The coupling gives TV ≤ max b ≤ 2^{-q}. Then TV(P^M) ≤ M·2^{-q} ≥ 1/3 forces M ≥ 2^q/3.

**Legality and margins**
- YES and NO use the same rounding. The CNOT versus identity coefficients are exact grid values, so the emitted matrices differ only in the CNOT bond.
- With acceptance exactly 1 and 0, the margins 487/1536 and 287/1536 hold.
- Bit costs are consistent: O(log n) fractional bits per coefficient, and a score of bit length O(k log n).

## Mandatory changes

None.

## Optional changes

1. **"Arbitrary work strings" wording.** The span sentence says "prescribed padding and output … and arbitrary work strings." State that the work strings range only over the q Hadamard bits. The control stays 1, the output stays 0 (before the late edge), and wires 1–3 stay 0. This is what makes the terminal pin a scalar d_T, and the YES and NO distinction rests on it.
2. **Say that D is a superset.** In the work coordinates, YES and NO agree through layer T−2. The only difference is d_T. D = {visit ≥ g−1} is the exact physical divergence set (the physical row at g−1 uses the CNOT edge). It is also a valid superset in the coordinates, since g−1 < T−1. One clause would say so and remove the apparent tension with "the changed edge."
3. **Narrow "flip both sites."** Make it explicit that the masks (3,0) and (0,3) flip one site and that (1,2) occurs twice. Only the exceptional masks (2,1) and (5,1) need the separation argument. All collisions among the other masks sum grid values.
4. **Wire 3.** Add that wire 3 is also a fixed zero, in case data shifts place it near site 2 in transport.
5. **Scope of constants.** Say that "explicit" is asymptotic. For q ≤ 12 the unary power is about 3.6×10^16. For q ≥ 13, n ≈ 8.8×10^7 and m ≈ 5×10^39. "n = Θ(q)" carries a constant near 3·2^21. The "superpolynomial in written length" claim holds only along the family, and each q uses the least admissible width, so the ratio n/q can be about 10^6.
6. **The 2^a congruence.** It is only needed to make J = 2^a, so that η is exactly τ/(2^19 J) and F = τ^{-1} − 1. It is not needed for validity. This is optional, and it keeps the stated grid.

## Quantifiers covered and not covered

**Covered**
- Every q ≥ 1.
- Every admissible width n = (2^{11+21u} + 10)/49 with n ≥ 3q+5.
- Cap c = 3/2 only, so d = 1/2.
- Every common positive retry cap, with exhaustion scoring zero.
- Every M and every randomized decoder with success at least 2/3 on both inputs.

**Not covered, and stated as such**
- Other caps c.
- Other roundings.
- Other proposals; Theorem 5 handles variance for every full-support proposal, and Theorem 6 covers only the specified row proposal.
- Widths outside the congruence family.
