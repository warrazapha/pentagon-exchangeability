# Standard vs alternate Cayley-Dickson-type product at n=4: associator counts, pentagon census, bit-reversed labelling, octonion-stage zero divisor of the alternate product. Top part is exec'd by dim32_check.py and corr_check.py.
# Run from this directory: python3 alt_product_check.py   (needs numpy)
import itertools, collections
# algebra elements: dict-free lists of length 2^n ; index = standard CD index (top bit = last doubling)
def make(prod):
    def mul(x,y):
        n=len(x)
        if n==1: return [x[0]*y[0]]
        h=n//2
        a,b=x[:h],x[h:]; c,d=y[:h],y[h:]
        return prod(mul,conj,a,b,c,d)
    def conj(x):
        n=len(x)
        if n==1: return x[:]
        h=n//2
        return conj(x[:h])+[-v for v in x[h:]]
    return mul,conj
def add(u,v): return [p+q for p,q in zip(u,v)]
def sub(u,v): return [p-q for p,q in zip(u,v)]
def std(mul,conj,a,b,c,d):   # (ac - d* b, da + b c*)
    return sub(mul(a,c),mul(conj(d),b))+add(mul(d,a),mul(b,conj(c)))
def alt(mul,conj,a,b,c,d):   # (ac - b* d, d a* + b c)
    return sub(mul(a,c),mul(conj(b),d))+add(mul(d,conj(a)),mul(b,c))
def tables(prod,N=16):
    mul,_=make(prod)
    def e(i):
        v=[0]*N; v[i]=1; return v
    sig={}
    for x in range(N):
        for y in range(N):
            p=mul(e(x),e(y)); nz=[(i,v) for i,v in enumerate(p) if v]
            assert len(nz)==1 and nz[0][0]==x^y and abs(nz[0][1])==1
            sig[x,y]=nz[0][1]
    return sig
def alpha(sig):
    return {(x,y,z):sig[x,y]*sig[x^y,z]*sig[y,z]*sig[x,y^z] for x in range(16) for y in range(16) for z in range(16)}
def census(al):
    neg=sum(1 for v in al.values() if v<0)
    c=collections.Counter()
    for a,b,cc,d in itertools.product(range(16),repeat=4):
        T=[(a,b,cc),(a,b^cc,d),(b,cc,d),(a,b,cc^d),(a^b,cc,d)]
        F=tuple(i for i,t in enumerate(T) if al[t]<0)
        c[F]+=1
    sizes=collections.Counter()
    for F,n in c.items(): sizes[len(F)]+=0
    per={k:sorted(set(n for F,n in c.items() if len(F)==k)) for k in (0,2,4)}
    return neg,per,len(c),{k:sum(1 for F in c if len(F)==k) for k in (0,2,4)}
def rev(x): return int(format(x,'04b')[::-1],2)
S=tables(std); A=tables(alt)
for name,sig in (('standard',S),('alt (std indexing)',A)):
    al=alpha(sig); print(name,census(al), 'pos',sum(1 for v in al.values() if v>0))
# shuffle-basis labelling of alt: label m -> standard index rev(m)
Ash={(x,y):A[rev(x),rev(y)] for x in range(16) for y in range(16)}
alS=alpha(S); alA=alpha(Ash)
print('alt shuffle labels',census(alA))
print('disagree (alt shuffle labels vs standard labels):',sum(1 for k in alS if alS[k]!=alA[k]))
print('disagree (alt std labels vs standard):',sum(1 for k,v in alpha(A).items() if alS[k]!=v))
print('alpha(1,2,4): std',alS[1,2,4],'alt-shuffle',alA[1,2,4],'alt-std',alpha(A)[1,2,4])
# zero divisors in octonion stage of alt product?
mul,_=make(alt)
import itertools as it
def zd8():
    cnt=0
    for i,j,k,l in it.product(range(8),repeat=4):
        for s in (1,-1):
            for t in (1,-1):
                x=[0]*8; x[i]+=1; x[j]+=s
                y=[0]*8; y[k]+=1; y[l]+=t
                if any(x) and any(y) and not any(mul(x,y)):
                    return x,y
print('alt octonion-stage zero divisors:',zd8())
mul2,_=make(std)
print('std octonion zero divisors (control):',(lambda: next((1 for i,j,k,l in it.product(range(8),repeat=4) for s in (1,-1) for t in (1,-1) if (lambda x,y: any(x) and any(y) and not any(mul2(x,y)))((lambda v:(v.__setitem__(i,v[i]+1),v.__setitem__(j,v[j]+s),v)[2])([0]*8),(lambda v:(v.__setitem__(k,v[k]+1),v.__setitem__(l,v[l]+t),v)[2])([0]*8))),None))())
