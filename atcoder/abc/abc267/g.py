from collections import Counter
n,k = map(int,input().split())
A = list(map(int,input().split()))
mod = 998244353

N = n+5
fact = [1]*N
finv = [1]*N
 
for i in range(2,N):
    fact[i] = (fact[i-1]*i)%mod
finv[-1] = pow(fact[-1],mod-2,mod)
for i in range(1,N)[::-1]:
    finv[i-1] = (finv[i]*i)%mod

def nCr(n,r):
    if r > n:
        return 0
    else: 
        return fact[n]*finv[r]%mod*finv[n-r]%mod


C = Counter(A)

dp = [0]*(k+1)
size = 0
dp[0] = 1
for key in sorted(C.keys()):
    num = C[key]
    ndp = [0]*(k+1)
    
    for i in range(k+1):
        if dp[i] == 0:
            continue
        same = i + 1
        ad = size-i
        if ad < 0:
            break
        for j in range(num+1):
            if i+j > k:
                break
            p = nCr(ad,j) * nCr(same+num-1,num-j) * fact[num] % mod
            ndp[i+j] += dp[i]*p%mod
            ndp[i+j] %= mod
            
    dp = ndp
    size += num
print(dp[-1])