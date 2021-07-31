from collections import deque

n,m,k = map(int,input().split())
mod = 998244353
e = [[] for i in range(n)]
for i in range(n):
    e[i].append(i)
for _ in range(m):
    u,v = [int(x)-1 for x in input().split()]
    e[u].append(v)
    e[v].append(u)


ans = [1]*n
ans[0] = 0
base = 1
for i in range(k):
    nbase = 0
    nans = [0]*n
    for now in range(n):
        num = (base-ans[now])%mod
        nbase += num
        nbase %= mod
        for nex in e[now]:
            nans[nex] += num
            nans[nex] %= mod
    ans = nans
    base = nbase

print((base-ans[0])%mod)