# Claude review of v1.4.0

Automated manuscript review. [Editorial disposition](disposition.md)

The initial request timed out without a completed report. The release-candidate review below covers the complete revised source.

## Final scientific review

[Exact manuscript](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/ea2bbc797621a67ecabf262e9113678adc94610a/manuscript.tex), SHA-256 7681b653c255957031d0a61edfe766091116a1b5f6bfed577379eb86a435a08c.

# Referee report

**Verdict: READY.** I found no mandatory corrections. I rechecked the algebra of the main theorems and Appendix B line by line and found no error that affects the release. I also checked Theorem 5's inputs against the stated constructions. I could not check the external locators, which are listed at the end. The optional items below are presentation only.

## Theorem 5 (Appendix B, two-step walk)

**Input and schedule.**
- The three wires are a zero spectator, a control fixed at one, and a zero target/output.
- The pair (target H, CNOT with control 1) acts as X·H, which is rotation by π/4. Its eighth power is the identity, so the output stays 0 and p = 0. This is a valid NO instance.
- r = 16u+2 matches 8u pairs of sweeps plus the two identity sweeps.
- D = n(2n+3) = 27 and T = 27(r−1)+2 are internally consistent.
- Sweep a's second slot starts at time 27a+1, so the Hadamard edges are (28,29), (82,83) and (136,137), at a = 1, 3, 5.
- Edge (163,164) is the next CNOT. It lies outside the window, so exactly three Hadamards are internal to U (times 2 to 163).

**Legal sector and phases.**
- The clock term h_* has diagonal 1/(2(T+1)) at time 0. With π_0 = 1/2 and π_1 = 1/(2T), the energy q_0 = 1/[2(T+1)] is correct.
- Each interior layer has diagonal exactly 1−s and off-diagonal block sV_t/2. This follows from two incident projectors of weight 1/2 each, and the sign is positive for B_* = I − sH.
- The chain B_*² block is exactly s(1−s)V_t, since only the two same-gate paths contribute.
- The gaps are valid: Σq_i^{-1} = 4T²+2 ≤ 4T²+2T for the rejecting sector, and 4T²−2T+2 ≤ 4T² for the accepting sector.

**Quadratic form.**
- I recomputed the uniform-vector form. It is 2s(1−s)[1+(3√2−4)/ℓ], which matches γ = [3(√2−1)−1]/ℓ ≈ 1.5·10⁻³.
- The inequality 1−2s+2s(1−s)(1+γ)−3pτ ≥ 1+γs needs roughly s ≲ γ/2, about 7·10⁻⁴. This holds for large u because s ≤ 1/(1024J). "Sufficiently large u" is therefore honest, but the threshold is not trivial.

**Rounding and constants.**
- The bound τ/s ≤ 1/(9216T²) follows from m = 144KT² and s = 1/(4K).
- The perturbation bounds 3τ per entry and 3pτ on U hold.
- Realness holds: odd-Y coefficients vanish and stay zero.
- k = 72KT² is even and ks = 18T².

**Connectors.**
- Any marked or ordinary entry times a diagonal sum at least 3/2 exceeds b = s/(8√T).
- Reaching the target-1 words at times before 28 by crossing H and returning is sound.
- Even-power positivity of A_U^{k−2h} and the pigeonhole step give the exponent 18γT² − O(log T).

**Estimator and capped law.**
- E|Z| = (A^k)_jj holds for any proposal with full support on nonzero entries.
- Var ≥ (E|Z|)² − 1 follows from |EZ| ≤ 1.
- The capped-mean argument is rigorous. Retention is at least 1−k2^{−R} ≥ 23/24 ≥ 11/12, so ν′ ≥ (11/12)ν as measures. The integrand (z−a)² is nonnegative, so integrating against it is valid, and the decomposition into variance plus squared mean shift is correct. No thinning assumption is needed, and path-dependent retention is covered.

**Bit costs.**
- Dyadic row weights with real and imaginary parts give exact integer rejection sampling.
- Row enumeration is at most S² pairs, and the per-draw bit cost is polynomial.

**Scope.**
- Theorem 5 lower-bounds one plain walk estimator on an easy NO instance. It does not bound other estimators, and the manuscript says so.

## Other claims audited (no error found)

- **Clock (Sec. 3–4).**
  - The Fourier-mode sign, R = C†(2Π−I)C and the p/2 weight are correct.
  - The gap 1−2/M², the weight K = 2M, e^{−6} < 1/256, and the constants 487/1536 and 287/1536 all check.
  - The Hadamard conjugation on clock bits preserves λ.
- **Theorem 3.**
  - The bound q ≤ 2A/ln 2, the tail 2e^{−6} < 1/128, and W_2(T_k) ≤ 5^k (21·5^{k−1} ≤ 25·5^{k−1}) are correct.
  - The error budget 12/512 + 1/512 = 13/512 is correct.
  - The converse is correct: Markov on I with ‖g‖ ≤ 17/16, 2mh/17 ≥ A/9, and ℓ ≤ log₂W + 8.
- **Corollary 4 and the Z-only variance.**
  - The ranks 16 and 12, and μ ≤ 7(N−1)/64+3/16, are valid and conservative.
  - The (N−13)/32 bound and the algebra 3/16·NT² ≤ A ≤ 36KT² are correct.
  - d_Z(H) ≥ the diagonal of H on a basis word is valid.

## Genuine pre-existing error

None found. The notation collisions below are not errors.

## Optional changes

1. Replace "the published schedule" in the Theorem 5 proof with an explicit reference to Appendix A with n = 3 and D = 27. Add a remark that the argument needs only a fixed number of Hadamard edges inside a fixed-length window. Then a different AGIK per-round count would shift the times but not break the proof.
2. State the "sufficiently large u" threshold, or at least that it follows from s ≤ 1/(1024J).
3. Put the scope into the theorem statement. The theorem is about the ideal walk, and the capped sampler (the stated dyadic row proposal) is covered by the closing paragraph.
4. Reduce symbol overloading:
   - M is the clock size and the trial count.
   - D is the clock half-length, the degree cutoff and the round length.
   - A is the clock operator, A = m ln λ, a flag, and |C|.
   - C is the circuit and B².
   - Z and Y are both Paulis and scores.
5. Note that the Theorem 5 exponent (about 0.027·T²) exceeds the filter-based exp(Θ(T√N)) of Corollary 4. The two are lower bounds for different estimators, so this is not a contradiction. A sentence would pre-empt the question.
6. The self-citation [vone] is version 1.0.0. Make the version relationship explicit.

## Bibliography

- **Verified by supplied checks.** Cifuentes et al. (PRX Quantum 7, 020364, DOI 10.1103/g5x4-jcsz, Crossref title) and Montanaro–Shao Prop. 5.5 (arXiv:2311.06999v3, §5.2). I accept these as supplied. I did not re-fetch them.
- **Not independently verified, so bibliographic uncertainty remains.**
  - The AGIK locators ("Fact 2.2", the rules preceding Fig. 1, and the D = n(2n+3) round count).
  - Bausch–Crosson "Lemma 4".
  - Cifuentes "Discussion and Sec. IV A" and "Appendix A".
  - The Montanaro–Shao page range.
  - The author list and DOI details for the remaining entries.
  - The author should confirm these against the sources.
