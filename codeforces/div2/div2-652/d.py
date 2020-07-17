M = 2*10**6+1
dp = [0]*(M)
mod = 10**9+7
for i in range(3,M):
    dp[i] = 2*dp[i-2]+dp[i-1]
    if i%3==0:
        dp[i] += 4
    dp[i] %= mod
t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])