S = input()
mod = 998244353
n = len(S)
dp = [0]*(n+1)
dp[0] = 1

for s in S:
    ndp = [0]*(n+1)
    for i in range(n+1):
        if dp[i] == 0:
            continue
        if s != ")":
            ndp[i+1] += dp[i]
            ndp[i+1] %= mod
        if s != "(" and i:
            ndp[i-1] += dp[i]
            ndp[i-1] %= mod
    dp = ndp
print(dp[0])