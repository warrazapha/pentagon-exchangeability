# 60 random cochains with alpha trivial on dependent triples: reports non-uniform samples (expected 0) and distinct count triples.
# Run from this directory: python3 uniformity_probe_dep.py   (needs numpy)
exec(open("uniformity_probe.py").read().split("dep=[")[0])
rng=range(1,N)
dep=[alpha_lin(x,y,z) for x in range(N) for y in range(N) for z in range(N) if rank_dep(x,y,z)<8]
lr=[alpha_lin(x,x,z) for x in rng for z in rng]+[alpha_lin(x,z,z) for x in rng for z in rng]
def span(ms):
    piv={}
    for m in ms:
        for p,r in sorted(piv.items(),reverse=True):
            if m>>p&1: m^=r
        if m: piv[m.bit_length()-1]=m
    return len(piv)
print('rank dep',span(dep),'rank lr',span(lr),'rank both',span(dep+lr))
basis=solve(dep)
random.seed(7)
bad=0; seen=set()
for i in range(60):
    r,al=census(sample(basis))
    ok=all(len(v)==1 for v in r.values())
    seen.add((r[0][0],r[2][0],r[4][0]))
    if not ok: bad+=1; print('NONUNIFORM',r)
print('nonuniform samples:',bad,'of 60; distinct (nf,2f,4f) triples seen:',len(seen))
# cosets of alpha-triviality: also check that census values satisfy 15136-like identity
for t in sorted(seen)[:5]: print(t, t[0]+10*t[1]+5*t[2])
