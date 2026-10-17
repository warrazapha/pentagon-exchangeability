# Alternative sign cochains and S_5-exchangeability of the pentagon of bracketings

Version 2026-10-17 (revised later the same day: sections 9-11 added). **Status: hand proof, supported by computation; not reviewed by a mathematician.** No claim of novelty or priority is made; the literature search was partial (sections 7 and 11). Developed with several AI systems (Claude, ChatGPT, Gemini, Grok) under the direction of the human author; agreement between AI systems is not treated as evidence. Everything below is meant to be checked.

## 1. Setting

Let G = F_2^n and let sigma: G x G -> {+1,-1} be *normalized*: sigma(0,y) = sigma(x,0) = 1. Think of the twisted group algebra with basis e_x and e_x e_y = sigma(x,y) e_{x+y} (for the Cayley-Dickson algebras this is the usual sign function on basis units). Define the associator sign alpha = delta sigma by

    (e_x e_y) e_z = alpha(x,y,z) e_x (e_y e_z),   alpha(x,y,z) = sigma(x,y) sigma(x+y,z) sigma(y,z) sigma(x,y+z).

Facts used (all immediate):
- (N) alpha(x,y,z) = 1 whenever x, y or z is 0.
- (P) Pentagon identity: for all a,b,c,d,
  alpha(a,b,c) alpha(a,b+c,d) alpha(b,c,d) alpha(a,b,c+d) alpha(a+b,c,d) = 1.
  Proof: compare ((e_a e_b) e_c) e_d with (e_a e_b)(e_c e_d) in two ways. Moving the brackets one step at a time gives ((ab)c)d = alpha(a,b,c) (a(bc))d = alpha(a,b,c) alpha(a,b+c,d) a((bc)d) = alpha(a,b,c) alpha(a,b+c,d) alpha(b,c,d) a(b(cd)) = alpha(a,b,c) alpha(a,b+c,d) alpha(b,c,d) alpha(a,b,c+d) (ab)(cd), while directly ((ab)c)d = alpha(a+b,c,d) (ab)(cd). All signs are +-1. (Equivalently delta^2 sigma = 1.)

Hypotheses (alternativity on basis elements):
- (L) alpha(x,x,z) = 1 for all x,z.
- (R) alpha(x,z,z) = 1 for all x,z.

These are conditions on the signs of *basis units* only. They do not say the algebra is alternative: the sedenion algebra is not alternative (it is flexible and power-associative), but its basis-unit signs satisfy (L),(R) ((L) and (R) are the left and right alternative laws of the unit loop; this is known for the standard Cayley-Dickson loop, see section 10).

Pentagon edges. For a quadruple (a,b,c,d) in G^4 put T_1=(a,b,c), T_2=(a,b+c,d), T_3=(b,c,d), T_4=(a,b,c+d), T_5=(a+b,c,d) and X_i = alpha(T_i) in {+-1}. By (P), X_1...X_5 = 1, so the set F of i with X_i = -1 has size 0, 2 or 4.

## 2. Theorem

If sigma satisfies (L) and (R), then for every n the joint law of (X_1,...,X_5), over the uniform distribution on all 2^{4n} quadruples, is invariant under all 120 permutations of the five coordinates. Equivalently: all C(5,2) = 10 two-element patterns F occur equally often, and all 5 four-element patterns occur equally often.

It is an exchangeability statement; it does not give the individual counts. The converse (exchangeability of the aggregate law implies (L) and (R)) is Theorem 9.1 below.

## 3. Proof

**Step 1: three substitution symmetries (valid for all triples).** Substitute in (P):
- d = c: the factors alpha(b,c,c), alpha(a,b,0), alpha(a+b,c,c) equal 1 by (R), (N), (R). Hence alpha(a,b,c) = alpha(a,b+c,c). That is, X(x,y,z) = X(x,y+z,z).   [s2]
- b = a: the factors alpha(a,a,c), alpha(a,a,c+d), alpha(0,c,d) equal 1 by (L), (L), (N). Hence alpha(a,a+c,d) = alpha(a,c,d), i.e. X(x,y,z) = X(x,x+y,z).   [s1]
- c = b: here b+c = 0 and the factors alpha(a,b,b), alpha(a,0,d), alpha(b,b,d) equal 1 by (R), (N), (L). Hence alpha(a,b,b+d) = alpha(a+b,b,d); with x=a, y=b, z=b+d this reads X(x,y,z) = X(x+y,y,y+z).   [t3]

**Step 2: the group.** Triples transform by 3x3 matrices over F_2 acting on the coefficient triple (x,y,z). Let S be the set of invertible M whose first row plus third row is (1,0,1) (those preserving x+z); |S| = 168/7 = 24. The matrices of s1, s2, t3 lie in S, and closure under composition (an exhaustive finite computation, script below) shows they generate all 24 elements. By Step 1, X(M t) = X(t) for every M in S and every triple t.
Consequence (not needed for the theorem): for independent x,y,z, the S-orbits are the fibers of (span, x+z), so alpha depends only on the span and on x+z.

**Step 3: the five-vector frame.** Work in the coefficient space F_2^4 with coordinates (a,b,c,d). Let u_i,v_i,w_i be the coefficient vectors of T_i and q_i = u_i + w_i:
q_1=a+c, q_2=a+d, q_3=b+d, q_4=a+c+d, q_5=a+b+d.
They sum to 0 and any four are independent. Let H_i = span(u_i,v_i,w_i), a hyperplane. One checks q_i in H_i and q_j not in H_i for j != i. Hence H_i is the unique hyperplane containing q_i and none of the other q_j (a linear functional is determined by its values on four independent vectors, and f(q_j) = 1 for exactly four j forces f(q_i) = 0). Every permutation pi of {1..5} extends to a unique psi in GL_4(F_2) with psi(q_i) = q_pi(i) (four of the q_i form a basis and the fifth is their sum), and psi(H_i) = H_pi(i) by the uniqueness just shown.

**Step 4 (equivariance lemma).** Let j = pi(i). Then (psi u_i, psi v_i, psi w_i) = M (u_j, v_j, w_j) for a unique M in GL_3(F_2) with M in S.
- Both triples are bases of H_j (psi(H_i) = H_j), so M exists and is invertible.
- psi u_i + psi w_i = psi(q_i) = q_j = u_j + w_j. The left side is (r_1 + r_3).(u_j,v_j,w_j), the right side is (1,0,1).(u_j,v_j,w_j); independence of u_j,v_j,w_j gives r_1 + r_3 = (1,0,1).

**Step 5 (conclusion).** A quadruple is a linear map phi: F_2^4 -> G (images of the coordinate vectors); T_i(phi) = phi applied to (u_i,v_i,w_i). The map phi -> phi psi is a bijection of all quadruples. By Step 4, T_i(phi psi) = M applied to T_j(phi) with M in S, so by Step 2, X_i(phi psi) = X_j(phi). Therefore the law of (X_1..X_5) equals the law of (X_pi(1)..X_pi(5)). QED.

The three points to check most carefully: the three substitutions in Step 1; the group computation in Step 2; the equivariance lemma in Step 4.

## 4. What the theorem explains

- Pentagon parity (|F| in {0,2,4}) holds for every sigma (it is delta^2 sigma = 1). Exchangeability needs (L),(R): random normalized cochains give non-uniform counts.
- The five-vector circuit (the uniform matroid U_{4,5}) appears because its automorphism group S_5 is what permutes the edges.
- The mean E[X_i] is the same for every edge and every sigma (each T_i is uniformly distributed over triples), so the whole content is equality of the ten pair correlations.

## 5. Computational checks (scripts in this repository)

| System | n | no flip | each 2-flip pattern | each 4-flip pattern |
|---|---|---|---|---|
| standard Cayley-Dickson (sedenions), (p,q)(r,s)=(pr - s\*q, sp + q r\*) | 4 | 15,136 | 2,688 | 4,704 |
| alternate product (a,b)(c,d)=(ac - b\*d, da\* + bc) | 4 | 26,656 | 3,456 | 864 |
| standard Cayley-Dickson | 5 | 166,576 | 48,720 | 78,960 |

- The alternate product has zero divisors at dimension 8 in my implementation, e.g. (e1+e4)(e2-e7) = 0, so it is not a Cayley-Dickson doubling product in the usual sense; it is included only as a second example of a cochain satisfying (L),(R).
- Random cochains satisfying (L),(R) (sampled from the exact linear solution space): n=3 (3 samples), n=4 (many), n=5 (2 samples) all show exactly one count per pattern size. Random normalized cochains without (L),(R): never uniform.
- Step 4 tested directly: X_i(phi psi_pi) = X_pi(i)(phi) with 0 mismatches over all 120 permutations x 300 random quadruples x 5 edges (two random sigma).
- (L),(R) for the standard Cayley-Dickson sign function: known for all n (section 10); checked here at n = 1..7 (`cd_LR_induction_check.py`) and proved by induction in section 10.
- Scripts (in this repository; `paren_verify.py` is the sedenion one): `gram_separator_verify.py`, `cd_LR_induction_check.py`, `uniformity_proof_check.py`, `sym_probe.py`, `uniformity_probe.py`, `pairs_check.py`, `pairs_classes.py`, `alt_product_check.py`, `dim32_check.py`, `general_n_check.py`, `transcribe_check.py`, `paren_verify.py`. `run_all.sh` runs them all.

## 6. Scope and open questions

- Necessity: neither (L) nor (R) alone suffices (explicit counterexamples, section 6a), and the pair is necessary and sufficient for the aggregate law (Theorem 9.1). Weaker conditions suffice only for finer statements, if at all; not investigated.
- Is there a more intrinsic description of the S_5 action (associahedron, binary matroids, cohomology)?
- (Answered: (L),(R) hold for the standard Cayley-Dickson unit loop for all n, section 10.)
- Is the theorem, or an equivalent statement, already in the literature?

## 6a. Proposition: why both conditions are needed

Fix n = 4 and let a "family" be a set of linear constraints on the 225 sign bits of a normalized sigma. Say M in GL_3(F_2) is a *universal symmetry* of the family if alpha(M t) = alpha(t) for every triple t and every sigma in the family.

**(a)** The group of universal symmetries has order 1 for no condition, **2 for (L) only** (it is {1, s1}), **2 for (R) only** (it is {1, s2}), and **24 for (L) and (R)** (the stabilizer S of x+z).
Proof: alpha(M t) + alpha(t) is an F_2-linear form in the sign bits of sigma, so it vanishes on the whole solution space of a family exactly when it lies in the row space of that family's constraint forms. This is checked for all 168 matrices and all 4096 triples by `scripts/exact_invariance_groups.py` (exact linear algebra, no sampling).
So Step 2 of the proof cannot be run with one condition: the invariance group available to the argument is of order 2, not 24.

**(b)** Neither condition alone implies exchangeability. `scripts/counterexamples.py` contains two explicit cochains (as 225-bit integers): one satisfies (L) but not (R), the other (R) but not (L); for each, the two-flip counts take 7 distinct values and the four-flip counts 4 distinct values over the 65,536 quadruples (verified by the script, standard library only).

Caveats: (a) is a statement about the method (which substitutions are guaranteed), not about all possible proofs; (b) is a genuine counterexample to sufficiency of a single condition. Both are for n = 4; the theorem itself is for every n.

## 7. Literature (partial; fetch extracts and abstracts only for several items)

Kirshtein arXiv:1102.5151 (recursive associator formulas, Remark 35); Culbert 2007; Cawagas 2004 (8 octonion-like and 7 quasi-octonion maximal subloops); Albuquerque-Majid math/9802116; Hu-Huang-Zhang 1506.01502; Bales 1107.1375; Saniga-Holweck-Pracna 1405.6888; Wilmot 2505.11747 (triad classification; no pentagon counts or closed associator formula in the extract). Not found does not mean not known.


---

## 9. Necessity: exchangeability implies (L) and (R)  (added 2026-10-17)

**Theorem 9.1 (hand proof; finite checks; not reviewed by a mathematician).** For every n and every normalized sigma on G = F_2^n, with alpha = delta sigma, the following are equivalent.
1. The law of (X_1,...,X_5) over uniform (a,b,c,d) in G^4 is invariant under S_5.
2. (L) alpha(x,x,z) = 1 and (R) alpha(x,z,z) = 1 for all x, z.
3. The ten pair sums T_ij = sum X_i X_j coincide.
4. P = Q = R = W as functions on G x G (defined below).

Setting. q = 2^n. Define on G x G
P(x,y) = sum_t alpha(t,x,y),  Q(x,y) = sum_t alpha(t,t+x,y),  R(x,y) = sum_t alpha(x,y,t),  W(x,y) = sum_t alpha(x,t,t+y)
(R here is a marginal function, not the law (R)), and <U,V> = sum_{x,y} U(x,y) V(x,y).

**Step 1 (valid for any +-1 triple function).** Changes of summation variables give
T_12=<R,W>, T_13=<P,R>, T_14=||R||^2, T_15=<Q,R>, T_23=<P,Q>, T_24=||W||^2, T_25=||Q||^2, T_34=<P,W>, T_35=||P||^2, T_45=<Q,W>.
Example, T_25: put s = a+b+c. Then X_2 = alpha(a,a+s,d) and X_5 = alpha(a+b,(a+b)+s,d), and a, a+b are independent and uniform, so the sum is sum_{s,d} Q(s,d)^2. Example, T_24: put s = b+c+d; X_2 = alpha(a,t,t+s) with t = b+c, X_4 = alpha(a,t',t'+s) with t' = b, giving sum_{a,s} W(a,s)^2.

**Step 2 (sum of squares).** Take c = (-2,-2,3,-2,-2,3,3,-2,3,-2) in the order 12,13,14,15,23,24,25,34,35,45. Then sum(c) = 0 and
F := c.T = 3(||P||^2+||Q||^2+||R||^2+||W||^2) - 2 sum_{U<V} <U,V> = sum over the six pairs U<V of ||U-V||^2 >= 0,
with F = 0 iff P = Q = R = W.

**Step 3 (F detects every defect; uses only normalization).** At (0,z): P = R = W = q and Q = q - 2 l_z, l_z = #{t : alpha(t,t,z) = -1}. At (x,0): P = Q = R = q and W = q - 2 r_x, r_x = #{t : alpha(x,t,t) = -1}. The point (0,z) contributes 12 l_z^2 to F and (x,0) contributes 12 r_x^2; they meet only at (0,0), where both are 0. So
F >= 12 (sum_z l_z^2 + sum_x r_x^2) >= 12 (number of (L)-defects + (R)-defects).

**Step 4 (necessity).** If all T_ij are equal, F = (sum c) T_ij = 0, so P = Q = R = W, so every l_z and r_x is 0: (L) and (R) hold. Exchangeability gives equal pair sums (the pair characters are permuted by S_5). Steps 1-3 hold for every normalized +-1 triple function; they do not use that alpha is a coboundary.

**Step 5 (sufficiency by this route).** Let d_x = sigma(x,x). Expanding (L), (R):
(L') sigma(x,z) sigma(x,x+z) = d_x,   (R') sigma(x,z) sigma(x+z,z) = d_z.
Multiplying (R') at (u,v), (L') at (u+v,v) and (R') at (u+v,u) gives (C) sigma(u,v) sigma(v,u) = d_u d_v d_{u+v}. Then for all t,x,y:
- Id.1  alpha(t,t+x,y) = alpha(t,x,y): the ratio is [sigma(t,t+x) sigma(t,x)] [sigma(t,t+x+y) sigma(t,x+y)] = d_t d_t = 1 by (L') twice.
- Id.2  alpha(x,y+t,t) = alpha(x,y,t): the ratio is [sigma(x+y+t,t) sigma(x+y,t)] [sigma(y+t,t) sigma(y,t)] = d_t d_t = 1 by (R') twice.
- Id.3  alpha(t,x,y) = alpha(x,y,t+x+y): expand the right side as sigma(x,y) sigma(x+y,t+x+y) sigma(y,t+x+y) sigma(x,t+x); apply (L') to the last three factors (each gains a d), reverse the arguments with (C) (each gains three d's); every d occurs twice and cancels, leaving sigma(x,y) sigma(t,x+y) sigma(t+x,y) sigma(t,x) = alpha(t,x,y).

Id.1 gives Q = P. Substituting t -> t+y in the sum defining W and using Id.2 gives W = R. Summing Id.3 over t gives P = R. So P = Q = R = W, all Gram entries equal ||P||^2, and the ten pair sums coincide. The five means are equal for every sigma (each edge map G^4 -> G^3 is a surjective linear map with equal fibres), and the 16 even-parity sign patterns have 16 characters (constant, five singletons, ten pairs), so equal means and equal pair sums give S_5-invariance. This reproves the aggregate form of section 2 without the order-24 group; it does not give the finer statement for each rank stratum.

**Scope.** The theorem concerns the aggregate law over all of G^4. It does not say the edge law is concentrated at +1 or that the algebra is associative.

**Credit.** The weight vector c, the Gram identification, the sum-of-squares form, Step 3 and the identities of Step 5 come from a report by a separate AI instantiation, relayed by the human author. Each identity was re-derived by hand and checked by script. Agreement among AI systems is not treated as evidence.

**Checks (`scripts/gram_separator_verify.py`, about 1.5 min).** Gram identities for random +-1 triple functions at q = 4, 8; sum(c) = 0 and the SOS form; the defect bound and F >= 0 on all 512 normalized cochains at n = 2 (F = 0 for exactly the 16 with (L)&(R); minimum positive F is 160); random cochains at n = 3, 4; all 961 single flips of the standard n = 5 cochain (minimum F = 2400); Id.1-3 and P = Q = R = W for the standard and alternate Cayley-Dickson cochains at n = 1..6.
**Not checked:** exhaustive search beyond n = 2; independent human review.

## 10. (L) and (R) for Cayley-Dickson basis units, all n

**Known.** Kinyon, Phillips, Vojtechovsky, *C-loops: extensions and constructions*, arXiv:math/0412390, section 7: the loop L_n of signed standard basis elements of the real Cayley-Dickson algebra satisfies the alternative and flexible laws for every n (they cite their Lemma 6.2(vii), which they prove only in part). Our (L) and (R) are the left and right alternative laws of this loop. See also arXiv:2501.00123 (doubling of loops with involution). Sources were read through fetch extracts only.

**Our proof (a re-derivation, not a new result).** Product (p,q)(r,s) = (pr - s-bar q, sp + q r-bar). Write eps(x) = +1 if x = 0, else -1, so e-bar_x = eps(x) e_x and u^2 = eps(u) for every basis unit u; conjugation reverses products. Assume (L) and (R) for basis units of A_n; let u, w be basis units of A_{n+1} (one nonzero component each).
- (L), u = (p,0), w = (r,s): u(uw) = (p(pr), (sp)p) and (uu)w = (p^2 r, s p^2); equal by (L) and (R) at level n.
- (L), u = (0,q), w = (r,s): (uu)w = (-r,-s); u(uw) = (-(r q-bar) q, -q(q-bar s)); and (r q-bar) q = eps(q) r q^2 = r by (R), q(q-bar s) = eps(q) q^2 s = s by (L).
- (R), w = (r,0), u = (p,q): (uw)w = (p r^2, q r^2) = u(ww), by (R) at level n.
- (R), w = (0,s), u = (p,q): u(ww) = (-p,-q); (uw)w = (-s-bar(sp), -s(s-bar q)) = (-p,-q), using s-bar(sp) = eps(s) s^2 p = p by (L) and s(s-bar q) = q likewise.

Both laws at level n+1 use both at level n, so the pair is proved together. Checked: `scripts/cd_LR_induction_check.py` builds the unit sign table by the same recursion (cross-checked against the full vector product for n <= 4) and verifies (L),(R) for n = 1..7.

**Alternate product** (a,b)(c,d) = (ac - b-bar d, da-bar + bc): the same induction works with one change (the (R) case with w = (0,s) uses s(s-bar q) = q, which is (L), not (R)); (L),(R) are verified for n = 1..6 in `gram_separator_verify.py`. We did not determine whether this is in the literature.

**Consequence.** The theorem of section 2 holds for the standard Cayley-Dickson algebras at every n, not only n = 3, 4, 5. The unit loop is alternative from n = 4 on while the algebra is not.

## 11. Literature update (round 5, 2026-10-17)

Related, not the same: Albuquerque-Elduque-Perez-Izquierdo, *Alternative quasialgebras*, Bull. Austral. Math. Soc. 63 (2001) 257-268 (Prop. 3.9(i): phi(a,b,c) = 1 iff the subgroup generated by a,b,c has order at most 4, for alternative division quasialgebras; compare with our rank-2 statement only after reading it in full). Albuquerque-Majid, math/9802116 (octonions as a Z_2^3 cocycle twist; abstract only). We did not find the pentagon exchangeability statement, the Gram argument, or the necessity theorem in the sources searched; the search was partial, and not finding something is not evidence that it is new. See `notes/literature-audit-round5.md`.

## 12. History

The derivation path, corrections and failed approaches are recorded in the project notes: `uniformity-property-note-2026-10-16.md` (addenda 1-3c), `sedenion-pentagon-proof-revised-2026-10-16.md`, and the literature audits rounds 1-4.
