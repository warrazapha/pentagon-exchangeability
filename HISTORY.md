# History: corrections, failed approaches, open items

Kept as a record. Dated 2026-10-16/17 unless noted. "CG" = ChatGPT.

## Corrections made along the way
- "GL(3,2) acts simply transitively on the 7 split spans' data" was wrong (an AI-written claim, caught in review): it is transitive with stabilizer of order 24. Fixed in the 144-count derivation.
- The proof of F3 (rank <= 2 gives alpha = +1) was incomplete (anticommutation and squares alone do not give the quaternion table); fixed by using alternativity of the unit loop and an explicit table.
- F2 (a(bc) = -(ab)c for independent octonion units) depended on an external note; reproved inline.
- A "one checks" step in Lemma 2 (five-point frame) was replaced by an explicit reduction.
- The reason the zero top-bit pattern is excluded at rank 3 was misstated; it is excluded only because the span is not the low half.
- Edge-1 / edge-3 labels of the q-vectors had been swapped in one draft; corrected.
- Script header claimed Python 3.8; it needs 3.10+.
- Early MathOverflow draft said the five q_i equal (5,9,10,13,11) for every quadruple. That holds only for independent (a,b,c,d), written in the basis a,b,c,d with a,b,c,d read as bits 1,2,4,8 (reading them as 8,4,2,1 gives 10,9,5,11,13). The write-up now states the vectors explicitly.
- An AI "review" suggested the sedenion formula looked new; this is not accepted (absence of search hits is not evidence of novelty).

## Approaches that did not work / were not enough
- Pentagon parity alone (delta^2 sigma = 1): holds for random sigma, no uniformity.
- Symmetry of sigma itself: not the relevant property; the relevant objects are symmetries of alpha.
- Suggestion to count by GL(4,2) orbits of tuples: alpha is not GL(4,2)-invariant (the sedenion formula singles out an index and a bit); the counts instead come from the S_5 symmetry of the five-vector frame.
- (Suggested by an AI review, 2026-10-17, and then made exact:) the size of the guaranteed-symmetry group under one condition: order 2, versus 24 for both (THEOREM.md section 6a).
- Single conditions: left alternativity only, right only, alpha(x,y,x)=1 only, alpha(x,y,x+y)=1 only: no uniformity (the last gives the dihedral classes: adjacent edges equal, non-adjacent edges equal, not all equal).
- Comparing with Bales' closed sign function (arXiv:1602.02317): it belongs to a different product, not a convention for the sedenions; its census differs. Whether the paper was withdrawn: the arXiv abstract page and PDF (via fetch extracts) show no withdrawal note; the retraction was reported secondhand and is unconfirmed.

## Tool failures
- arXiv:2505.11747: first fetches returned HTTP 429; later fetches succeeded (extracts only).
- Search tool with domain restriction to mathoverflow.net returned HTTP 400; MathOverflow, MathStackExchange and Quora were not searchable directly.
- MathOverflow's AI policy could not be found by search.

## Open items
- Independent review of the three critical steps (THEOREM.md, section 3).
- Whether left and right alternativity of the standard Cayley-Dickson basis signs holds for every n (checked n = 3,4,5).
- Necessity / weaker conditions; an intrinsic (associahedral, matroidal or cohomological) explanation of the S_5 action.
- Literature: unread bodies of several sources (Kirshtein in full, Bales 1707.07318, Schafer, Imaeda); other Bales doubling products; comparison of d(F_S) from Hu-Huang-Zhang with our alpha.
- Dimension 32 is covered by the theorem only if the hypotheses hold there (they do for the standard product, checked).

---

## Addendum, 2026-10-17 (later the same day; earlier entries above are left as written)

### Open items resolved
- "Whether (L) and (R) hold for every n": they do, and this is known for the standard loop (Kinyon-Phillips-Vojtechovsky, arXiv:math/0412390, section 7). We also have an induction proof (THEOREM.md section 10), checked n = 1..7, and the alternate product checked to n = 6.
- "Necessity / weaker conditions": exchangeability of the aggregate edge law is equivalent to (L)+(R) (THEOREM.md section 9), by a Gram-matrix sum-of-squares identity.

### Corrections
- Alternate-product induction sketch (a ChatGPT draft): the second component for (R) with w = (0,s) was written as (q-bar s)s = q using (R). The correct identity is s(s-bar q) = q, which uses (L). The conclusion is unchanged.
- ChatGPT's order-24 argument skipped the step for z -> z+q (obtained from y -> y+q by conjugating with the swap). Its transfer of the 672/672 counts across classes was unproven, though enumeration confirms the result.
- A note of mine asserted that the five means are equal without justification. The justification (each edge map G^4 -> G^3 is a surjective linear map with equal fibres) came from ChatGPT, and the note was updated.
- Misattribution: a commentary described a "seven-plane decomposition, 512-case certificate" as being in an attached file; it was not. I flagged it and re-derived the plane certificate (the rank-2 converse) myself.
- Wrong conjecture: that the aggregate S35 - S15 is >= 0 (supported by n = 3 only) was refuted at n = 5 (minimum -6240). The note keeps the original text struck through.
- The MathOverflow question read as if (L),(R) on Cayley-Dickson units were a finding. They are known (Kinyon-Phillips-Vojtechovsky); the question was edited to say so.
- `cd_LR_induction_check.py` printed "table matches full product (n<=4): False" for n >= 5, which only meant "not cross-checked at that size". The label was changed.

### Approaches that did not work (superseded by the Gram proof; not wrong in what they claimed)
- Positivity of a single pair-correlation difference (T35 - T15 >= 0): false at n = 5, and per cochain at n = 4 (three explicit witnesses).
- Autocorrelation reformulation: the bridge to a positivity argument is blocked, since the pair subspaces have rank 4.
- Rank-stratified sums: the rank-2 converse holds (plane certificate, 512 cases), but the rank-3 and rank-4 sums are not sign-definite.
- Pentagram-minus-pentagon: non-negative at rank 2 and (heuristically) 3, fails at rank 4 and in aggregate at n = 5.
- Sampled LP/adversarial searches for a separating functional (n = 3): no hull obstruction found; not used in any proof.

### Literature (round 5)
- Known: (L),(R) for the Cayley-Dickson sign loop (KPV section 7, citing their Lemma 6.2(vii)); loops with involution (arXiv:2501.00123).
- Related, not read in full: Albuquerque-Elduque-Perez-Izquierdo 2001; Albuquerque-Majid.
- Not found: the pentagon statement, the Gram argument, the necessity theorem. Weak evidence only.
- Fetches returned summaries, so statements are "per excerpt".

### Open items
- Independent human review of the three critical steps in THEOREM.md section 3 and of Theorem 9.1.
- An intrinsic (associahedral, matroidal or cohomological) reason for P = Q = R = W.
- Full reading of KPV sections 6-7, arXiv:2501.00123 sections 9-10, AEP 2001 section 3; Culbert, Cawagas, Kivunge-Smith; Bales 1707.07318; Schafer; Imaeda.

