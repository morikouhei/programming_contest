n,x = map(int,input().split())
mod = 998244353

facts = [1]*(n+1)
for i in range(2,n+1):
    facts[i] = facts[i-1]*i%mod


x2 = 2*x-1

dp = [[0]*(1<<x2) for i in range(n+1)]

dp[0][(1<<(x-1))-1] = 1
for i in range(n):
    ndp = [[0]*(1<<x2) for j in range(n+1)]

    for j in range(i+1):
        for b in range(1<<x2):
            if dp[j][b] == 0:
                continue
            ndp[j][b//2] += dp[j][b]
            ndp[j][b//2] %= mod

            for ni in range(x2):
                if b >> ni & 1:
                    continue
                nx = i + ni - x + 1
                if nx < 0 or nx >= n:
                    continue
                nb = b | 1<<ni
                ndp[j+1][nb//2] += dp[j][b]
                ndp[j+1][nb//2] %= mod


    dp = ndp

ans = 0
f = -1
for i in range(n+1):
    f *= -1

    for b in range(1<<x2):
        ans += dp[i][b]*f*facts[n-i]
        ans %= mod
print(ans)