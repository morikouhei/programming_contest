n,m = map(int,input().split())
e = [[] for i in range(n)]
for _ in range(m):
    a,b,c = map(int,input().split())
    a,b = a-1,b-1
    e[a].append([b,c])
    e[b].append([a,c])

inf = 10**20
dp = [[-inf]*n for i in range(1<<n)]
for i in range(n):
    dp[1<<i][i] = 0

ans = 0
for b in range(1<<n):
    for i in range(n):
        if dp[b][i] == -inf:
            continue
        ans = max(ans,dp[b][i])
        for ni,c in e[i]:
            if b >> ni & 1:
                continue
            dp[b|1<<ni][ni] = max(dp[b|1<<ni][ni],dp[b][i]+c)
print(ans)