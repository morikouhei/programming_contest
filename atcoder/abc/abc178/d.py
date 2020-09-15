s = int(input())
mod = 10**9+7

fact = [1,1]
finv = [1,1]
inv = [0,1]
 
for i in range(2,s+5):
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
for i in range(1,s//3+1):
    x = s-3*i
    ans += nCr(i+x-1,x,mod)
    ans %= mod
print(ans)