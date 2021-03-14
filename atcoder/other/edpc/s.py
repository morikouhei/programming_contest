D = int(input())
k = input()
mod = 10**9+7

dp = [[0]*2 for i in range(D+1)]
dp[0][0] += 1
for i in k:
    num = int(i)
    ndp = [[0]*2 for j in range(D+1)]
    for j in range(D+1):
        for t in range(10):
            if t == num:
                ndp[(j+t)%D][0] += dp[j][0]
                ndp[(j+t)%D][0] %= mod
            elif t < num:
                ndp[(j+t)%D][1] += dp[j][0]
            ndp[(j+t)%D][1] += dp[j][1]
            ndp[(j+t)%D][1] %= mod
    dp = ndp
print((sum(dp[0])-1)%mod)