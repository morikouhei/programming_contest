from collections import deque
n = int(input())
C = input().split(" ")
mod = 10**9+7
e = [[] for i in range(n)]
for _ in range(n-1):
    a,b = [int(x)-1 for x in input().split()]
    e[a].append(b)
    e[b].append(a)
par = [-1]*n
topo = []
q = deque([0])
while q:
    now = q.pop()
    topo.append(now)
    for nex in e[now]:
        if par[now] == nex:
            continue
        par[nex] = now
        q.append(nex)
dp = [[-1]*3 for i in range(n)]

for x in topo[::-1]:
    id = int(C[x] == "b")
    dpx = [0]*3
    dpx[id] = 1
    dpx[2] = 1
    for nex in e[x]:
        if nex == par[x]:
            continue
        ndp = dp[nex]
        dpx[id] *= (ndp[id]+ndp[2])
        dpx[id] %= mod
        dpx[2] *= sum(ndp)+ndp[2]
        dpx[2] %= mod
    dpx[2] -= dpx[id]
    dpx[2] %= mod
    dp[x] = dpx

print(dp[0][2])