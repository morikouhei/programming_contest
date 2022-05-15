n,mod = map(int,input().split())

dp = [[0]*(n+1) for i in range(n+1)]

for di,dj in zip((1,10,100,1000),(2,3,4,5)):
    if dj > n:
        break
    if di <= n:
        dp[di][dj] += 26
        dp[di][dj] %= mod
    if di*10 <= n:
        dp[di*10][dj] -= 26
        dp[di*10][dj] %= mod
for i in range(n+1):
    for j in range(n+1):
        dp[i][j] += dp[i-1][j]
        dp[i][j] %= mod

        if dp[i][j] == 0:
            continue
        num = dp[i][j]*25%mod
        for di,dj in zip((1,10,100,1000),(2,3,4,5)):
            if j+dj > n:
                break
            if i+di <= n:
                dp[i+di][j+dj] += num
                dp[i+di][j+dj] %= mod
            if i+di*10 <= n:
                dp[i+di*10][j+dj] -= num
                dp[i+di*10][j+dj] %= mod

ans = sum(dp[-1][:n])%mod
print(ans)
