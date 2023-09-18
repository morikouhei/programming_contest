n = int(input())
XY = [list(map(int,input().split())) for i in range(n)]
lim = 30
inf = 10**20
dp = [[inf]*lim for i in range(n)]

dp[0][0] = 0

for i in range(n-1):
    x,y = XY[i]

    for j in range(lim):
        if dp[i][j] == inf:
            continue

        for nj in range(j,lim):
            ni = i + nj+1-j
            if ni >= n:
                continue

            nx,ny = XY[ni]

            d = ((x-nx)**2 + (y-ny)**2)**0.5

            dp[ni][nj] = min(dp[ni][nj],dp[i][j]+d)


ans = inf
for i in range(lim):
    if i == 0:
        ans = min(ans,dp[-1][i])
    else:
        ans = min(ans,dp[-1][i]+(1<<(i-1)))
print(ans)
