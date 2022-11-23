from collections import deque

h,w = map(int,input().split())
C = [input() for i in range(h)]

par = [[-1]*w for i in range(h)]
vis = [[0]*w for i in range(h)]
for i in range(h):
    for j in range(w):
        if C[i][j] == "S":
            gx,gy = i,j

vis[gx][gy] = 1
q = deque([])
q.append([gx,gy])

while q:
    x,y = q.pop()
    vis[x][y] = 1
    # print(x,y,par[x][y])
    for dx,dy in ((1,0),(0,1),(0,-1),(-1,0)):
        nx = x+dx
        ny = y+dy
        if (nx,ny) == par[x][y]:
            continue
        if 0 <= nx < h and 0 <= ny < w and C[nx][ny] != "#":
            if nx == gx and ny == gy:
                print("Yes")
                exit()

            if vis[nx][ny]:
                continue
            # vis[nx][ny] = 1
            par[nx][ny] = (x,y)
            # print(nx,ny)
            q.append([nx,ny])

print("No")