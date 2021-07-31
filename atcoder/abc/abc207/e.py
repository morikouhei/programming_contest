n = int(input())
A = list(map(int,input().split()))
mod = 10**9+7

dp = [[0]*(n+2) for i in range(n+2)]
cum = 0
dp[1][0] = 1
ans = 0
for i in range(n):
    cum += A[i]
    for j in range(1,n+1)[::-1]:
        dp[j+1][cum%(j+1)] += dp[j][cum%j]
        dp[j+1][cum%(j+1)] %= mod
        if i == n-1:
            ans += dp[j][cum%j]
            ans %= mod
print(ans)