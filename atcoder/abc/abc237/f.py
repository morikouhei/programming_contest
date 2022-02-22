n,m = map(int,input().split())
mod = 998244353

dp = [[[0]*(m+2) for i in range(m+2)] for j in range(m+2)]
dp[m+1][m+1][m+1] = 1

for i in range(n):
    ndp = [[[0]*(m+2) for i in range(m+2)] for j in range(m+2)]
    for j in range(1,m+2):
        for k in range(1,j+1):
            for t in range(1,k+1):
                if dp[t][k][j] == 0:
                    continue
                for a in range(1,m+1):
                    if a <= t:
                        ndp[a][k][j] += dp[t][k][j]
                        ndp[a][k][j] %= mod
                    elif a <= k:
                        ndp[t][a][j] += dp[t][k][j]
                        ndp[t][a][j] %= mod
                    elif a <= j:
                        ndp[t][k][a] += dp[t][k][j]
                        ndp[t][k][a] %= mod
    dp = ndp

ans = 0
for i in range(1,m+1):
    for j in range(1,i):
        for k in range(1,j):
            ans += dp[k][j][i]
            ans %= mod

print(ans)
