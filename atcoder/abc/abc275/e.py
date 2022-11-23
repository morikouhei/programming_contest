n,m,k = map(int,input().split())
mod = 998244353
dp = [0]*(n+1)
dp[0] = 1
ans = 0
invm = pow(m,mod-2,mod)
for i in range(k):
    ndp = [0]*(n+1)
    for j in range(n):
        if dp[j] == 0:
            continue
        p = dp[j]*invm%mod
        for k in range(j+1,j+m+1):
            if k <= n:
                ndp[k] += p
                ndp[k] %= mod
            else:
                ndp[n-k-1] += p
                ndp[n-k-1] %= mod
    ans += ndp[-1]
    ans %= mod
    dp = ndp
print(ans)