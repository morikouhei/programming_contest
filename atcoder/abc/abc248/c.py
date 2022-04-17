n,m,k = map(int,input().split())
mod = 998244353

dp = [0]*(k+1)
dp[0] = 1
for i in range(n):
    ndp = [0]*(k+1)
    for j in range(k+1):
        for t in range(1,m+1):
            if j+t <= k:
                ndp[j+t] += dp[j]
                ndp[j+t] %= mod
    dp = ndp
print(sum(dp)%mod)