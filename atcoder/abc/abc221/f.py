from collections import deque

n = int(input())
mod = 998244353
n2 = 2*n
e = [[] for i in range(n2)]
for i in range(n-1):
    u,v = [int(x)-1 for x in input().split()]
    e[n+i].append(u)
    e[n+i].append(v)
    e[u].append(n+i)
    e[v].append(n+i)

def bfs(x):
    dis = [n2]*(n2-1)
    par = [-1]*(n2-1)
    dis[x] = 0
    q = deque([x])
    while q:
        now = q.popleft()
        for nex in e[now]:
            if dis[nex] > dis[now]+1:
                dis[nex] = dis[now]+1
                par[nex] = now
                q.append(nex)
    return dis,par

dis0,par0 = bfs(0)
dis,par = bfs(dis0.index(max(dis0)))
d = max(dis)
d2 = d//2
center = dis.index(d)
for i in range(d2):
    center = par[center]


dis2,_ = bfs(center)
cand = []
ans = 1
count = 0
for i in e[center]:
    par = 0
    q = deque([i])
    while q:
        now = q.popleft()
        if dis2[now] == d2:
                par += 1
        for nex in e[now]:
            if dis2[nex] < dis2[now]:
                continue
            q.append(nex)
    count += par
    ans *= par+1
    ans %= mod
print((ans-count-1)%mod)
    