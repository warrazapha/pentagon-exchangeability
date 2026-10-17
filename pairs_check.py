# Ten pair-correlation sums C_ij as explicit sums over (a,b,c,d); checks the explicit formulas against brute force on a random sigma.
# Run from this directory: python3 pairs_check.py   (needs numpy)
exec(open('uniformity_probe.py').read().split("dep=[")[0])
import numpy as np, itertools, random
rng=range(1,N)
def alpha_arr(v):
    s=np.zeros((N,N),dtype=np.int64)
    for x in range(1,N):
        for y in range(1,N): s[x,y]=v>>var[x,y]&1
    A=np.zeros((N,N,N),dtype=np.int64)
    for x in range(N):
        for y in range(N):
            for z in range(N):
                A[x,y,z]=s[x,y]^s[x^y,z]^s[y,z]^s[x,y^z]
    return A
idx=np.arange(N)
def brute(X):
    g=np.array(np.meshgrid(idx,idx,idx,idx,indexing='ij')).reshape(4,-1); a,b,c,d=g
    T=[(a,b,c),(a,b^c,d),(b,c,d),(a,b,c^d),(a^b,c,d)]
    Y=[X[t] for t in T]
    return {(i+1,j+1):int((Y[i]*Y[j]).sum()) for i in range(5) for j in range(i+1,5)}
def explicit(X):
    L=X.sum(0); M=X.sum(1); R=X.sum(2)   # L(y,z)=sum_x, R(x,y)=sum_z
    C={}
    x,y,z=np.meshgrid(idx,idx,idx,indexing='ij')
    C[1,2]=int((X*R[x,y^z]).sum())
    C[1,3]=int((L*R).sum())                 # sum_{b,c} L(b,c)R(b,c)
    C[1,4]=int((R*R).sum())
    C[1,5]=int((X*R[x^y,z]).sum())
    C[2,3]=int((X*L[y^z,y*0+z] if False else 0))
    # C23 = sum_{b,c,d} L(b+c,d) X(b,c,d)
    C[2,3]=int((X*L[y^z,z*0+0]).sum()) if False else int(sum(X[b,c,d]*L[b^c,d] for b in idx for c in idx for d in idx))
    C[3,4]=int(sum(X[b,c,d]*L[b,c^d] for b in idx for c in idx for d in idx))
    C[3,5]=int((L*L).sum())
    # 4-sums
    C[2,4]=int(sum(X[a,u,w^c]*X[a,u^c,w] for a in idx for u in idx for w in idx for c in idx))
    C[2,5]=int(sum(X[a,b^c,d]*X[a^b,c,d] for a in idx for b in idx for c in idx for d in idx))
    C[4,5]=int(sum(X[a,b,c^d]*X[a^b,c,d] for a in idx for b in idx for c in idx for d in idx))
    return C
if __name__=='__main__':
    random.seed(5)
    v=sample([1<<i for i in range(NV)]); X=1-2*alpha_arr(v)
    B=brute(X); E=explicit(X)
    print('explicit==brute:',all(B[k]==E[k] for k in B)); print(B)
