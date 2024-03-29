n,m,k = map(int,input().split())

mod = 998244353

### for bigger prime 
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

edges = [0]*n
for _ in range(m):
    u,v = [int(x)-1 for x in input().split()]
    edges[u] += 1
    edges[v] += 1

div = [0]*2
for e in edges:
    div[e%2] += 1


ans = 0
for i in range(0,k+1,2):
    if div[1] < i or div[0] < (k-i):
        continue
    ans += nCr(div[1],i)*nCr(div[0],k-i)
    ans %= mod
print(ans)