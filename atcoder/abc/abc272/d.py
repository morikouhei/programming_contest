from collections import deque

n,m = map(int,input().split())

moves = []

for i in range(n):
    for j in range(n):
        if i**2+j**2 == m:
            moves.append([i,j])
inf = 10**10
dist = [[inf]*n for i in range(n)]
dist[0][0] = 0

q = deque([])
q.append([0,0])
while q:
    x,y = q.popleft()

    for dx,dy in moves:
        
        for px,py in ((1,1),(1,-1),(-1,1),(-1,-1)):

            nx = x+dx*px
            ny = y+dy*py
            if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == inf:
                dist[nx][ny] = dist[x][y]+1
                q.append([nx,ny])

for i in range(n):
    for j in range(n):
        if dist[i][j] == inf:
            dist[i][j] = -1
    print(*dist[i])
