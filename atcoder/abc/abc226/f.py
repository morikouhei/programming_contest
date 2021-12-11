import math
n,K = map(int,input().split())
mod = 998244353

### for bigger prime 
fact = [1,1]
finv = [1,1]
inv = [0,1]
 
for i in range(2,n+5):
    fact.append((fact[-1]*i)%mod)
    inv.append((inv[mod%i]*(mod-mod//i))%mod)
    finv.append((finv[-1]*inv[-1])%mod)
 
def nCr(n,r,mod):
    if r > n:
        return 0
    else: 
        return fact[n]*finv[r]%mod*finv[n-r]%mod

dp = [{} for i in range(n+1)]
dp[0][1] = 1

for i in range(n):
    for k,v in dp[i].items():
        for j in range(1,n-i+1):
            nk = k*j//(math.gcd(k,j))
            dp[i+j][nk] = (dp[i+j].get(nk,0)+v*nCr(n-1-i,j-1,mod)%mod*fact[j-1]%mod)%mod

ans = 0
for k,v in dp[n].items():
    ans += pow(k,K,mod)*v%mod
    ans %= mod
print(ans)