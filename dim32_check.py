# Standard Cayley-Dickson at n=3,4,5: checks left/right alternativity of alpha and, at n=5, the full 32^4 pentagon census.
# Run from this directory: python3 dim32_check.py   (needs numpy)
exec(open('alt_product_check.py').read().split("S=tables(std)")[0])
import itertools, collections
def sig_table(prod,n):
    N_=1<<n; mul,_=make(prod)
    def e(i): v=[0]*N_; v[i]=1; return v
    sig={}
    for x in range(N_):
        ex=e(x)
        for y in range(N_):
            p=mul(ex,e(y)); i=[k for k,v in enumerate(p) if v][0]; sig[x,y]=p[i]; assert i==x^y
    return sig
for n in (3,4,5):
    sig=sig_table(std,n); N_=1<<n
    al=lambda x,y,z: sig[x,y]*sig[x^y,z]*sig[y,z]*sig[x,y^z]
    L=all(al(x,x,z)==1 for x in range(N_) for z in range(N_))
    R=all(al(x,z,z)==1 for x in range(N_) for z in range(N_))
    print('n=',n,'left alt:',L,'right alt:',R)
    if n==5:
        T=lambda a,b,c,d:[(a,b,c),(a,b^c,d),(b,c,d),(a,b,c^d),(a^b,c,d)]
        c=collections.Counter()
        import random
        for a,b,cc,d in itertools.product(range(N_),repeat=4):
            c[tuple(i for i,t in enumerate(T(a,b,cc,d)) if al(*t)<0)]+=1
        print({k:sorted(set(v for F,v in c.items() if len(F)==k)) for k in (0,2,4)}, 'patterns',len(c))
