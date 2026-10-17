# Two explicit normalized cochains on F_2^4 showing that ONE alternativity condition is not enough.
# sigma(x,y) = (-1)^bit, bit index = (x-1)*15 + (y-1) for x,y in 1..15 (sigma(0,.)=sigma(.,0)=1).
# Run: python3 counterexamples.py   (standard library only)
import itertools, collections
MASKS = {'left only (L holds, R fails)': 0xbcf62f8df145e1ad13d8243333b14eb4b5065d533660078b540052d5, 'right only (R holds, L fails)': 0x157bb032ce4155857fb6a301f460887deb7d1a25427347aef8c21a305}
def make(mask):
    def s(x,y):
        return 0 if x==0 or y==0 else (mask >> ((x-1)*15 + (y-1))) & 1
    def a(x,y,z): return s(x,y) ^ s(x^y,z) ^ s(y,z) ^ s(x,y^z)
    return a
for name,mask in MASKS.items():
    a = make(mask); R16 = range(16)
    L_ok = all(a(x,x,z)==0 for x in R16 for z in R16)
    R_ok = all(a(x,z,z)==0 for x in R16 for z in R16)
    c = collections.Counter()
    for q in itertools.product(R16, repeat=4):
        A,B,C,D = q
        T = [(A,B,C),(A,B^C,D),(B,C,D),(A,B,C^D),(A^B,C,D)]
        c[tuple(i for i,t in enumerate(T) if a(*t))] += 1
    sizes = {k: sorted(set(v for F,v in c.items() if len(F)==k)) for k in (0,2,4)}
    print(name); print('  (L) holds:',L_ok,'  (R) holds:',R_ok)
    print('  distinct counts by flip-set size:',sizes,'  -> uniform:',all(len(v)==1 for v in sizes.values()))
