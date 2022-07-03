import bisect
n = int(input())
S = list(map(int,input()))
W = list(map(int,input().split()))
W = [w*2 for w in W]
ans = 0

par = []
chi = []
for s,w in zip(S,W):
    if s:
        par.append(w)
    else:
        chi.append(w)

par.sort()
chi.sort()
lp = len(par)
lc = len(chi)
for p in par:

    for i in range(-1,2):
        x = p+i
        i1 = bisect.bisect_left(par,x)
        i2 = bisect.bisect_left(chi,x)
        ans = max(ans,lp-i1+i2)

for p in chi:
    
    for i in range(-1,2):
        x = p+i
        i1 = bisect.bisect_left(par,x)
        i2 = bisect.bisect_left(chi,x)
        ans = max(ans,lp-i1+i2)
print(ans)