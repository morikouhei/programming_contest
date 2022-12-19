n,p = map(int,input().split())
mod = 998244353

m1 = p*pow(100,mod-2,mod)%mod
m2 = (100-p)*pow(100,mod-2,mod)%mod
dp = [0]*(n+2)
for i in range(n)[::-1]:
    count = dp[i+2]*m1+dp[i+1]*m2+1
    dp[i] = count%mod
print(dp[0])