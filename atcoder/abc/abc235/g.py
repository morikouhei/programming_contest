n,a,b,c = map(int,input().split())

mod = 998244353

fact = [1,1]
finv = [1,1]
inv = [0,1]
 
for i in range(2,n+5):
    fact.append((fact[-1]*i)%mod)
    inv.append((inv[mod%i]*(mod-mod//i))%mod)
    finv.append((finv[-1]*inv[-1])%mod)
 
def nCr(n,r,mod=mod):
    if r > n:
        return 0
    else: 
        return fact[n]*finv[r]%mod*finv[n-r]%mod


ans = 0
numa,numb,numc = 1,1,1
sign = 1 if n%2 == 0 else -1

for i in range(n+1):
    count = nCr(n,i)*numa%mod*numb%mod*numc%mod
    ans += count*sign
    ans %= mod

    numa += numa-nCr(i,a)
    numa %= mod
    numb += numb-nCr(i,b)
    numb %= mod
    numc += numc-nCr(i,c)
    numc %= mod

    sign *= -1
print(ans)