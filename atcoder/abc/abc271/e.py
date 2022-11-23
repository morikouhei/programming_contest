n,m,k = map(int,input().split())


inf = 10**20

dist = [inf]*n
dist[0] = 0

edges = [list(map(int,input().split())) for i in range(m)]

E = list(map(int,input().split()))

for e in E:
    e -= 1

    a,b,c = edges[e]
    a,b = a-1,b-1
    if dist[a] == inf:
        continue
    dist[b] = min(dist[b],dist[a]+c)

ans = dist[-1]
if ans == inf:
    ans = -1
print(ans)