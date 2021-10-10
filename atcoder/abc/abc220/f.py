n = int(input())
e = [[] for i in range(n)]
for _ in range(n-1):
    u,v = [int(x)-1 for x in input().split()]
    e[u].append(v)
    e[v].append(u)

topo = []
q = [0]
par = [-1]*n
while q:
    now = q.pop()
    topo.append(now)
    for nex in e[now]:
        if par[now] == nex:
            continue
        par[nex] = now
        q.append(nex)

size = [0]*n
child = [1]*n
for now in topo[::-1]:
    for nex in e[now]:
        if nex == par[now]:
            continue
        child[now] += child[nex]
        size[now] += size[nex]+child[nex]

ans = [0]*n
ans[0] = size[0]
for now in topo[1:]:
    ans[now] = ans[par[now]]+n-2*child[now]
for i in ans:
    print(i)
