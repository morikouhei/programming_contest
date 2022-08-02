n = int(input())
A = list(map(int,input().split()))
mod = 998244353

dp = [[0]*(n+2) for i in range(n+2)]

dp[0][0] = 1
for a in A:
    for i in range(n+1)[::-1]:
        for j in range(n+1):
            ni = i+1
            x = (a+j)%ni
            dp[ni][x] += dp[i][j]
            dp[ni][x] %= mod
ans = 0
for i in range(1,n+1):
    ans += dp[i][0]
    ans %= mod
print(ans)