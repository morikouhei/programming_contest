n,m = map(int,input().split())
mod = 998244353

comb = [[0]*(n+1) for i in range(n+1)]
for i in range(n+1):
    comb[i][0] = 1
    comb[i][i] = 1
    for j in range(1,i):
        comb[i][j] = (comb[i-1][j]+comb[i-1][j-1])%mod

dp = [[0]*(m+1) for i in range(n+1)]
dp[0][0] = 1

for i in range(n):

    ndp = [[0]*(m+1) for j in range(n+1)]

    for j in range(n+1):
        for k in range(m+1):
            if dp[j][k] == 0:
                continue

            nj = j+1
            for x in range(j+1):
                nk = x + k
                if nk > m:
                    break
                ndp[nj][nk] += dp[j][k] * comb[j][x] % mod
                ndp[nj][nk] %= mod

            nj = j
            for x in range(i-j+1):
                nk = x + k + j
                if nk > m:
                    break
                ndp[nj][nk] += dp[j][k] * comb[i-j][x] % mod
                ndp[nj][nk] %= mod
    dp = ndp

ans = 0
for i in range(1,n+1):
    ans += dp[i][m]
    ans %= mod
print(ans)
