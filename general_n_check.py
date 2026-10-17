# Random cochains satisfying left+right alternativity at n=3,4,5 (exact linear solution space): pentagon census by flip-set size.
# Run from this directory: python3 general_n_check.py   (needs numpy)
import numpy as np, random, itertools, collections, sys
def run(n,samples,seed):
    N=1<<n; var={}
    for x in range(1,N):
        for y in range(1,N): var[x,y]=len(var)
    NV=len(var)
    def lin(x,y): return 0 if x==0 or y==0 else 1<<var[x,y]
    def al(x,y,z): return lin(x,y)^lin(x^y,z)^lin(y,z)^lin(x,y^z)
    cons=[al(x,x,z) for x in range(1,N) for z in range(1,N)]+[al(x,z,z) for x in range(1,N) for z in range(1,N)]
    piv={}
    for m in cons:
        for p in sorted(piv,reverse=True):
            if m>>p&1: m^=piv[p]
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
    print(f'n={n}: variables {NV}, free (solution space dim) {len(basis)}')
    random.seed(seed)
    idx=np.arange(N)
    g=np.array(np.meshgrid(idx,idx,idx,idx,indexing='ij')).reshape(4,-1); a,b,c,d=g
    for _ in range(samples):
        v=0
        for bv in basis:
            if random.random()<.5: v^=bv
        s=np.zeros((N,N),dtype=np.int64)
        for (x,y),k in var.items(): s[x,y]=v>>k&1
        X3,Y3,Z3=np.meshgrid(idx,idx,idx,indexing='ij')
        A=s[X3,Y3]^s[X3^Y3,Z3]^s[Y3,Z3]^s[X3,Y3^Z3]
        T=[(a,b,c),(a,b^c,d),(b,c,d),(a,b,c^d),(a^b,c,d)]
        code=np.zeros(a.shape,dtype=np.int64)
        for i,t in enumerate(T): code+=A[t]<<i
        cnt=np.bincount(code,minlength=32)
        bysize=collections.defaultdict(set)
        for m in range(32):
            if cnt[m] or bin(m).count('1')%2==0: bysize[bin(m).count('1')].add(int(cnt[m]))
        odd=any(cnt[m] for m in range(32) if bin(m).count('1')%2)
        print('  sample: counts by flip-set size',{k:sorted(v) for k,v in sorted(bysize.items()) if k%2==0},'odd-weight patterns present:',odd,'neg triples',int(A.sum()))
run(3,3,1)
run(4,2,2)
run(5,2,3)
