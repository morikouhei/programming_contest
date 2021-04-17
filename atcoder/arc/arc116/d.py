n,m = map(int,input().split())
mod = 998244353

fact = [1,1]
finv = [1,1]
inv = [0,1]
 
for i in range(2,max(n,m)+5):
    fact.append((fact[-1]*i)%mod)
    inv.append((inv[mod%i]*(mod-mod//i))%mod)
    finv.append((finv[-1]*inv[-1])%mod)
 
def nCr(n,r,mod):
    if r > n:
        return 0
    else: 
        return fact[n]*finv[r]*finv[n-r]%mod

l = m.bit_length()
dp = [0]*(m+1)
dp[0] = 1
for i in range(l):
    ndp = [0]*(m+1)
    for j in range(m+1):
        if dp[j] == 0:
            continue
        for k in range(0,m+5,2):
            if k > n or j+k*(1<<i) > m:
                break
            ndp[j+k*(1<<i)] += nCr(n, k, mod)*dp[j]
            ndp[j+k*(1<<i)] %= mod
    dp = ndp
print(dp[-1])
