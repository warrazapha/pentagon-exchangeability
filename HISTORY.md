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
