n,m,k = map(int,input().split())
mod = 10**9+7

fact = [1,1]
finv = [1,1]
inv = [0,1]
 
for i in range(2,n+m+5):
    fact.append((fact[-1]*i)%mod)
    inv.append((inv[mod%i]*(mod-mod//i))%mod)
    finv.append((finv[-1]*inv[-1])%mod)
 
def nCr(n,r,mod):
    if r > n:
        return 0
    else: 
        return fact[n]*finv[r]%mod*finv[n-r]%mod

if n > m+k:
    print(0)
else:
    print((nCr(n+m,n,mod)-nCr(n+m,m+k+1,mod))%mod)