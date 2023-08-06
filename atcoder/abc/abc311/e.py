h,w,n = map(int,input().split())
dist = [[0]*w for i in range(h)]
hole = [[0]*w for i in range(h)]
for _ in range(n):
    a,b = [int(x)-1 for x in input().split()]
    hole[a][b] = 1

ans = 0
for i in range(h):
    for j in range(w):
        if hole[i][j]:
            dist[i][j] = 0
        else:
            dist[i][j] = min(dist[i-1][j],dist[i][j-1],dist[i-1][j-1]) + 1

            ans += dist[i][j]
print(ans)