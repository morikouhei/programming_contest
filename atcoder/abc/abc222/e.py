from collections import deque
from collections import Counter

n,m,K = map(int,input().split())
A = list(map(int,input().split()))
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

e = [[] for i in range(n)]
for i in range(n-1):
    u,v = [int(x)-1 for x in input().split()]
    e[u].append((v,i))
    e[v].append((u,i))

count = [0]*n

def bfs(x):
    par = [-1]*n
    q = deque([x])
    while q:
        now = q.popleft()
        for nex,ind in e[now]:
            if par[now] == nex:
                continue
            par[nex] = now
            q.append(nex)
    return par

for a,na in zip(A,A[1:]):
    a,na = a-1,na-1
    par = bfs(a)
    now = na
    while now != a:
        for nex,ind in e[now]:
            if nex == par[now]:
                count[ind] += 1
                now = nex
                break
s = sum(count)
if abs(K) > s:
    print(0)
    exit()
C = Counter(count)
dp = [0]*(2*s+5)

dp[0] = 1
base = 1
for i,c in C.items():
    if i == 0:
        base *= pow(2,c-1,mod)
        continue
    ndp = [0]*(2*s+5)
    for j in range(-s,s+1):
        if dp[j] == 0:
            continue
        for k in range(c+1):
            dif = i*k-i*(c-k)
            ndp[j+dif] += dp[j]*nCr(c,k,mod)%mod
            ndp[j+dif] %= mod
    dp = ndp
print(dp[K]*base%mod)