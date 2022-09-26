h,w = map(int,input().split())
G = [input() for i in range(h)]

vis = [[0]*w for i in range(h)]

x,y = 0,0
vis[x][y] = 1
c = "UDLR"
dx = [-1,1,0,0]
dy = [0,0,-1,1]
while True:
    cind = c.find(G[x][y])

    nx,ny = x+dx[cind],y+dy[cind]

    if 0 <= nx < h and 0 <= ny < w:
        if vis[nx][ny]:
            print(-1)
            exit()
        vis[nx][ny] = 1
        x,y = nx,ny
    else:
        print(x+1,y+1)
        exit()
