n,m = map(int,input().split())
mod = 998244353
fact = [1,1]
finv = [1,1]
inv = [0,1]
 
for i in range(2,max(n,m)+1000):
    fact.append((fact[-1]*i)%mod)
    inv.append((inv[mod%i]*(mod-mod//i))%mod)
    finv.append((finv[-1]*inv[-1])%mod)
 
def nCr(n,r,mod):
    if r > n:
        return 0
    else: 
        return fact[n]*finv[r]*finv[n-r]%mod

ans = 0
for i in range(1,m+1):
    base = 1
    now = i
    for j in range(2,int(i**0.5)+1):
        if j > now:
            break
        if now%j == 0:
            c = 0
            while now%j == 0:
                now //= j
                c += 1
            base *= nCr(c+n-1,n-1,mod)
            base %= mod
    if now != 1:
        base *= nCr(n,n-1,mod)
        base %= mod
    ans += base
    ans %= mod

print(ans)
