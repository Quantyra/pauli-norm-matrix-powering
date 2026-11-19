# Claude review of v1.3.0

Automated manuscript review. [Editorial disposition](disposition.md)

## Initial revision

[Reviewed source](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/71399c1702bca8920be642bac58dc2c49711c726/manuscript.tex), SHA-256 `c8d0b936d6d66428fa6eee1f3717cae6abba0978b5cc486610ddaf52a442f976`.

## Referee Report

**Verdict: REVISE** (no mathematical error found in the new results; four items need repair before acceptance)

### Checks performed
I re-derived the new material independently. **Theorem 3, part 1:** `b ≥ 1` holds (λ ≤ 3/2 < 2); `q ≤ 2A/ln 2` follows from `b+1 ≤ 2b`; `y^q = E T_{|S_q|}(y)` via `E e^{iθS_q} = cos^q θ`; Hoeffding truncation at `D = min(q,⌈√(12q)⌉)` gives tail `2e^{-6} < 1/128`; `W_λ(x^r p(x^b)) = λ^r W_{λ^b}(p)` is exact (distinct degrees `r+bk`, no collection loss); the recurrence gives `W_2(T_{k+1}) ≤ 4W_2(T_k)+W_2(T_{k-1}) ≤ 21·5^{k-1} ≤ 5^{k+1}`, so `W ≤ 2·5^D = exp(O(√(1+A)))`. Estimator mean is `f(B)_{jj}`, scores lie in `{0,±W}`, Chebyshev with `M = ⌈6·64²W²⌉` gives failure 1/6; binary rejection (acceptance ≥ 1/2, cap `⌈log₂ 12M(m+1)⌉+1`) costs ≤ 1/24 over ≤ `M(m+1)` draws, inside the stated 1/12; error `1/128+1/64+1/512 = 13/512`, success 3/4. Tables are exactly dyadic (`a_k` over `2^q`, `λ^k` with `m ≤ L` bits), space polynomial, counters `O(√L)` bits. Since `A ≤ m ln(3/2) = O(L)`, all non-exponential costs are genuinely poly. **Part 2:** `Σ|d_j|h^j ≤ W_λ(f)`, tail `≤ 2^{-(ℓ+1)}W ≤ 1/256`, `‖g‖_{∞,I} ≤ 133/128 ≤ 17/16`, rise `> 1-e^{-1}-10/128 > 1/2` over `1/m`, Markov on `|I| = h/2` gives `ℓ² ≥ 2mh/17 ≥ A/9`; bound correct. **Corollary 4:** `ms = 36T²`, `2τ ≤ 1/(128m) = s/(4608T²) ≤ sN/128`, `(N-13)/32 ≥ N/64` at `N ≥ 26`, `(3/16)NT² ≤ m ln λ ≤ 36KT²`, hence `M = exp(Θ(T√N))` — superpolynomial on the chain images, consistent with Corollary 2's hardness and with `A = Θ(L) ≫ log²L`. Theorem 1's arithmetic also recheck: `487/1536 > 9/32`, `287/1536 < 7/32`, margin `55/1536 > 1/32`; clock spectrum, `p/2` weight, Hadamard norm invariance, rounding (`‖B-B_*‖ ≤ 3τ/2`, `3/512`) all hold; chain gap `1/(4T²+2T) ≥ 1/(6T²)` and `π_0 = 1/2` confirmed.

### Mandatory corrections
1. **Corollary 4, μ-bound is not robust.** `λ(H)-2μ = Ω(N)` needs `λ(H) ≥ ⌊N/2⌋/2 ≈ N/4` to beat `2μ ≤ R(N-1)/32`; this *fails at R = 8*. The constants "at most seven rewrite projectors of rank ≤ 4 per bond" and "rank one" end rules carry the whole claim and are asserted, not cited rule-by-rule. Supply an explicit table of installed terms with ranks and exact AGIK pointers, or obtain a norm lower bound with slack.
2. **Corollary 4, test word.** The bound uses `L_b F_left ↔ F_left R_b` on every displayed pair; justify that this transport rule is installed on `⌊N/2⌋` disjoint bonds of the *position-dependent* chain, including bond (1,2) after the `S R_b ↔ L_0 G_b` replacement.
3. **§2, λ > 1 extension.** "failure at most `2^{-L²}` per draw" is per-draw only; the run makes up to `λ^{2m}poly(L) = 2^{O(L)}` draws. Add the union bound (and note `λ ≤ c` keeps the count `2^{O(L)}`).
4. **Theorem 3 statement vs. endpoint policy.** The advertised accuracy `1/32` is precisely the value §1 declares insufficient at the promise endpoints. The proof delivers `13/512`, which *does* decide both endpoints against `1/4`; state `13/512` (or say the estimator decides) so Theorem 3 is not read as endpoint-ambiguous.

### Optional polish
"Matching exponential bounds" (abstract) overstates: `log₂W` is between `≈0.33√A - 8` and `≈13.7√A + 1`; write "matching up to the constant in the exponent." Make `N ≥ 26` explicit in Corollary 4's "sufficiently long." List the transitions `V_a` explicitly in §3 — "gates of `C†` in application order" is ambiguous (it is correct: `G_t†` first) — and record `D-2t-1 ≥ 0`. Note where `λ ≤ 3/2` rather than `< 2` is actually needed (only `h ≤ 1/2` in the converse). Give the crossover `N` for the final `16^N` comparison, which holds only for large `N` (roughly `N ≳ 200` with the stated constants). The truncation step proves `1/256` but quotes `1/128`; harmless slack worth flagging as such.

## Release candidate

[Reviewed source](https://github.com/Quantyra/pauli-norm-matrix-powering/blob/8708b50322448cb437c4764fa2c2260baffdbedc/manuscript.tex), SHA-256 `06fa0bb5acd7fcf55c99a9442009147e3e00bde2888a92a309cdaf90fab7b05e`.

## Referee Report (second round)

**Verdict: READY** — all four first-round mandatory items are repaired; no mathematical error found. Remaining notes are optional.

### Objections rechecked against this source
1. **μ-bound robustness (was mandatory).** Fixed. Corollary 4 now supplies the 13-row table with tag rewrites, placements, ranks, and a rule-level AGIK pointer. I verified the rank rule (orthogonal source/target tag sectors ⇒ rank = source data dimension; `tr[(J_in−J_outV)(·)^†/2] = r`), the per-bond totals (within-block 4+2+2+1+2+1+4 = 16; crossing 12), and the one-site terms (3 × 1/16 = 3/16). True per-bond normalized trace is 16/256 = 4/64, so the quoted 7/64 overcounts even the sum of *all* two-site ranks (22/256 < 28/256) — the bound is now robust to misclassified placement. With `⌊N/2⌋/2 ≥ 8(N−1)/32`, the margin `(N−13)/32` follows, and `(N−13)/32 ≥ N/64` exactly at `N ≥ 26`.
2. **Test word (was mandatory).** Fixed by replacing it: the alternating word `L_0,A,L_0,A,…` uses rule 3 (`LA↔AR`), which has both within-block and crossing versions, and bond 1 lost only rule 1 to the marked projector. Diagonal 1/2 per pair confirmed (`J_out` sector orthogonal to `⟨L_0A|`). Full-space use is legitimate since `λ(H) ≥ ‖H‖`.
3. **§2 union bound (was mandatory).** Fixed: cap `⌈log₂(12mM_0)⌉` over `mM_0` draws gives 1/12 total; `M_0 = ⌈48λ^{2m}/ε²⌉` yields 1/12 by Chebyshev.
4. **Endpoint policy (was mandatory).** Fixed: Theorem 3 now advertises `13/512` and states the 1/4 comparison decides endpoints (`131/512 > 128/512`, `125/512 < 128/512`).

Independently re-derived, unchanged results still hold: `b ≥ 1`, `q ≤ 2A/ln2`, `y^q = E T_{|S_q|}(y)`, tail `2e^{−6} < 1/128`, `W_2(T_k) ≤ 5^k` (21 ≤ 25), `W ≤ 2·5^D`, `M = ⌈6·64²W²⌉`, rejection cost ≤ 1/24, error 4/512+8/512+1/512, dyadic tables, `O(√L)` counters; converse `ℓ² ≥ 2mh/17 ≥ A/9`; `ms = 36T²`, `2τ ≤ s/(4608T²)`, `(3/16)NT² ≤ m lnλ ≤ 36KT²`, `M = exp(Θ(T√N))`; Theorem 1's `487/1536 > 432/1536`, `287/1536 < 336/1536`, `3τ/2`, `1/(4T²+2T) ≥ 1/(6T²)`, `π_0 = 1/2`, `q_0^{-1}+…= 4T²−2T+2 ≤ 4T²`.

### Mandatory corrections
None.

### Optional polish
Abstract now reads "matching up to constants in the exponent" — good. Still open: the converse truncation proves 1/256 but quotes 1/128 (flag as slack); no crossover `N` for the `16^N` comparison (≈200 with these constants; "on growing chains" is honest but vague); where `λ ≤ 3/2` beats `λ < 2` is unremarked (only `h ≤ 1/2`, fixing `I ⊂ [3/4,1]`); "thirteen symbols" means thirteen levels (8 bit-carrying + 5 single) — say so; rule 3's "every bond" placement is the one claim resting entirely on the AGIK citation, now harmless given the slack above.
