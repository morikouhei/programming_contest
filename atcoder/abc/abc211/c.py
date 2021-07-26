S = input()
mod = 10**9+7
l = "chokudai"

dp = [0]*9
dp[0] = 1
for s in S:
    for i in range(8)[::-1]:
        if s == l[i]:
            dp[i+1] += dp[i]
            dp[i+1] %= mod
print(dp[-1])