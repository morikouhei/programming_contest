from collections import deque

n,m = map(int,input().split())
a = [list(input()) for i in range(n)]
sx = sy = gx = gy = float("INF")
for i in range(n):
    for j in range(m):
        if a[i][j] == "S":
            sx,sy = i,j
            a[i][j] = "0"
        if a[i][j] == "G":
            gx,gy = i,j
            a[i][j] = "10"
if sx == float("INF") or gx == float("INF"):
    print(-1)

dx = [1,-1,0,0]
dy = [0,0,1,-1]
q = deque([])
q.append([sx,sy,0])
dis = [[float("INF")]*m for i in range(n)]
dis[sx][sy] = 0
for i in range(1,11):
    g = str(i)
    while q:
        x,y,d = q.popleft()
        if a[x][y] == g:
            continue
        for j in range(4):
            nx = x+dx[j]
            ny = y+dy[j]
            if 0 <= nx < n and 0 <= ny < m:
                if dis[nx][ny] > d+1:
                    dis[nx][ny] = d+1
                    q.append([nx,ny,d+1])
    
    for j in range(n):
        for k in range(m):
            if a[j][k] == g:
                q.append([j,k,dis[j][k]])
            else:
                dis[j][k] = float("INF")

if dis[gx][gy] == float("INF"):
    print(-1)
else:
    print(dis[gx][gy])

