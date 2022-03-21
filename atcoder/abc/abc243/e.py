n,m = map(int,input().split())
e = [[] for i in range(n)]
edges = []
for i in range(m):
    a,b,c = map(int,input().split())
    a -= 1
    b -= 1
    edges.append([a,b,c])

inf = 10**20
dis = [[inf]*n for i in range(n)]



for a,b,c in edges:
    dis[a][b] = dis[b][a] = c

for i in range(n):
    dis[i][i] = 0


for k in range(n):
    for i in range(n):
        for j in range(n):
            if dis[i][k] == inf or dis[k][j] == inf:
                continue
            dis[i][j] = min(dis[i][j],dis[i][k]+dis[k][j])

ans = 0
for a,b,c in edges:
    if dis[a][b] < c:
        ans += 1
        continue
    find = 0
    for i in range(n):
        if i == a or i == b:
            continue
        if dis[a][b] == dis[a][i]+dis[i][b]:
            find = 1
    ans += find
print(ans)
