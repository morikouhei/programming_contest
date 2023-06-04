n,m = map(int,input().split())
mod = 998244353

if n > 60:
    print(0)
    exit()

dp = [1]*61

for i in range(n):
    ndp = [0]*61

    for j in range(60):
        if 1 << j > m:
            break

        pat = min(1<<j,m-(1<<j)+1)
        ndp[j] += dp[j-1]*pat%mod
    
    dp = ndp
    for j in range(59):
        dp[j+1] += dp[j]
        dp[j+1] %= mod

print(dp[-2])