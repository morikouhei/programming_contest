from heapq import heappop,heappush

n,m,v = map(int,input().split())
v -= 1

e = [[] for i in range(n)]
deg = [0]*n
for _ in range(m):
    a,b,c = map(int,input().split())
    a,b = a-1,b-1
    e[b].append((a,c))
    deg[a] += 1

inf = 10**15
dfirst = [inf]*n
dsecond = [0]*n

h = []
for i in range(n):
    if deg[i]:
        continue

    dfirst[i] = 0
    for nex,c in e[i]:
        if dfirst[nex] > dsecond[i]+c:
            dfirst[nex] = dsecond[i]+c
            heappush(h,[dfirst[nex],nex])
    heappush(h,[0,i])

while h:
    cost,now = heappop(h)

    if dfirst[now] != cost:
        continue

    for nex,c in e[now]:
        deg[nex] -= 1
        dsecond[nex] = max(dsecond[nex],cost+c)

        if deg[nex]:
            continue
        for nnex,c2 in e[nex]:
            if dfirst[nnex] > dsecond[nex]+c2:
                dfirst[nnex] = dsecond[nex]+c2
                heappush(h,[dfirst[nnex],nnex])


ans = dfirst[v]
if ans == inf:
    ans = "INFINITY"

print(ans)