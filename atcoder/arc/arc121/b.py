import bisect
n = int(input())
inf = 10**20
R = [inf,-inf]
G = [inf,-inf]
B = [inf,-inf]
for i in range(2*n):
    a,c = input().split()
    if c == "R":
        R.append(int(a))
    elif c == "G":
        G.append(int(a))
    else:
        B.append(int(a))

if len(R)%2 == len(G)%2 == len(B)%2 == 0:
    print(0)
    exit()

R.sort()
G.sort()
B.sort()

if len(G)%2 == 0:
    R,G = G,R
elif len(B)%2 == 0:
    B,R = R,B

ans = inf
Gcand = []
for g in G:
    if abs(g) == inf:
        continue
    ind = bisect.bisect_left(B,g)
    ind2 = bisect.bisect_left(R,g)
    Gcand.append(g-R[ind2-1])
    Gcand.append(R[ind2]-g)

    ans = min(ans,g-B[ind-1],B[ind]-g)

Bcand = []
for b in B:
    if abs(b) == inf:
        continue
    ind = bisect.bisect_left(G,b)
    ind2 = bisect.bisect_left(R,b)
    Bcand.append(b-R[ind2-1])
    Bcand.append(R[ind2]-b)
    ans = min(ans,b-G[ind-1],G[ind]-b)
if Gcand and Bcand:
    ans = min(ans,min(Gcand)+min(Bcand))
print(ans)
