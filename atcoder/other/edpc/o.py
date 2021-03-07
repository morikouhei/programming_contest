n = int(input())
A = [list(map(int,input().split())) for i in range(n)]
mod = 10**9+7

dp = [0]*(1<<n)
dp[0] = 1
for i in range(1<<n):
    num = bin(i).count("1")
    for j in range(n):
        if i >> j & 1:
            continue
        if A[num][j]:
            dp[i|1<<j] += dp[i]
            dp[i|1<<j] %= mod
print(dp[-1])
