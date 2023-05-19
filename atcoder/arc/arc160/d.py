n,m,k = map(int,input().split())
mod = 998244353

if m%k:
    print(0)
    exit()

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

size = 2*n - k + 1

## 2n-k+1個に mk 個を配る
## 2n-k+mk C mk-1
## i 個が k 個以上配られている時は 2n-k+1 個に mk - ik 
## 2n-k + mk - ik C mk-ik-1


a = 2*n - k + m//k
b = 2*n - k

ans = 0
chi = 1
for i in range(1,b+1):
    chi *= i
    chi %= mod
# print(a,b)
inv = pow(chi,mod-2,mod)
for i in range(n-k+2):

    if a - i*k < 0:
        continue
    par = 1
    for j in range(b):
        par *= a-i*k-j
        par %= mod
    
    if i%2:
        ans -= par*inv%mod*nCr(n-k+1,i)%mod
    else:
        ans += par*inv%mod*nCr(n-k+1,i)%mod
    ans %= mod
print(ans)
    