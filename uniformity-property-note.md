# Which property of sigma gives uniform pentagon counts? (2026-10-16)

Status: Checked (computation, sampling); Interpretation/Open (no proof). Scripts: engine/uniformity_probe.py, engine/uniformity_probe_dep.py.

Setup. sigma: normalized sign cochain on F_2^4 (sigma(0,.)=sigma(.,0)=1; 225 free bits), alpha = delta sigma, pentagon edges T1..T5 as in the consolidated note. "Uniform" = all 10 two-flip patterns have one common count and all 5 four-flip patterns have one common count.

Findings (all computed; the constraint sets are linear over F_2 in the bits of sigma, so they were solved exactly and random solutions were sampled).
1. Pentagon parity (0, 2 or 4 flips) holds for every sigma. Not the explanation.
2. Unconstrained random sigma: never uniform.
3. Constraint "alpha(x,x,z)=+1 for all x,z" alone (left alternative): never uniform in 5 samples. Same for "alpha(x,z,z)=+1" alone (right), "alpha(x,y,x)=+1" alone, and "alpha(x,y,x+y)=+1" alone (partly structured: two distinct two-flip counts).
4. Constraint "left and right together" has the same solution space as "alpha=+1 on every dependent triple" (both give constraint rank 175, joint rank 175, solution space dimension 50 in sigma, i.e. 35 after removing the 15-dimensional space of coboundaries d(beta), which do not change alpha). In 60 random samples from that space (plus 4+4 earlier): 0 non-uniform, 42 distinct count triples (no-flip, two-flip, four-flip), so the counts themselves vary; only the uniformity is constant.
5. Both the sedenion convention and the alternate (Bales-type) product satisfy the condition (alpha=+1 on dependent triples) and are uniform; the counts differ (15136/2688/4704 vs 26656/3456/864).

Conclusion (conjecture, supported by sampling only). Uniformity appears to follow exactly from alternativity of the loop of units, F0 in the proof note (alpha(x,x,z)=alpha(x,z,z)=+1, equivalently alpha trivial on dependent triples). It needs both the left and right identities; neither alone suffices. Not shown: that it is necessary (only that the tested weaker conditions fail) and that it is sufficient (60 samples out of 2^35 alpha functions).

Suggested proof route (not carried out). Under the condition alpha is supported on independent triples. Rank-3 tuples: classify the possible alpha restricted to a 3-dimensional span V (finite). Rank-4 tuples: edges become five triples in a 4-space related by the five-point frame; the cocycle identity ties them together. Then show the pattern counts are symmetric under S5 acting on the frame. Also test n=5 (Z_2^5) for the same behavior.

## Addendum: moment formulation (CG's, checked by me)
Status: Checked (arithmetic and computation); the reduction in point 3 is mine and elementary.
1. Let X_i = alpha(T_i) = +-1. Pentagon parity gives X_1...X_5 = 1, so every product of edge signs equals the product of the complementary set; the distribution on the 16 even words is determined by the 5 means E[X_i] and 10 pair correlations E[X_iX_j]. Uniformity (counts depend only on |F|) is equivalent to: all means equal and all pair correlations equal. (A reformulation, not an explanation.)
2. Values, rechecked from the census and by direct summation: sedenion E[X_i] = 25/256, E[X_iX_j] = 113/512; alternate product 121/256 and 161/512.
3. The means are equal for EVERY sigma: each map (a,b,c,d) -> T_i is uniformly distributed over triples (a bijective change of variables on the free letters), so E[X_i] = average of (-1)^A over all 4096 triples. Checked on random sigma (means identical across edges). So the whole question is the ten pair correlations. For random sigma they are far from equal (e.g. sums 12160 for (3,5) vs 2080 for (4,5) out of 65536); under "alpha = +1 on dependent triples" they come out equal in every sample tested.
Script: engine/corr_check.py.

## Addendum 2: the ten pair correlations as explicit sums, and which conditions identify which (2026-10-16)
Status: Checked (explicit sums verified against brute force on a random sigma; equalities are "equal in all 14 random samples per family", exact integers, not proofs). Scripts: engine/pairs_check.py (formulas), engine/pairs_classes.py (families).

Notation. X = (-1)^A = alpha on F_2^4 triples. L(y,z) = sum_x X(x,y,z), R(x,y) = sum_z X(x,y,z). C_ij = sum over all (a,b,c,d) of X(T_i)X(T_j). Summing out a free letter gives:
- C12 = sum_{x,y,z} X(x,y,z) R(x, y+z)
- C13 = sum_{y,z} L(y,z) R(y,z)
- C14 = sum_{x,y} R(x,y)^2
- C15 = sum_{x,y,z} X(x,y,z) R(x+y, z)
- C23 = sum_{b,c,d} X(b,c,d) L(b+c, d)
- C34 = sum_{b,c,d} X(b,c,d) L(b, c+d)
- C35 = sum_{y,z} L(y,z)^2
- C24 = sum_{a,u,w,c} X(a,u,w+c) X(a,u+c,w)   (no letter can be summed out)
- C25 = sum X(a,b+c,d) X(a+b,c,d)             (4-sum)
- C45 = sum X(a,b,c+d) X(a+b,c,d)             (4-sum)
Edge order T1..T5 is the cyclic order around the pentagon (adjacent edges share a vertex): pairs 12,23,34,45,15 adjacent; 13,14,24,25,35 non-adjacent.

Which equalities hold in every sample (14 samples each):
- Unconstrained, and "alpha(x,y,x)=1" alone: none.
- alpha(x,x,z)=1 (left): {13,15}, {23,25,35}, {34,45}; singles 12, 14, 24.
- alpha(x,z,z)=1 (right): {12,14,24}, {13,34}, {15,45}; singles 23, 25, 35.
- alpha(x,y,x+y)=1 alone: exactly two classes, the adjacent pairs {12,23,34,45,15} and the non-adjacent pairs {13,14,24,25,35}. The pentagon's dihedral symmetry appears from this one condition.
- Left and right together (= alpha trivial on dependent triples): all ten equal. (The left and right classes overlap enough to chain together; with alpha(x,y,x+y)=1 contained in the condition, adjacent = non-adjacent also follows.)
Consistency check (reversal). Reversing (a,b,c,d) -> (d,c,b,a) maps the edge triples to the reverses of T3, T2, T1, T5, T4 respectively, so it acts on edge labels as 1<->3, 4<->5, 2 fixed, and sends alpha(x,y,z) to alpha(z,y,x), i.e. left <-> right. Applying that relabelling to the left classes gives exactly the right classes ({13,15} -> {13,34}, {23,25,35} -> {12,24,14}, {34,45} -> {15,45}; singles 12,14,24 -> 23,35,25). Checked by hand against the computed classes; not used in any argument.

## Addendum 3: a proof of uniformity from left + right alternativity (2026-10-17)
Status: **Proof** (mine, by hand; each step also checked by computation; not reviewed by a mathematician). Scripts: engine/uniformity_proof_check.py, engine/sym_probe.py, engine/dim32_check.py.

Theorem. Let sigma be a normalized sign cochain on F_2^n (sigma(0,.)=sigma(.,0)=1), alpha = d sigma, X = alpha viewed as +-1. Assume (L) X(x,x,z)=1 and (R) X(x,z,z)=1 for all x,z. Let (a,b,c,d) range over all 2^{4n} quadruples and X_i = X(T_i) with T_1=(a,b,c), T_2=(a,b+c,d), T_3=(b,c,d), T_4=(a,b,c+d), T_5=(a+b,c,d). Then the joint distribution of (X_1,...,X_5) is invariant under all permutations of the five coordinates. In particular, the counts depend only on |F|. (n=4 gives the 10 + 5 uniformity.)

Proof.
Step 0 (facts for any normalized sigma). X(x,y,z)=1 if some argument is 0, and the pentagon identity P(a,b,c,d): X(a,b,c) X(a,b+c,d) X(b,c,d) X(a,b,c+d) X(a+b,c,d) = 1 holds for all a,b,c,d.
Step 1 (three substitution symmetries). Put d=c in P and use (R) (X(b,c,c)=X(a+b,c,c)=1) and X(a,b,0)=1: X(a,b,c)=X(a,b+c,c). [s2: y -> y+z]
Put b=a in P and use (L) (X(a,a,c)=X(a,a,c+d)=1) and X(0,c,d)=1: X(a,a+c,d)=X(a,c,d). [s1: y -> y+x]
Put c=b in P and use (R), (L) (X(a,b,b)=X(b,b,d)=1) and X(a,0,d)=1: X(a,b,b+d)=X(a+b,b,d), i.e. X(x,y,z)=X(x+y,y,y+z). [t3]
These hold for every triple, dependent or not.
Step 2 (the group). The substitutions s1, s2, t3 act on ordered triples through 3x3 matrices over F_2. By direct enumeration (closure under composition) they generate a group of order 24, equal to S = {M in GL_3(F_2): row 1 + row 3 = (1,0,1)}, the matrices preserving x+z. So X(M t) = X(t) for every M in S and every triple t. Consequence: for independent x,y,z, alpha(x,y,z) depends only on the span V and on x+z.
Step 3 (the five-vector frame, in coefficient space F_2^4 with coordinates a,b,c,d). q_i = first + third of T_i: q = (a+c, a+d, b+d, a+c+d, a+b+d), summing to 0, any four independent. Let H_i be the span of the three coefficient vectors of T_i (a hyperplane). Then q_i is in H_i and q_j is not in H_i for j != i (checked), and H_i is the only hyperplane containing q_i and none of the other q_j (a functional is determined by its values on four independent vectors). For each pi in S_5 there is psi_pi in GL_4(F_2) with psi_pi(q_i)=q_pi(i); it sends H_i to H_pi(i) by the uniqueness just stated.
Step 4 (exchangeability). A quadruple is a linear map phi: F_2^4 -> F_2^n (a,b,c,d = images of the coordinate vectors); phi -> phi psi_pi is a bijection of all quadruples. The triple T_i(phi psi_pi) is phi applied to the basis (psi u, psi v, psi w) of H_pi(i) obtained from T_i's basis (u,v,w). Both it and T_pi(i)'s basis (u',v',w') are bases of H_pi(i) with first+third = q_pi(i), so they differ by a matrix in S. By Step 2, X_i(phi psi_pi) = X_pi(i)(phi). Hence the law of (X_i) is invariant under pi. QED.

Checked: group order 24 and equality with S; q_i in H_i only; for a random sigma satisfying (L),(R), generators invariant on all 4096 triples; X_i(phi psi_pi) = X_pi(i)(phi) with 0 mismatches over all 120 permutations x 300 random quadruples x 5 edges, two random sigma.

What this explains / does not.
- Explains the uniformity of both the sedenion and the alternate products, why the five-vector frame appears (its automorphism group S_5 is what permutes the edges), and the earlier observation that alpha(x,y,z) depends on the span and x+z only.
- Only (L)+(R) are used; the earlier empirical classes for L alone or R alone correspond to using only s1 (or s2) in Step 1.
- Not shown: necessity of (L)+(R) (other conditions might also suffice).
- The argument never uses n=4. For the standard Cayley-Dickson product at n=5 (dimension 32) I checked (L) and (R) by computation and, separately, the census over all 32^4 = 1,048,576 quadruples: no flip 166,576; each of the 10 two-flip patterns 48,720; each of the 5 four-flip patterns 78,960 (total 1,048,576). That the unit loop is alternative for every n is not proved here (n=3,4,5 checked).

### Addendum 3b: clarifications after review (2026-10-17)
- The proof needs only invariance X(M t) = X(t) for every M in S and every triple t (Step 2 gives this because the three identities of Step 1 hold for all triples). It does not need a statement about orbits on dependent triples, and it does not use that alpha is trivial on dependent triples.
- Orbit statement, for the record. For independent triples the S-orbits are exactly the fibers of (span, x+z): fix a basis B of V; the bases of V are M B with M in GL_3(F_2), and x'+z' = (row1+row3).B equals x+z iff M is in S; so each fiber is one S-orbit, and S acts simply transitively on it (24 elements; 168/7 = 24). Hence alpha(x,y,z) = f(span, x+z) on independent triples. For dependent triples nothing is claimed or needed.
- Direction of the equivalence "left+right <=> alpha trivial on dependent triples": dependent-trivial implies (L),(R) because x=y and y=z are dependent cases (immediate). The converse is only computational so far (identical solution spaces, constraint rank 175); the theorem is stated with hypothesis (L)+(R), which is what the derivation uses.
- Step 1 derivation of the third identity, written out: in P(a,b,c,d) set c=b. Then b+c=0 and the five factors are X(a,b,b) X(a,0,d) X(b,b,d) X(a,b,b+d) X(a+b,b,d) = 1; the first three equal 1 by (R), normalization and (L), leaving X(a,b,b+d) = X(a+b,b,d). Substituting x=a, y=b, z=b+d (d = y+z) gives X(x,y,z) = X(x+y,y,y+z).

### Addendum 3c: the equivariance step as a stand-alone lemma (2026-10-17)
Lemma. Let pi be in S_5 and psi = psi_pi in GL_4(F_2) with psi(q_i) = q_pi(i). For every i let (u_i,v_i,w_i) be the coefficient vectors of T_i (so u_i + w_i = q_i), and set j = pi(i). Then (psi u_i, psi v_i, psi w_i) = M (u_j, v_j, w_j) for a unique M in GL_3(F_2) with M in S, i.e. row 1 + row 3 of M equals (1,0,1).
Proof. (1) Span: psi(H_i) = H_j (Step 3), so both triples are bases of H_j and M exists, unique and invertible. (2) First-plus-third: psi u_i + psi w_i = psi(q_i) = q_j = u_j + w_j. The left side equals (r_1 + r_3).(u_j,v_j,w_j), the right side equals (1,0,1).(u_j,v_j,w_j); since u_j,v_j,w_j are independent, r_1 + r_3 = (1,0,1). So M preserves x+z, which is the definition of S. QED.
Hence for every linear phi, T_i(phi psi) = M applied to T_j(phi), and X(M t) = X(t) gives X_i(phi psi) = X_j(phi). Both properties the review asked for (matching hyperplanes, preserving x+z) are exactly parts (1) and (2). This was already the content of Step 4; the lemma just isolates it. The computational check in uniformity_proof_check.py tests the conclusion directly (0 mismatches).
Status unchanged: hand proof, unreviewed by a mathematician. Agreement among AI systems (CG, me) is not evidence; no priority claim is made, and the result may already be known in the literature on Cayley-Dickson loops or twisted group algebras (not searched for).
