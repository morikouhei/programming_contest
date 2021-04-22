from heapq import heappop, heappush

n,m = map(int,input().split())
e = [[] for i in range(n+1)]
for i in range(m):
    a,b,c = map(int,input().split())
    e[a].append((b,c))
    e[b].append((a,c))

inf = 10**20
def dijkstra(x):
    dp = [inf]*(n+1)
    h = [[0,x]]
    while h:
        dis,now = heappop(h)
        if dis >= dp[now]:
            continue
        dp[now] = dis
        for nex,c in e[now]:
            if dp[nex] > dis+c:
                heappush(h, [dis+c,nex])

    return dp

dis1 = dijkstra(1)
disn = dijkstra(n)

for i in range(1,n+1):
    print(dis1[i]+disn[i])