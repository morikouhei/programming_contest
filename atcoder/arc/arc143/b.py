n,m = map(int,input().split())
XY = [list(map(int,input().split())) for i in range(m)]


S = [[[],[]] for i in range(2)]

for x,y in XY:
    d = (x+y)%2
    S[d][0].append(y-x)
    S[d][1].append(x+y)

ans = 0

for t in range(2):
    sp = set(S[t][0])
    sm = set(S[t][1])
    L = []
    for p in sp:
        ans += n-abs(p)
        L.append([abs(p),1])
        L.append([2*n-abs(p)+1,-1])
    L.sort()
    sm = sorted(sm)
    count = 0
    now = 0
    for m in sm:
        while now < len(L) and L[now][0] <= m:
            count += L[now][1]
            now += 1

        base = n-abs(n+1-m)
        ans += base-count
print(ans)
