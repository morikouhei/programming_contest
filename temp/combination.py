mod = 10**9+7

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

def nPr(n,r,mod):
    if r > n:
        return 0
    else: 
        return fact[n]*finv[n-r]%mod

### for small prime number 

fact = [1]
finv = [1]*(n+1)
cum_mod = [0]
for i in range(1,n+1):
    count = 0
    now = i
    while now % mod == 0:
        now //= mod
        count += 1
    fact.append((fact[-1]*now)%mod)
    cum_mod.append(cum_mod[-1]+count)
finv[n] = pow(fact[n],mod-2,mod)

for i in range(n)[::-1]:
    now = i+1
    while now % mod == 0:
        now //= mod
    finv[i] = finv[i+1]*now%mod

def nCr(n,r,mod):
    if n < r or r < 0:
        return 0
    if cum_mod[n] > cum_mod[r]+cum_mod[n-r]:
        return 0

    return fact[n]*finv[r]%mod*finv[n-r]%mod