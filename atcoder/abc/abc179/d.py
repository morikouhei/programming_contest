mod = 998244353
n,k = map(int,input().split())
K = [list(map(int,input().split())) for i in range(k)]

dp = [0]*(n+1)
dp[0] = 1
dp2 = [0]*(n+1)
for i in range(n):
    dp2[i] = (dp2[i]+dp2[i-1])%mod
    dp[i] = (dp[i]+dp2[i])%mod
    for l,r in K:
        dp2[min(i+l,n)] = (dp2[min(i+l,n)]+dp[i])%mod
        dp2[min(i+r+1,n)] = (dp2[min(i+r+1,n)]-dp[i])%mod
print(dp[n-1]%mod)
