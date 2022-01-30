S = input()
n = len(S)
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
        return fact[n]*finv[r]%mod*finv[n-r]%mod


count = [0]*26
for s in S:
    count[ord(s)-ord("a")] += 1

dp = [0]*(n+1)
dp[0] = 1
for c in count:
    ndp = [0]*(n+1)
    for i in range(c+1):
        for j in range(n+1):
            if dp[j] == 0:
                continue
            ndp[i+j] += dp[j]*nCr(i+j,i,mod)%mod
            ndp[i+j] %= mod
    dp = ndp
print((sum(dp)-1)%mod)
