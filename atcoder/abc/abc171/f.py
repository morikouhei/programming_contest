k = int(input())
s = list(input())

mod = 10**9+7 
fact = [1,1]
finv = [1,1]
inv = [0,1]
 
for i in range(2,k+len(s)+5):
    fact.append((fact[-1]*i)%mod)
    inv.append((inv[mod%i]*(mod-mod//i))%mod)
    finv.append((finv[-1]*inv[-1])%mod)
 
def nCr(n,r,mod):
    if r > n:
        return 0
    else: 
        return fact[n]*finv[r]*finv[n-r]%mod
t = len(s)
ans = 0
dp = [0]*(k+1)
dp[0] = 1
ans += pow(26,k)
for i in range(1,k+1):
    x = (nCr(t+i-1,t-1,mod)*pow(25,i,mod))%mod*pow(26,k-i,mod)%mod
    ans += x
    ans %= mod

print(ans%mod)
