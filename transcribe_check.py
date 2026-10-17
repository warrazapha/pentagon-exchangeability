# Checks the three displayed substitution identities on all triples for random alternative cochains and recomputes q_i, H_i (a,b,c,d = bits 1,2,4,8 gives 5,9,10,13,11).
# Run from this directory: python3 transcribe_check.py   (needs numpy)
exec(open('pairs_check.py').read().split("if __name__")[0])
random.seed(31)
cons=[alpha_lin(x,x,z) for x in rng for z in rng]+[alpha_lin(x,z,z) for x in rng for z in rng]
basis=solve(cons)
ok={'(1) a(x,y,z)=a(x,y+z,z)':True,'(2) a(x,y,z)=a(x,x+y,z)':True,'(3) a(x,y,z)=a(x+y,y,y+z)':True}
for _ in range(5):
    A=alpha_arr(sample(basis))
    for x in range(N):
        for y in range(N):
            for z in range(N):
                v=A[x,y,z]
                if v!=A[x,y^z,z]: ok['(1) a(x,y,z)=a(x,y+z,z)']=False
                if v!=A[x,x^y,z]: ok['(2) a(x,y,z)=a(x,x+y,z)']=False
                if v!=A[x^y,y,y^z]: ok['(3) a(x,y,z)=a(x+y,y,y+z)']=False
print('displayed identities hold on all triples, 5 random sigma with (L),(R):',ok)
# also derive from the substitutions d=c, b=a, c=b literally in the pentagon identity, symbolic check of which factors vanish
# q_i and H_i with a,b,c,d = bits 1,2,4,8 (the convention that reproduces 5,9,10,13,11)
bit={'a':1,'b':2,'c':4,'d':8}
def vec(s): return sum(bit[c] for c in s.replace('+',''))
T=[('a','b','c'),('a','b+c','d'),('b','c','d'),('a','b','c+d'),('a+b','c','d')]
def v(s):
    r=0
    for p in s.split('+'): r^=bit[p]
    return r
q=[v(t[0])^v(t[2]) for t in T]
print('q (a,b,c,d = bits 1,2,4,8):',q, 'expected [5,9,10,13,11]:',q==[5,9,10,13,11])
x=0
for t in q: x^=t
print('sum of q_i =',x)
def span(vs):
    S={0}
    for t in vs: S|={y^t for y in S}
    return S
H=[span([v(s) for s in t]) for t in T]
print('dims (log2 sizes):',[len(h).bit_length()-1 for h in H])
print('q_i in H_i:',all(q[i] in H[i] for i in range(5)),'; q_j in H_i for j!=i:',[ (i,j) for i in range(5) for j in range(5) if i!=j and q[j] in H[i]])
# alternative reading: a,b,c,d = bits 8,4,2,1 (msb first) gives different integers:
bit2={'a':8,'b':4,'c':2,'d':1}
def v2(s):
    r=0
    for p in s.split('+'): r^=bit2[p]
    return r
print('with a,b,c,d = bits 8,4,2,1 the q_i integers are',[v2(t[0])^v2(t[2]) for t in T])
