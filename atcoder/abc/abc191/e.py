from heapq import heappush, heappop
n,m = map(int,input().split())
e = [[] for i in range(n)]

for i in range(m):
    a,b,c = map(int,input().split())
    e[a-1].append((b-1,c))
inf = 10**20

def Dijkstra(x):
    dis = [inf]*n
    h = []
    for i,c in e[x]:
        if c < dis[i]:
            dis[i] = c
            h.append((c,i))
    while h:
        cos,now = heappop(h)
        if dis[now] < cos:
            continue
        for nex, c in e[now]:
            if cos+c < dis[nex]:
                dis[nex] = cos+c
                heappush(h, (cos+c,nex))
    return dis[x]

for i in range(n):
    ans = Dijkstra(i)
    if ans == inf:
        ans = -1
    print(ans)