q,k = map(int,input().split())
dp = [0]*(k+1)
dp[0] = 1
mod = 998244353

for _ in range(q):
    s,x = input().split()
    x = int(x)

    if s == "+":
        for i in range(x,k+1)[::-1]:
            dp[i] += dp[i-x]
            dp[i] %= mod

    else:
        for i in range(x,k+1):
            dp[i] -= dp[i-x]
            dp[i] %= mod

    print(dp[k])
