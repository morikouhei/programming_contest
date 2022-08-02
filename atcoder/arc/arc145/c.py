n = int(input())
mod = 998244353

### for bigger prime 
N = 2*n+5
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


ans = nCr(2*n,n)*pow(n+1,mod-2,mod)%mod*pow(2,n,mod)*fact[n]%mod
print(ans)