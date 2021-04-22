n = int(input())
mod = 10**9+7

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

ans = [0]*(n+1)

for i in range(1,n+1):
    for j in range(1,n+1):
        if (i-1)*(j-1)+i > n:
            break
        ans[j] += nCr(n-(i-1)*(j-1), i, mod)
        ans[j] %= mod
for i in ans[1:]:
    print(i)