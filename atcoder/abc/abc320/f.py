n,h = map(int,input().split())
inf = 10**10
X = [0] + list(map(int,input().split()))
PF = [[inf,0]] + [list(map(int,input().split())) for i in range(n-1)]
X = X[::-1]
PF = PF[::-1]


dp = [[inf]*(h+1) for i in range(h+1)]

for i in range(1,h):
    dp[i][i] = 0

for i in range(n):
    dif = X[i]-X[i+1]
    p,f = PF[i]
    print(dif,p,f)
    ndp = [[inf]*(h+1) for i in range(h+1)]

    for j in range(h+1):
        for k in range(h+1):
            if dp[j][k] == inf:
                continue

            nj = j+dif
            nk = k-dif
            if nj <= h and nk >= 0:
                ndp[nj][nk] = min(ndp[nj][nk],dp[j][k])
            


            nj = j+dif
            nk = k-dif
            if nj <= h and nk >= 0:
                nk = min(nk+f,h)
                ndp[nj][nk] = min(ndp[nj][nk],dp[j][k]+p)


            nk = k-dif
            nj = j+dif
            if nj <= h and nk >= 0:
                nj = max(0,nj-f)
                ndp[nj][nk] = min(ndp[nj][nk],dp[j][k]+p)
    dp = ndp

ans = inf
for i in range(h+1):
    ans = min(ans,dp[h][i])
if ans == inf:
    ans = -1
print(ans)