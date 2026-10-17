# Literature audit, round 4: leads from the MathOverflow assistant paste (2026-10-16)

Status: fetch extracts only (a small model summarised each page); not read in full. Related-work notes, no priority or novelty claim.

## Wilmot, arXiv:2505.11747, "Structure of the Cayley-Dickson algebras" (body now seen via fetch extract)
- XOR indexing of basis elements; associator [a,b,c]=(ab)c-a(bc); triple associator T(b,c,d).
- Thm 2 (24 permutations of a triad product fall into three associativity types), Thm 3 (two distinct blades generate a quaternion subalgebra), Thm 4 (non-associative triad: T=+-2a, a=bcd), Thm 5, Thm 6 (Moufang identities vs types), Thm 7 (only 8 of 64 three-triad cycle silos exist), Thm 8 (counts of quasi-octonion subalgebras, divisible by seven), Thm 9 (projection onto H, O, P4, P12, P14).
- Per the extract: no closed-form associator sign formula, no four-fold bracketing or pentagon counts. Related: classification of triads (our rank-3 / span types; compare Thm 8 with Cawagas' 8 + 7 maximal subloops).
- To do: read Thm 4, 5, 8 in full and compare with our triple formula.

## Codidact answer (math.codidact.com/posts/292189), author "r~~", Aug 2024
- Closed form for the sign function sigma(m,n) for the ALTERNATE product (a,b)(c,d)=(ac-b*d, da*+bc) in a "shuffle basis" (bit-reversed index); cites "An alternate Cayley-Dickson product" (Bales, arXiv:1602.02317). Says the standard product makes a closed sigma hard.
- Nothing on the associator (per the extract). Our result is about alpha for the standard product; the bit-reversal relabeling confirms the shuffle basis puts the doubling bit at the bottom.
- To do: check whether alpha = d(sigma) for Bales' closed sigma gives our formula (convention differs; Prop 1' covers only the opposite algebra, not this product).

## MathOverflow assistant's "F4 commu-associator" quote
- Not found in Wilmot. Source article unidentified; ask the user for the link in the MO "prior posts" panel.

## Addendum: comparison with Bales' alternate product (checked by me, 2026-10-16)
Status: Checked (computation). Scripts: scratchpad alt_check.py, rand_check.py (to be copied to engine/).
- Alternate product implemented from the recursion (a,b)(c,d)=(ac-b*d, da*+bc) (taken from the Codidact extract; not confirmed to be exactly Bales' P2 in the paper), all 256 pair signs +-e_{x^y}.
- alpha=d(sigma). Standard (ours): 2248 positive / 1848 negative triples; no-flip 15136, two-flip 2688 x10, four-flip 4704 x5. Alternate: 3016 / 1080; 26656; 3456 x10; 864 x5. Reproduces the figures in the pasted report.
- 1440 triples differ with the shuffle (bit-reversed) labelling, 1344 with the standard labelling: the count of disagreements depends on labelling, the census does not (bit reversal is linear and preserves the pentagon structure). alpha(1,2,4): -1 (ours), +1 (alternate, either labelling).
- The alternate product has octonion-stage zero divisors: (e1+e4)(e2-e7)=0 in my implementation (standard control: none found in that search). So it is not a Cayley-Dickson doubling in the usual sense, consistent with the report.
- NOT verified: the claimed retraction. arXiv abs page (v3, 2020-01-11) and the PDF, per fetch extracts, show no withdrawal note and call P2 a doubling product. The retraction and Bales' corrected MO answer come from the pasted report only; check sources before citing.
- Random sign cochains (sigma(x,0)=sigma(0,x)=1, otherwise random): pentagon parity always holds (only 0/2/4 flips), but the counts per pattern are NOT uniform. So the uniformity is a real property shared by both products, not automatic. Open: what property of sigma gives it.
