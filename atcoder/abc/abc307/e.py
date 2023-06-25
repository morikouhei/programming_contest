n,m = map(int,input().split())
mod = 998244353

dp = [m,0]
for i in range(n-1):
    ndp = [0,0]
    ndp[0] = dp[1]
    ndp[1] = dp[0]*(m-1)%mod + dp[1]*(m-2)%mod
    ndp[1] %= mod
    dp = ndp
print(dp[1])