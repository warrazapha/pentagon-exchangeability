"""Consolidated verification for the sedenion parenthesis-spectrum note.
Independent of the project engine except for section (0), which cross-checks the basis table against it.
Run:  python3 paren_verify.py   (optionally set ENGINE_DIR to the folder holding evaluator_algebras.py)
"""
import itertools, os, sys
from collections import Counter
import numpy as np

# ---------- Cayley-Dickson product, convention is a parameter ----------
def conj(x):
    y = -x.copy(); y[0] = x[0]; return y
def mul_ours(x, y):               # (p,q)(r,s) = (pr - s̄q, sp + q r̄)   [engine, Kirshtein]
    n = len(x)
    if n == 1: return x*y
    h = n//2; p,q,r,s = x[:h],x[h:],y[:h],y[h:]
    return np.concatenate([mul_ours(p,r) - mul_ours(conj(s),q), mul_ours(s,p) + mul_ours(q,conj(r))])
def mul_alt(x, y):                # (p,q)(r,s) = (pr - s q̄, p̄ s + r q)   [second common convention]
    n = len(x)
    if n == 1: return x*y
    h = n//2; p,q,r,s = x[:h],x[h:],y[:h],y[h:]
    return np.concatenate([mul_alt(p,r) - mul_alt(s,conj(q)), mul_alt(conj(p),s) + mul_alt(r,q)])

def table(mul, n=4):
    N = 2**n; S = np.zeros((N,N),dtype=int); X = np.zeros((N,N),dtype=int)
    for i in range(N):
        for j in range(N):
            e = np.zeros(N,dtype=int); f = np.zeros(N,dtype=int); e[i]=1; f[j]=1
            p = mul(e,f); k = int(np.nonzero(p)[0][0]); S[i,j]=p[k]; X[i,j]=k
    return S, X

def make_alpha(S, X):
    return lambda x,y,z: S[x,y]*S[X[x,y],z]*S[y,z]*S[x,X[y,z]]   # (xy)z = alpha x(yz)

# ---------- F_2 linear algebra helpers (indices are 4-bit integers) ----------
def span(vs):
    sp = {0}
    for v in vs: sp |= {s ^ v for s in sp}
    return sp
def rank(vs): return len(span(vs)).bit_length() - 1
T = 8
h = lambda x: (x >> 3) & 1

def predicted_alpha(x,y,z):       # the two-branch triple formula, plus dependent -> +1
    if rank([x,y,z]) < 3: return 1
    if T in span([x,y,z]): return -1
    return -1 if h(x) == h(z) else 1

def run(mul, label):
    S, X = table(mul); al = make_alpha(S, X)
    bad = [(x,y,z) for x in range(16) for y in range(16) for z in range(16) if al(x,y,z) != predicted_alpha(x,y,z)]
    print(f"[{label}] triple formula vs brute force on all 4096 index triples: mismatches = {len(bad)}")
    return S, X, al

S, X, al = run(mul_ours, "engine convention")
run(mul_alt, "alternative convention")

# (0) optional cross-check of the basis table against the project engine
ed = os.environ.get("ENGINE_DIR", "/home/claude/eng")
if os.path.exists(os.path.join(ed, "evaluator_algebras.py")):
    sys.path.insert(0, ed)
    import evaluator_algebras as E
    ok = True
    for i in range(16):
        for j in range(16):
            p = E.SEDENION.mul(E.SEDENION.basis(i), E.SEDENION.basis(j))
            nz = [(k,c) for k,c in enumerate(p) if c != 0]
            ok &= (len(nz)==1 and nz[0][0]==X[i,j] and nz[0][1]==S[i,j])
    print("[engine] basis product table identical to project engine:", ok)

# ---------- full census of all 16^4 index 4-tuples ----------
def edges(a,b,c,d):
    return [al(a,b,c), al(a,b^c,d), al(b,c,d), al(a,b,c^d), al(a^b,c,d)]
pattern = Counter(); byrank = {}
frame_bad = 0; odd = 0
q = [(1,0,1,0),(1,0,0,1),(0,1,0,1),(1,0,1,1),(1,1,0,1)]          # q_i in operand coords (a,b,c,d)
def vec(i): return tuple((i>>k)&1 for k in range(4))
def dot(u,v): return sum(a*b for a,b in zip(u,v)) % 2
def Hmember(i, kv):       # is kv in H_i = {0,q_i} U {q_j+q_l : j,l != i} ?
    if not any(kv): return True
    if kv == q[i]: return True
    for j in range(5):
        for l in range(j+1,5):
            if i not in (j,l) and tuple((a+b)%2 for a,b in zip(q[j],q[l])) == kv: return True
    return False
for tup in itertools.product(range(16), repeat=4):
    a,b,c,d = tup
    e = edges(a,b,c,d); flips = tuple(i for i in range(5) if e[i]==-1)
    if len(flips)%2: odd += 1
    r = rank(tup); pattern[(r,flips)] += 1
    # --- frame prediction for rank 3 and 4
    if r >= 3:
        hv = (h(a),h(b),h(c),h(d)); u = [dot(q[i],hv) for i in range(5)]
        if r == 4:
            kv = tuple(1 if T == 0 else 0 for _ in range(4))
            # coordinates of t=8 in the basis (a,b,c,d)
            kv = next(k for k in itertools.product((0,1),repeat=4)
                      if (k[0]*a)^(k[1]*b)^(k[2]*c)^(k[3]*d) == T)
            pred = tuple(i for i in range(5) if Hmember(i,kv) or u[i]==0)
        else:
            kv = next(k for k in itertools.product((0,1),repeat=4) if any(k) and
                      (k[0]*a)^(k[1]*b)^(k[2]*c)^(k[3]*d) == 0)
            tin = T in span(tup)
            pred = tuple(i for i in range(5) if (not Hmember(i,kv)) and (tin or u[i]==0))
        if pred != flips: frame_bad += 1
print("tuples whose edge-flip count is odd (pentagon product must be +1):", odd)
print("tuples (rank 3 or 4) where the five-point-frame prediction differs from brute force:", frame_bad)
print("\nrank, #flips -> number of index 4-tuples")
agg = Counter()
for (r,f),n in pattern.items(): agg[(r,len(f))] += n
for k in sorted(agg): print("  rank", k[0], "flips", k[1], ":", agg[k])
two = {f:n for (r,f),n in pattern.items() if len(f)==2}
four = {f:n for (r,f),n in pattern.items() if len(f)==4}
# per-pattern totals (all ranks), and by rank
def per(pat, rk): return pattern.get((rk,pat),0)
print("\nper two-flip pattern (rank3, rank4, total):", sorted({(per(p,3),per(p,4),per(p,3)+per(p,4)) for p in itertools.combinations(range(5),2)}))
print("per four-flip pattern (rank3, rank4, total):", sorted({(per(p,3),per(p,4),per(p,3)+per(p,4)) for p in itertools.combinations(range(5),4)}))
print("tuples with no flipped edge:", sum(n for (r,f),n in pattern.items() if not f), "of", 16**4)

# ---------- F0 (alternativity of the unit loop) and Proposition 1' (second convention = opposite algebra) ----------
def _f0(mul, label):
    S_, X_ = table(mul)
    ok = True
    for x in range(16):
        for y in range(16):
            sq = S_[x, x]                                  # e_x * e_x = sq * e_0
            # e_x(e_x e_y): sign S[x,y]*S[x, x^y]; (e_x e_x)e_y = sq*S[0,y]
            ok &= (S_[x, y] * S_[x, x ^ y] == sq * S_[0, y])
            # (e_y e_x)e_x: sign S[y,x]*S[y^x, x]; e_y (e_x e_x) = sq*S[y,0]
            ok &= (S_[y, x] * S_[y ^ x, x] == sq * S_[y, 0])
    print(f"[{label}] F0: x(xy) = x^2 y and (yx)x = y x^2 on all 256 unit pairs: {ok}")
_f0(mul_ours, "engine convention"); _f0(mul_alt, "alternative convention")
S2_, X2_ = table(mul_alt)
print("Prop 1': sigma_alt(x,y) == sigma(y,x) on all 256 pairs (second convention is the opposite algebra):",
      all(S2_[x, y] == S[y, x] and X2_[x, y] == X[y, x] for x in range(16) for y in range(16)))
