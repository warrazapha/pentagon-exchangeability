# Random normalized cochains without alternativity: parity holds, uniformity fails.
# Run from this directory: python3 random_cochain_check.py   (needs numpy)
import random, itertools, collections
def run(sig):
    al={(x,y,z):sig[x,y]*sig[x^y,z]*sig[y,z]*sig[x,y^z] for x in range(16) for y in range(16) for z in range(16)}
    c=collections.Counter()
    for a,b,cc,d in itertools.product(range(16),repeat=4):
        T=[(a,b,cc),(a,b^cc,d),(b,cc,d),(a,b,cc^d),(a^b,cc,d)]
        c[tuple(i for i,t in enumerate(T) if al[t]<0)]+=1
    return c
random.seed(1)
for trial in range(6):
    sig={(x,y):(1 if x==0 or y==0 else random.choice((1,-1))) for x in range(16) for y in range(16)}
    c=run(sig)
    print({k:sorted(set(n for F,n in c.items() if len(F)==k)) for k in (0,2,4)}, 'sizes odd?',any(len(F)%2 for F in c))
# bilinear-type twist: sigma(x,y)=(-1)^{B(x,y)} (a coboundary-trivial alpha=+1 case) and a quadratic-type one
