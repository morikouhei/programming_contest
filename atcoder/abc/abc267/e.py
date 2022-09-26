from collections import deque
from heapq import heappop,heappush
n,m = map(int,input().split())
A = list(map(int,input().split()))

e = [[] for i in range(n)]

base = [0]*n
for _ in range(m):
    u,v = map(int,input().split())
    u,v = u-1,v-1
    e[u].append(v)
    e[v].append(u)
    base[v] += A[u]
    base[u] += A[v]


cost = [0]*n
vis = [-1]*n
mod = 1<<20
def calc(x,t):

    # vis = [0]*n
    # cost = base[:]
    q = []
    for i in range(n):
        cost[i] = base[i]
        if cost[i] <= x:
            heappush(q,-(A[i]<<20)-i)
            vis[i] = t
    print(cost)
    while q:
        now = -heappop(q)
        now = now%mod
        # print(now)
        for nex in e[now]:
            cost[nex] -= A[now]
        for nex in e[now]:
            if vis[nex] == t or cost[nex] > x:
                continue
            heappush(q,-(A[nex]<<20)-nex)
            vis[nex] = t
    if sum(vis) == t*n:
        return 1
    else:
        return 0

t = 0

cands = [0]+base[:]+[10**15]
l = 0
r = 10**15
while r > l + 1:
    m = (r+l)//2
    if calc(m,t):
        r = m
    else:
        l = m
    t += 1
print(r)