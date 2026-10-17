"""Verification of the Gram-matrix necessity proof (all steps).  Python 3 + numpy.  ~2-3 minutes.
Pair order 12,13,14,15,23,24,25,34,35,45 ; c = (-2,-2,3,-2,-2,3,3,-2,3,-2) ; F = c.T.
Marginals: P(x,y)=sum_t a(t,x,y), Q=sum_t a(t,t+x,y), R=sum_t a(x,y,t), W=sum_t a(x,t,t+y).
Checks:
 A  the ten pair sums equal the ten Gram entries for ARBITRARY +-1 triple functions;  B  F = sum_{U<V}||U-V||^2, sum(c)=0
 C  defect bound  F >= 12(sum_z l_z^2 + sum_x r_x^2)   and  F>=0, F=0 iff L&R   (all 512 cochains at n=2; samples at n=3,4; all 961 single flips of CD at n=5)
 D  for L&R cochains (standard and alternate Cayley-Dickson, n=1..6): identities  a(t,t+x,y)=a(t,x,y), a(x,y+t,t)=a(x,y,t), a(t,x,y)=a(x,y,t+x+y)  and P=Q=R=W.
Hand proofs of A, B, C, D are in pentagon-necessity-gram-proof-2026-10-17.md."""
import itertools, sys, time
import numpy as np
pairs=list(itertools.combinations(range(5),2))
c=np.array([-2,-2,3,-2,-2,3,3,-2,3,-2])
def edges(q):
    g=np.arange(q); a,b,cc,d=[x.ravel() for x in np.meshgrid(g,g,g,g,indexing='ij')]
    return [(a,b,cc),(a,b^cc,d),(b,cc,d),(a,b,cc^d),(a^b,cc,d)]
def pair_sums(A,q):
    X=[A[e[0],e[1],e[2]].astype(np.int64) for e in edges(q)]
    return np.array([int((X[i]*X[j]).sum()) for i,j in pairs])
def marginals(A,q):
    g=np.arange(q); x,y=np.meshgrid(g,g,indexing='ij'); P=np.zeros((q,q),dtype=np.int64); Q=P.copy(); R=P.copy(); W=P.copy()
    for t in range(q): P+=A[t,x,y]; Q+=A[t,t^x,y]; R+=A[x,y,t]; W+=A[x,t,t^y]
    return P,Q,R,W
def gram(P,Q,R,W):
    ip=lambda U,V:int((U*V).sum()); return np.array([ip(R,W),ip(P,R),ip(R,R),ip(Q,R),ip(P,Q),ip(W,W),ip(Q,Q),ip(P,W),ip(P,P),ip(Q,W)])
def alpha_of(S,q):
    g=np.arange(q); x,y,z=np.meshgrid(g,g,g,indexing='ij'); return S[x,y]*S[x^y,z]*S[y,z]*S[x,y^z]
def defects(A,q):
    g=np.arange(q); x,z=np.meshgrid(g,g,indexing='ij'); Lm=(A[x,x,z]==-1); Rm=(A[x,z,z]==-1)
    return int(Lm.sum()),int(Rm.sum()),int((Lm.sum(0)**2).sum()),int((Rm.sum(1)**2).sum())
def sig_from_mask(bits,q):
    S=np.ones((q,q),dtype=np.int64); k=0
    for x in range(1,q):
        for y in range(1,q):
            if (bits>>k)&1: S[x,y]=-1
            k+=1
    return S
def eps(x): return 1 if x==0 else -1
def table(n,alt):
    if n==0: return [[1]]
    S=table(n-1,alt); m=1<<(n-1); T=[[0]*(2*m) for _ in range(2*m)]
    for x in range(2*m):
        h1,xp=divmod(x,m)
        for y in range(2*m):
            h2,yp=divmod(y,m)
            if h1==0 and h2==0: v=S[xp][yp]
            elif not alt:
                v = S[yp][xp] if (h1==0 and h2==1) else S[xp][yp]*eps(yp) if (h1==1 and h2==0) else -eps(yp)*S[yp][xp]
            else:
                v = S[yp][xp]*eps(xp) if (h1==0 and h2==1) else S[xp][yp] if (h1==1 and h2==0) else -eps(xp)*S[xp][yp]
            T[x][y]=v
    return T
rng=np.random.default_rng(1); allok=True
def report(name,ok):
    global allok; allok&=bool(ok); print(("[ok]  " if ok else "[FAIL] ")+name)
# A,B
okA=okB=True
for q in (4,8):
    for _ in range(6):
        A=rng.choice([-1,1],size=(q,q,q)).astype(np.int64); T=pair_sums(A,q); P,Q,R,W=marginals(A,q)
        okA&=(T==gram(P,Q,R,W)).all(); okB&=int(c@T)==sum(int(((U-V)**2).sum()) for U,V in itertools.combinations([P,Q,R,W],2))
report("A: ten pair sums = ten Gram entries (arbitrary +-1 triple functions, q=4,8)",okA)
report("B: sum(c)=0 and F=c.T = sum of six squared distances",okB and c.sum()==0)
# C n=2 exhaustive
q=4; neg=0; boundok=True; zeros=[]; minpos=10**9
for bits in range(512):
    A=alpha_of(sig_from_mask(bits,q),q); F=int(c@pair_sums(A,q)); L,R,sl,sr=defects(A,q)
    neg+=F<0; boundok&=F>=12*(sl+sr)
    if F==0: zeros.append((L,R))
    else: minpos=min(minpos,F)
report(f"C: n=2 all 512 cochains: F>=0, defect bound holds, F=0 for exactly {len(zeros)} (all L&R: {all(a==0 and b==0 for a,b in zeros)}), min positive F={minpos}",neg==0 and boundok and len(zeros)==16 and all(a==0 and b==0 for a,b in zeros))
for q,trials in ((8,200),(16,30)):
    ok=True
    for _ in range(trials):
        S=np.ones((q,q),dtype=np.int64); S[1:,1:]=rng.choice([-1,1],size=(q-1,q-1)); A=alpha_of(S,q); F=int(c@pair_sums(A,q)); L,R,sl,sr=defects(A,q)
        ok&= F>=12*(sl+sr) and F>0 if (L+R)>0 else F>=0
    report(f"C: random cochains q={q} ({trials}): F>=12(sum l^2+sum r^2) when defective",ok)
q=32; S0=np.array(table(5,False),dtype=np.int64); ok=True; minF=10**18
for x in range(1,q):
    for y in range(1,q):
        S=S0.copy(); S[x,y]*=-1; A=alpha_of(S,q); F=int(c@pair_sums(A,q)); L,R,sl,sr=defects(A,q)
        ok&= F>=12*(sl+sr); minF=min(minF,F)
report(f"C: n=5, all 961 single flips of standard CD: defect bound holds, min F={minF}",ok and minF>0)
# D
for name,alt in (("standard",False),("alternate",True)):
    ok=True
    for n in range(1,7):
        q=1<<n; A=alpha_of(np.array(table(n,alt),dtype=np.int64),q); g=np.arange(q); t,x,y=np.meshgrid(g,g,g,indexing='ij')
        L,R,_,_=defects(A,q)
        i1=(A[t,t^x,y]==A[t,x,y]).all(); i2=(A[x,y^t,t]==A[x,y,t]).all(); i3=(A[t,x,y]==A[x,y,t^x^y]).all()
        P,Q,Rm,W=marginals(A,q)
        ok&= L==0 and R==0 and i1 and i2 and i3 and (P==Q).all() and (Q==Rm).all() and (Rm==W).all()
    report(f"D: {name} Cayley-Dickson n=1..6: L&R hold, identities 1-3 hold, P=Q=R=W",ok)
print("ALL CHECKS PASSED" if allok else "SOME CHECKS FAILED"); sys.exit(0 if allok else 1)
