# Claude review of v1.6.0

Automated manuscript review. [Editorial disposition](disposition.md)

## Release candidate

[Reviewed manuscript](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/1eeddebcc7e0306ed109593a3980c2d8c999ee24/manuscript.tex), SHA-256 17461fd7e2d54c45475c357b89b47957ea88514ae659db3280f7e742f9e48dc2.

# Review of "A fixed Pauli-norm threshold for diagonal matrix powering"

**Verdict: READY.** I found no mandatory fixes. Every check you asked for, and the spot checks on Appendices A–C, holds as written. All items listed below are optional.

I reviewed the text exactly as you pasted it. I had no shell or hashing tool in this session, so I could not confirm the SHA-256 (`17461fd7…2dc2`). I made no edits and contacted no one.

---

## 1. Corollary 3.1 and Appendix D (the remainder sampler)

**Finding the basis and the factor-two cover**
- **Cover problem:** In the conflict graph, two labels are joined when they anticommute. The identity label never conflicts with anything. A deletion leaves a commuting list exactly when it is a vertex cover, so the minimum cover weight equals β\*.
- **Bar-Yehuda–Even step:** Every edge charge falls on at least one vertex of any cover, and a vertex's charges sum to at most its weight. So any cover costs at least the sum of the charges. The chosen vertices are tight, which bounds their cost by twice that sum. This step is correct.
- **Clifford step:** Once the independent generators are mapped to single-qubit Z's, every element of the group they generate is a Z-type string with a ± sign. Conjugation only changes signs, so the coefficients stay real.
- **Off-diagonal weight:** Off-diagonal terms can only come from cover labels, so β ≤ 2β\* ≤ 1/2 and w = 1+β ≤ 3/2. That is exactly the range Theorem 3's filter allows.
- **Diagonal bound:** |d(x)| = |A_xx| ≤ 1 because A is a contraction.

**Endpoint sampling**
- The affine support set's direction contains V, because flip masks commute with the diagonal stabilizers. Both have dimension t, so they are equal.
- ρ has modulus 1 on the support and is 0 when x⊕y ∉ V. This is consistent with ψ(y) = 0 off the support.

**Unbiasedness**
- Σ_x |ψ(x)|² a(x) ρ(x,y(x)) = ⟨ψ|W|ψ⟩ with |ψ⟩ = U|j⟩.
- A D-step contributes w · (1/w) · d = D, so w^k 𝔼Z_k = ⟨j|U†A^kU|j⟩ = (B^k)_jj.
- |Z_k| ≤ 1.

**Error and confidence**
- Error: filter bias 1/128 plus sampling error 1/64 gives 3/128 < 1/32.
- Failure probability: 1/6 + 1/12 = 1/4, so success is at least 3/4.

**Runtime**
- ln w ≤ ln(1+2β\*), and the bound W ≤ 2·5^D increases with w.
- Since m ln(1+2β\*) ≤ 2mβ\*, the condition mβ\* = O(log²L) gives exp(O(log L)), which is polynomial.

**Arithmetic**
- Each d(x) is a signed sum of input coefficients, so it has at most F fractional bits.
- A product of at most m factors therefore has denominator 2^{mF}, which is polynomial in size.

## 2. The growing family

| Quantity | My calculation | Manuscript |
|---|---|---|
| Σp_i | (n² + n(n+1) − n)/(2n²) = 1 | 1 ✓ |
| Coefficients of H_T | identity 7/8; T₀: 1/8; T_i and T₀T_i: ±p_i/8 | ✓ |
| λ(H_T), λ(B) | 7/8 + 1/8 + 2·(1/8) = 5/4. The identity coefficient is 7/8 in both summands, so λ(B) = 5/4 | ✓ |
| Spectrum | I/2 ≤ H_T ≤ I, so I/2 ≤ B ≤ I | ✓ |
| L | 4n+3 labels × (n+1) letters, plus unary m = n², plus O(nℓ) coefficient bits, so L = Θ(n²) | ✓ |
| β₀ (removing the Z terms) | η(1/8 + 1/8 + 1/8) = 3αη/4 = 3ℓ²/(8n²) | ✓ |
| Cheapest X term vs. 2β₀ | (1−η)/(16n) vs. 3ℓ²/(4n²). It wins once n(1−η) > 12ℓ², i.e. **ℓ ≥ 11** | "eventually" ✓ |
| Optimal and 2-approximate covers | Any cover containing an X term costs more than 2β₀. With no X term, every Z term must be in the cover, because each one anticommutes with a single-site X. So the cover is unique and β\* = β₀ | ✓ |
| mβ\* | 3ℓ²/8. Since log L = Θ(ℓ), this is Θ(log²L) | ✓ |
| Fixed vector | \|+⟩₀\|0ⁿ⟩ is killed by K_X (via the selector) and by K_Z (since Σp_i = 1). Its squared overlap with j is 1/2, and positivity gives B^m_jj ≥ 1/2 | ✓ |
| D₀ | ‖D₀‖ = 1 − η + η(7/8) = 1 − η/8, so (D₀^m)_jj ≤ e^{−ℓ²/8}. The gap is ≥ 1/2 − o(1) | ✓ |
| Remainder sampler on this family | sqrt(m ln w) = O(ℓ), giving exp(O(ℓ)) = poly(n) | consistent ✓ |
| Coefficient lower bound | A = n² ln(5/4) ≥ 2, so W ≥ 2^{Ω(n)} = 2^{Ω(√m)} = 2^{Ω(√L)} | ✓ |

**Norm and row-sum inequalities**
- **H_X rows:** All flip masks are distinct, so every row's absolute sum equals λ(H_X) = 5/4.
- **B − H_X:** ‖B − H_X‖_∞ ≤ η(1 + 5/4) = 9η/4, using ‖H_Z‖_∞ ≤ 1. Also ‖B‖_∞ ≤ (1−η)(5/4) + η ≤ 5/4.
- **I − 2αK_X:** The identity coefficient is 3/4 and the other terms total 2α · 3/4 = 3/4, so each row sums to 3/2 = 1+α. Also ‖K_X‖_∞ = (1+1+1+1)/4 = 1.
- **H_X²:** By the reverse triangle inequality, each row sum is at least 1 + α − α² = 5/4.
- **B² − H_X²:** ‖B² − H_X²‖_∞ ≤ (5/4 + 5/4)(9η/4).
- **Rows of C:** The row sum is at least 5/4 − 45η/8 ≥ 9/8 once η ≤ 1/45, which holds for ℓ ≥ 6.
- **Returning-path bound:** C is symmetric, and u = n²/h is even. This gives (C^u)_jj ≥ 2^{−(n+1)}(9/8)^{n²/h}. The variance is then at least (𝔼|Z|)² − 1 = exp(Ω(m)) = exp(Ω(L)). ✓

## 3. Cap-only hardness remark and membership

- **Parameters:** d = 1/4 satisfies d ≤ min(1/2, c−1) = 1/4. Then s = 1/(8M) and m = 3M²/s = 24M³. ✓
- **Deletion weight:** A = (W+W†)/2 has trace zero, so its identity coefficient is 0. The non-identity weight is therefore (1−τ)·s·λ(A′) ≤ (1−τ)·d. Rounding toward zero only lowers this. Deleting those terms leaves a multiple of the identity, so β\* ≤ 1/4. ✓
- **λ(A) ≤ 2M:**
  - Each transition is a tensor product of one-bit matrix units, giving M terms of weight 1/M each.
  - The gate weights are: H √2, T cos(π/8)+sin(π/8) ≈ 1.307, CNOT 2, −Z 1.
- **Margins (in units of 1/1536):**
  - YES: 496 − 9 = 487, against the threshold 9/32 = 432.
  - NO: 272 + 6 + 9 = 287, against the threshold 7/32 = 336.
  - The distances from 1/4 = 384 are 55 and 49, and the tolerance is 1/32 = 48. Both inequalities hold strictly, though the NO side clears by only 1/1536.
- **Remainder term:**
  - The chord bound gives cos(π/M) ≤ 1 − 2/M².
  - Raising to the power m gives at most e^{−6} ≈ 0.00248, which is below 1/256.
  - The rounding perturbation is (3/2)·m·τ ≤ 3/512.
  - Compilation adds 2·(1/96) = 1/48.
- **Membership on every promised input:** |b_P| = 2^{−n}|Tr(PB)| ≤ ‖B‖ ≤ 1, so λ(B) is at most the number of listed terms, which is at most L. The Trotter bound u²λ²/(2k) is then polynomial. Phase estimation needs only ‖B‖ ≤ 1, and the β\* promise is never used. ✓
- **Consistency with Corollary 3.1:** The hard instances have m = 24M³ and β\* up to 1/4. Corollary 3.1 would then take exp(Θ(M^{3/2})) time, so there is no contradiction.

## 4. Other checks that passed

- **Theorem 3, upper bound:**
  - q ≤ 2A/ln 2, because b ln λ > ln 2 · b/(b+1) ≥ ln 2/2.
  - Truncation loses 2e^{−6} < 1/128.
  - W₂(T_k) ≤ 5^k, since 21·5^{k−1} ≤ 25·5^{k−1}.
  - Error 12/512 + 1/512 = 13/512.
- **Theorem 3, converse:**
  - The truncation tail is ≤ 1/256.
  - The rise of g is > 0.632 − 0.078 > 1/2.
  - 2/17 ≥ 1/9.
- **Spectral weight:** π₀ = 1/2. Σq_i^{−1} = 4T² − 2T + 2 ≤ 4T², and with the grounded edge 4T² + 2T ≤ 6T². The cyclic overlap sqrt(D/M)·⟨v|z⟩ gives weight p/2.
- **Corollary 4:**
  - Rank sums are 16 and 12, so μ ≤ 4(N−1)/64 + 3/16. The stated 7/64 bound is weaker but valid.
  - (N−13)/32 ≥ N/64 when N ≥ 26.
  - 9/40 ≥ 3/16.
- **Theorem 6:**
  - 2¹¹ ≡ 39 and 2²¹ ≡ 1 (mod 49), so n = 42.
  - J = 7N − 10 = 49n − 10 = 2^a.
  - η = τ/(2¹⁹J) and F = τ^{−1} − 1.
  - The XOR masks (2,1) and (5,1) do not match any competing rule.
  - m at n = 42 equals 144 · 2¹⁹ · 21965² = 36,424,602,825,523,200 ✓.
- **Theorem 5:**
  - The Hadamards inside U are at t = 28, 82, 136.
  - γ = (3(√2−1) − 1)/162 > 0.
  - τ/s ≤ 1/(9216T²).

## 5. Optional observations

1. **Make "eventually" explicit in the Appendix D family.** ℓ ≥ 11 is enough for the cover separation. It also covers the η ≤ 1/45 needed for the row sums.
2. **"Superpolynomial bounds" for the Pauli sampler.** On the Appendix D family, the claim is a lower bound on the prescribed coefficient budget, not on the Pauli trial's actual variance. The Appendix B variance argument doesn't carry over here, because the Z-type weight is d_Z(B) = 7/8 + 3η/8 < 1. It would help to say this in the sentence after Corollary 3.1.
3. **"Exponential" in the abstract (Theorem 5).** The variance is exp(Ω(T²)), and m = Θ(T³), so it is exp(Ω(L^{2/3})) in the input length. Consider "exponential in the clock length" or "superpolynomial."
4. **"Weight cap alone" in the abstract.** The phrase could be read as the λ cap. Write "the deletion-weight cap β\* ≤ 1/4," as the paragraph heading already does.
5. **Overloaded symbols.**
   - W: clock unitary and weighted mass.
   - A: clock Hermitian, m ln λ, UBU†, the entrywise |C|, and a flag.
   - D: idle length, truncation degree, round length, diagonal part, and event.
   - η: grid spacing and mixing weight.
   - ℓ: truncation degree, log n, and 162.
   - M: clock size and trial counts.
   - T: time, Chebyshev polynomial, and Pauli letter.
   - K: weight bound and K_T.
   - p: acceptance probability, p_i, and Pauli exponent.

   Appendix D is where this is most confusing, because "D step," the diagonal D and the Chebyshev degree D all appear together.
6. **The algorithm can certify itself.** It computes β ≤ 2β\*, so β > 1/2 proves β\* > 1/4. A one-line remark could note that the algorithm never needs β\*, which is hard to compute.
7. **Mixed corollary numbering.** The sequence runs Corollary 2, Theorem 3, Corollary 3.1, Corollary 4. Consider checking whether that is intended.
8. **Theorem 3 truncation tail.** The tail is actually ≤ 1/256. The stated 1/128 is valid, just loose.
