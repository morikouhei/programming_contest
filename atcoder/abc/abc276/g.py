n,m = map(int,input().split())
mod = 998244353

N = (n+m)+5
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


ans = 0

for i in range(n+1):
    left = m - i - (n-i)*2

    if left < 0:
        continue

    num = left//3
    # print(nCr(n,i) * nCr(n+num,num) % mod,i,left,num)
    ans += nCr(n,i) * nCr(n+num,num) % mod
    ans %= mod

for i in range(n):
    left = m - i - (n-1-i)*2

    if left < 0:
        continue

    num = left//3
    # print(nCr(n,i) * nCr(n+num,num) % mod,i,left,num)
    ans += nCr(n-1,i) * nCr(n+num,num) % mod
    ans %= mod
print(ans)
    