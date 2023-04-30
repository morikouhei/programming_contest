n = int(input())
AB = [list(map(int,input().split())) for i in range(n)]
mod = 998244353

dp = [1,1]

for i in range(1,n):
    a,b = AB[i-1]
    na,nb = AB[i]

    ndp = [0,0]
    if na != a:
        ndp[0] += dp[0]
    if na != b:
        ndp[0] += dp[1]
    
    if nb != a:
        ndp[1] += dp[0]
    if nb != b:
        ndp[1] += dp[1]
    dp = ndp
    dp[0] %= mod
    dp[1] %= mod
print(sum(dp)%mod)