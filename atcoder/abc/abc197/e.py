n = int(input())
l = [list(map(int,input().split())) for i in range(n)]
inf = 10**20
L = [inf]*(n+2)
R = [-inf]*(n+2)
for x,c in l:
    L[c] = min(L[c],x)
    R[c] = max(R[c],x)


L[0] = R[0] = 0
L[n+1] = R[n+1] = 0

d = []
for i,j in zip(L,R):
    if i != inf:
        d.append((i,j))

dp = [0]*2
for i,(l,r) in enumerate(d):
    ndp = [inf]*2
    for j in range(2):
        bef = d[i-1][j]
        ndp[0] = min(ndp[0],abs(r-bef)+r-l+dp[j])
        ndp[1] = min(ndp[1],abs(l-bef)+r-l+dp[j])
    dp = ndp
print(min(dp))