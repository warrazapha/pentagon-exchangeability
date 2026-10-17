# Checks E[X_i] = 25/256 and E[X_i X_j] = 113/512 for the sedenions and that the five means coincide for random sigma.
# Run from this directory: python3 corr_check.py   (needs numpy)
exec(open('uniformity_probe.py').read().split("dep=[")[0])
import numpy as np
def alpha_arr(v):
    s=np.zeros((N,N),dtype=np.int8)
    for x in range(1,N):
        for y in range(1,N): s[x,y]=v>>var[x,y]&1
    X=np.arange(N)
    A=np.zeros((N,N,N),dtype=np.int8)
    for x in range(N):
        for y in range(N):
            for z in range(N):
                A[x,y,z]=s[x,y]^s[x^y,z]^s[y,z]^s[x,y^z]
    return A
def moments(A):
    g=np.array(np.meshgrid(*[np.arange(N)]*4,indexing='ij')).reshape(4,-1)
    a,b,c,d=g
    T=[(a,b,c),(a,b^c,d),(b,c,d),(a,b,c^d),(a^b,c,d)]
    X=[1-2*A[t].astype(np.int64) for t in T]
    means=[int(x.sum()) for x in X]
    pairs={(i+1,j+1):int((X[i]*X[j]).sum()) for i in range(5) for j in range(i+1,5)}
    return means,pairs
def stdA():
    exec(open('alt_product_check.py').read().split("S=tables(std)")[0],globals())
    S=tables(std); al=alpha(S)
    A=np.zeros((N,N,N),dtype=np.int8)
    for k,v in al.items(): A[k]=(v<0)
    return A
A=stdA(); m,p=moments(A)
print('sedenion means*',m[0],set(m),'/65536 ->',m[0]/65536,25/256)
print('pairs',set(p.values()),[v/65536 for v in set(p.values())],113/512)
import random
random.seed(3)
for name,cons in (('random sigma',None),('dep-trivial',dep if False else None)):
    pass
basis_all=[1<<i for i in range(NV)]
print('--- unconstrained random sigma: means and pair sums')
for _ in range(3):
    v=sample(basis_all); m,p=moments(alpha_arr(v)); print(m); print(p)
