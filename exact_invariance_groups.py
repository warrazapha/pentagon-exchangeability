# EXACT (no sampling): for each constraint family on sigma, the group of linear substitutions M of triples
# (M in GL_3(F_2) acting on (x,y,z)) with alpha(M t) = alpha(t) for EVERY cochain sigma satisfying the family.
# alpha(Mt)+alpha(t) is a linear form in the sign bits of sigma; it vanishes on the whole solution space
# iff it lies in the row space of the family's constraint forms. Run: python3 exact_invariance_groups.py  (needs numpy)
exec(open('uniformity_probe.py').read().split("dep=[")[0])
import itertools
def apply(M,t):
    v=t; out=[]
    for r in M:
        o=0
        for k in range(3):
            if r>>(2-k)&1: o^=v[k]
        out.append(o)
    return tuple(out)
def invertible(M):
    s=set()
    for m in range(1,8):
        o=0
        for k in range(3):
            if m>>(2-k)&1: o^=M[k]
        s.add(o)
    return len(s)==7
GL=[M for M in itertools.product(range(1,8),repeat=3) if invertible(M)]
assert len(GL)==168
def rowspace(forms):
    piv={}
    for m in forms:
        for p in sorted(piv,reverse=True):
            if m>>p&1: m^=piv[p]
        if m: piv[m.bit_length()-1]=m
    return piv
def inspace(m,piv):
    for p in sorted(piv,reverse=True):
        if m>>p&1: m^=piv[p]
    return m==0
fam={
 'no condition':[],
 'left only  (L)':[alpha_lin(x,x,z) for x in range(1,N) for z in range(1,N)],
 'right only (R)':[alpha_lin(x,z,z) for x in range(1,N) for z in range(1,N)],
 'left and right':[alpha_lin(x,x,z) for x in range(1,N) for z in range(1,N)]+[alpha_lin(x,z,z) for x in range(1,N) for z in range(1,N)],
}
def name(M): return '('+','.join(''.join(c for c,b in zip('xyz',(r>>2&1,r>>1&1,r&1)) if b) for r in M)+')'
trip=list(itertools.product(range(N),repeat=3))
for fname,cons in fam.items():
    piv=rowspace(cons)
    good=[M for M in GL if all(inspace(alpha_lin(*t)^alpha_lin(*apply(M,t)),piv) for t in trip)]
    print(f'{fname:16s} universal invariance group order {len(good):2d}', [name(M) for M in good][:6] if len(good)<=6 else '(24 elements: all M with row1+row3 = (1,0,1))' if len(good)==24 else '')
