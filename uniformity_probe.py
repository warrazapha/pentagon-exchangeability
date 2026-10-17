# Solves linear constraint families on the sign bits of sigma (F_2^4), samples random cochains and prints pentagon pattern counts per flip-set size. Other scripts exec the top part of this file.
# Run from this directory: python3 uniformity_probe.py   (needs numpy)
import random, itertools, collections
N=16
var={}
for x in range(1,N):
    for y in range(1,N): var[x,y]=len(var)
NV=len(var)
def lin(x,y):  # bitmask of s(x,y)
    return 0 if x==0 or y==0 else 1<<var[x,y]
def alpha_lin(x,y,z): return lin(x,y)^lin(x^y,z)^lin(y,z)^lin(x,y^z)
def rank_dep(x,y,z):
    S={0,x,y,z,x^y,x^z,y^z,x^y^z}; return len(S)  # span size 2^dim if independent -> 8
def solve(constraints):
    # constraints: list of masks that must be 0 (homogeneous) ; return nullspace basis
    rows=[]; piv={}
    for m in constraints:
        for p,r in piv.items():
            if m>>p&1: m^=r
        if m:
            p=m.bit_length()-1
            for q in list(piv):
                if piv[q]>>p&1: piv[q]^=m
            piv[p]=m
    free=[i for i in range(NV) if i not in piv]
    basis=[]
    for f in free:
        v=1<<f
        for p,r in piv.items():
            if r>>f&1: v|=1<<p
        basis.append(v)
    return basis
def sample(basis):
    v=0
    for b in basis:
        if random.random()<.5: v^=b
    return v
def census(v):
    s=lambda x,y:0 if x==0 or y==0 else v>>var[x,y]&1
    al={(x,y,z):s(x,y)^s(x^y,z)^s(y,z)^s(x,y^z) for x in range(N) for y in range(N) for z in range(N)}
    c=collections.Counter()
    for a,b,cc,d in itertools.product(range(N),repeat=4):
        T=[(a,b,cc),(a,b^cc,d),(b,cc,d),(a,b,cc^d),(a^b,cc,d)]
        c[tuple(i for i,t in enumerate(T) if al[t])]+=1
    return {k:sorted(set(n for F,n in c.items() if len(F)==k)) for k in (0,2,4)}, al
def report(name,cons,trials=4):
    basis=solve(cons)
    print(name,'nullspace dim',len(basis))
    for _ in range(trials):
        r,al=census(sample(basis)); print('  ',r,'neg',sum(al.values()))
dep=[alpha_lin(x,y,z) for x in range(N) for y in range(N) for z in range(N) if rank_dep(x,y,z)<8]
report('alpha=+1 on dependent triples',dep)
# weaker: only x=y or y=z or x=z or involving zero is automatic; alpha=1 on rank<=2 ... same. try: alpha=1 when x=y (i.e. (xx)z=x(xz))
alt=[alpha_lin(x,x,z) for x in range(1,N) for z in range(1,N)]+[alpha_lin(x,z,z) for x in range(1,N) for z in range(1,N)]
report('left/right alternative only',alt)
al3=[alpha_lin(x,y,z) for x in range(N) for y in range(N) for z in range(N) if rank_dep(x,y,z)<8 and len({x,y,z})<3]
report('alpha=+1 when two entries equal',al3)
