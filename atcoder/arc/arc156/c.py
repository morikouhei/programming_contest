n = int(input())
deg = [0]*n
e = [[] for i in range(n)]

for _ in range(n-1):
    u,v = [int(x)-1 for x in input().split()]
    e[u].append(v)
    e[v].append(u)
    deg[u] += 1
    deg[v] += 1


P = [i+1 for i in range(n)]

q = []
for i,d in enumerate(deg):
    if d == 1:
        q.append(i)

while len(q) >= 2:
    u = q.pop()
    v = q.pop()
    P[u],P[v] = P[v],P[u]

    for nex in e[u]:
        deg[nex] -= 1
        if deg[nex] == 1:
            q.append(nex)
    for nex in e[v]:
        deg[nex] -= 1
        if deg[nex] == 1:
            q.append(nex)
print(*P)