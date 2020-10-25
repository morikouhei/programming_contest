n,k = map(int,input().split())
mod = 998244353

fact = [1,1]
finv = [1,1]
inv = [0,1]
 
for i in range(2,k+5):
    fact.append((fact[-1]*i)%mod)
    inv.append((inv[mod%i]*(mod-mod//i))%mod)
    finv.append((finv[-1]*inv[-1])%mod)
 
def nCr(n,r,mod):
    if r > n:
        return 0
    else: 
        return fact[n]*finv[r]*finv[n-r]%mod


a = list(map(int,input().split()))

count = [0]*(k+1)
for i in a:
    x = 1
    for j in range(k+1):
        count[j] += x
        count[j] %= mod
        x *= i
        x %= mod

pow2 = 2
for i in range(1,k+1):
    ans = 0
    for j in range(i+1):
        ans += count[j]*count[i-j]%mod*nCr(i,j,mod)%mod
        ans %= mod
    ans -= pow2*count[i]
    ans %= mod
    ans *= pow(2,mod-2,mod)
    ans %= mod
    pow2 *= 2
    pow2 %= mod
    print(ans)