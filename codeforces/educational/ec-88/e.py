n,k = map(int,input().split())
mod = 998244353

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
        return fact[n]*finv[r]*finv[n-r]%mod

def nPr(n,r,mod):
    if r > n:
        return 0
    else: 
        return fact[n]*finv[n-r]%mod
ans = 0
for i in range(1,n+1):
    x = n//i
    if x >= k:
        ans += nCr(x-1,k-1,mod)
        ans %= mod
    else:
        break
print(ans)
