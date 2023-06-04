n = int(input())
e = [[] for i in range(n)]
edges = [0]*n
for _ in range(n-1):
    u,v = [int(x)-1 for x in input().split()]
    e[u].append(v)
    e[v].append(u)

    edges[u] += 1
    edges[v] += 1

ans = []
dist = [n+1]*n
q = []
for i in range(n):
    if edges[i] == 1:
        q.append(i)
        dist[i] = 0
        break

while q:
    now = q.pop()
    for nex in e[now]:
        if dist[nex] > dist[now]+1:
            dist[nex] = dist[now]+1
            q.append(nex)


for i in range(n):
    if dist[i]%3 == 1:
        ans.append(edges[i])
print(*sorted(ans))