n,l = map(int,input().split())
mod = 10**9+7

dp = [0]*(n+1)
dp[0] = 1
for i in range(n):
    dp[i+1] += dp[i]
    dp[i+1] %= mod
    if i+l <= n:
        dp[i+l] += dp[i]
        dp[i+l] %= mod
print(dp[n])