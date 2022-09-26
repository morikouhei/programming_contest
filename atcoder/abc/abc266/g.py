r,g,b,k = map(int,input().split())
mod = 998244353

### for bigger prime 
N = r+g+b+5
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



r -= k
g -= k
ans = 0
for i in range(min(r,g)+1):

    num = fact[r - i + g - i + b + k + i] * finv[r - i] % mod * finv[g - i] * finv[b] % mod * finv[k] * finv[i] % mod
    if i%2:
        ans -= num
    else:
        ans += num
    ans %= mod
print(ans)

