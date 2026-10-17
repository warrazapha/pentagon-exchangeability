# For six constraint families, finds which of the ten pair correlations coincide in every sample (14 samples per family).
# Run from this directory: python3 pairs_classes.py   (needs numpy)
exec(open('pairs_check.py').read().split("if __name__")[0])
import numpy as np
fam={
 'unconstrained':[],
 'left a(x,x,z)=1':[alpha_lin(x,x,z) for x in rng for z in rng],
 'right a(x,z,z)=1':[alpha_lin(x,z,z) for x in rng for z in rng],
 'flexible a(x,y,x)=1':[alpha_lin(x,y,x) for x in rng for y in rng],
 'a(x,y,x+y)=1':[alpha_lin(x,y,x^y) for x in rng for y in rng],
 'left+right (=dep trivial)':[alpha_lin(x,x,z) for x in rng for z in rng]+[alpha_lin(x,z,z) for x in rng for z in rng],
}
random.seed(11)
keys=[(i,j) for i in range(1,6) for j in range(i+1,6)]
for name,cons in fam.items():
    basis=solve(cons); rows=[]
    for _ in range(14):
        X=1-2*alpha_arr(sample(basis)); B=brute(X); rows.append([B[k] for k in keys])
    M=np.array(rows,dtype=float)
    # equality classes across all samples
    cls=[]
    for i,k in enumerate(keys):
        for c in cls:
            if all(rows[r][i]==rows[r][keys.index(c[0])] for r in range(len(rows))): c.append(k); break
        else: cls.append([k])
    pass
    print(name); print('  equality classes:',cls); print('  rank of sample matrix:',np.linalg.matrix_rank(M),'(10 = no linear relation among the ten sums)')
    print('  distinct 10-vectors:',len(set(map(tuple,rows))))
