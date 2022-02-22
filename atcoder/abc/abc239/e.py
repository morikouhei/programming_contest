from collections import deque

n,Q = map(int,input().split())
X = list(map(int,input().split()))
e = [[] for i in range(n)]
for i in range(n-1):
    a,b = [int(x)-1 for x in input().split()]
    e[a].append(b)
    e[b].append(a)


dis = [n+1]*n
par = [-1]*n
dis[0] = 0
q = deque([0])
topo = []
while q:
    now = q.pop()
    topo.append(now)
    for nex in e[now]:
        if nex == par[now]:
            continue
        dis[nex] = dis[now]+1
        par[nex] = now
        q.append(nex)
M = 21
ans = [[0]*M for i in range(n)]

for now in topo[::-1]:
    lis = [X[now]]
    for nex in e[now]:
        if par[now] == nex:
            continue
        lis += ans[nex]
    lis.sort(reverse=True)
    ans[now] = lis[:M]

for i in range(Q):
    v,k = [int(x)-1 for x in input().split()]
    print(ans[v][k])