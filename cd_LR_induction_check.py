"""Check (L) alpha(x,x,z)=1 and (R) alpha(x,z,z)=1 for Cayley-Dickson basis units, n up to 7,
using the unit-level doubling recursion (p,q)(r,s)=(pr - conj(s)q, sp + q conj(r)) applied to basis units only.
Cross-checked against the full vector product for n<=4."""
import sys
def eps(x): return 1 if x==0 else -1
def table(n):
    if n==0: return [[1]]
    S=table(n-1); m=1<<(n-1)
    T=[[0]*(2*m) for _ in range(2*m)]
    for x in range(2*m):
        h1,xp=divmod(x,m)
        for y in range(2*m):
            h2,yp=divmod(y,m)
            if h1==0 and h2==0: v=S[xp][yp]
            elif h1==0 and h2==1: v=S[yp][xp]            # (p,0)(0,s)=(0,sp)
            elif h1==1 and h2==0: v=S[xp][yp]*eps(yp)     # (0,q)(r,0)=(0,q rbar)
            else: v=-eps(yp)*S[yp][xp]                   # (0,q)(0,s)=(-sbar q,0)
            T[x][y]=v
    return T
def conj(v):
    return [v[0]]+[-c for c in v[1:]]
def vmul(u,v):
    n=len(u)
    if n==1: return [u[0]*v[0]]
    h=n//2; p,q,r,s=u[:h],u[h:],v[:h],v[h:]
    a=vmul(p,r); b=vmul(conj(s),q); c=vmul(s,p); d=vmul(q,conj(r))
    return [x-y for x,y in zip(a,b)]+[x+y for x,y in zip(c,d)]
def alpha(T,x,y,z):
    # (e_x e_y) e_z = alpha e_x (e_y e_z); indices xor
    return T[x][y]*T[x^y][z]*T[y][z]*T[x][y^z]
ok=True
for n in range(1,8):
    T=table(n); N=1<<n
    if n<=4:
        for x in range(N):
            for y in range(N):
                e=[0]*N; e[x]=1; f=[0]*N; f[y]=1
                w=vmul(e,f); assert w[x^y]==T[x][y], (n,x,y)
    L=all(alpha(T,x,x,z)==1 for x in range(N) for z in range(N))
    R=all(alpha(T,x,z,z)==1 for x in range(N) for z in range(N))
    print(f"n={n}: cross-checked against full vector product: {'yes' if n<=4 else 'no (n>4: unit table only)'}; L={L}; R={R}")
    ok&=L and R
print("ALL OK" if ok else "FAIL"); sys.exit(0 if ok else 1)
