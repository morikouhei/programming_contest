n,x = map(int,input().split())
T = list(map(int,input().split()))
mod = 998244353
dp = [0]*(x+1)

invn = pow(n,mod-2,mod)
dp[0] = invn

for i in range(x):

    p = dp[i]

    np = p*invn%mod

    for t in T:
        if i+t <= x:
            dp[i+t] += np
            dp[i+t] %= mod

ans = 0
for i in range(max(x-T[0]+1,0),x+1):
    ans += dp[i]
    ans %= mod

print(ans)
