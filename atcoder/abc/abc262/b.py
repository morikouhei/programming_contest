n,m = map(int,input().split())
dis = [[0]*n for i in range(n)]
for i in range(m):
    u,v = map(int,input().split())
    u,v = u-1,v-1
    dis[u][v] = 1
    dis[v][u] = 1

ans = 0
for i in range(n):
    for j in range(i):
        for k in range(j):
            if dis[i][j] and dis[j][k] and dis[i][k]:
                ans += 1
print(ans)