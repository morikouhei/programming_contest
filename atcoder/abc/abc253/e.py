n,m,k = map(int,input().split())
mod = 998244353

if k == 0:
    print(pow(m,n,mod))
    exit()
dp = [1]*m

for i in range(n-1):
    ndp = [0]*m
    s = sum(dp)%mod
    ndp[0] += s
    for j in range(m):
        x = dp[j]
        ndp[max(0,j-k+1)] -= x
        ndp[max(0,j-k+1)] %= mod
        if j+k < m:
            ndp[j+k] += x
            ndp[j+k] %= mod

    for j in range(m-1):
        ndp[j+1] += ndp[j]
        ndp[j+1] %= mod
    dp = ndp

print(sum(dp)%mod)