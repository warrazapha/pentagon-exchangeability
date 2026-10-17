# Finds which invertible 3x3 substitutions on triples leave alpha invariant, for left-only, right-only and left+right families. Top part is exec'd by uniformity_proof_check.py.
# Run from this directory: python3 sym_probe.py   (needs numpy)
exec(open('pairs_check.py').read().split("if __name__")[0])
import itertools
# 3x3 invertible matrices over F2 as tuples of 3 row-bitmasks (row i = coefficients of new_i over (x,y,z) bits 4,2,1)
def apply(M,t):
    x,y,z=t; v=(x,y,z); out=[]
    for r in M:
        o=0
        for k in range(3):
            if r>>(2-k)&1: o^=v[k]
        out.append(o)
    return tuple(out)
def inv(M):
    # invertible iff images of basis independent
    cols=[ (1 if M[0]>>(2-k)&1 else 0, 1 if M[1]>>(2-k)&1 else 0, 1 if M[2]>>(2-k)&1 else 0) for k in range(3)]
    s=set()
    for m in range(1,8):
        v=[0,0,0]
        for k in range(3):
            if m>>(2-k)&1: v=[v[i]^cols[k][i] for i in range(3)]
        s.add(tuple(v))
    return len(s)==7 and (0,0,0) not in s
GL=[M for M in itertools.product(range(1,8),repeat=3) if inv(M)]
print(len(GL))
fam={
 'left':[alpha_lin(x,x,z) for x in rng for z in rng],
 'right':[alpha_lin(x,z,z) for x in rng for z in rng],
 'both':[alpha_lin(x,x,z) for x in rng for z in rng]+[alpha_lin(x,z,z) for x in rng for z in rng],
}
random.seed(21)
trip=[(x,y,z) for x in range(N) for y in range(N) for z in range(N)]
res={}
for name,cons in fam.items():
    basis=solve(cons); Xs=[1-2*alpha_arr(sample(basis)) for _ in range(6)]
    good=[]
    for M in GL:
        ok=True
        for X in Xs:
            for t in trip:
                if X[t]!=X[apply(M,t)]: ok=False;break
            if not ok:break
        if ok: good.append(M)
    res[name]=good
    print(name,'symmetries (invertible 3x3 acting on (x,y,z)):',len(good))
def show(M): return '('+','.join(''.join(c for c,b in zip('xyz',(r>>2&1,r>>1&1,r&1)) if b) for r in M)+')'
for n in res:
    print(n,[show(M) for M in res[n]][:40])
