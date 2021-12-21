n,k = map(int,input().split())
A = list(map(int,input().split()))
mod = 998244353 

dp = [0]*(n+1)
dp[0] = 1
for i in range(n):
    ndp = [0]*(n+1)
    for j in range(n+1):
        ndp[j] += dp[j]*A[i]
        ndp[j] %= mod
        if j != n:
            ndp[j+1] += dp[j]*(k-j)
            ndp[j+1] %= mod
    dp = ndp

ans = 0
for i in range(n+1):
    if k-i >= 0:
        ans += dp[i]*pow(n,k-i,mod)%mod
        ans %= mod

base = pow(n,k,mod)
ans *= pow(base,mod-2,mod)
ans %= mod
print(ans)