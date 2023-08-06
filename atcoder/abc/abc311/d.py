n,m = map(int,input().split())
S = [input() for i in range(n)]

vis = [[0]*m for i in range(n)]
stop = [[0]*m for i in range(n)]
q = [[1,1]]
vis[1][1] = 1
stop[1][1] = 1
while q:
    x,y = q.pop()

    for dx,dy in ((-1,0),(0,1),(1,0),(0,-1)):

        nx,ny = x,y
        while 0 <= nx < n and 0 <= ny < m and S[nx][ny] == ".":
            vis[nx][ny] = 1
            lx,ly = nx,ny
            nx,ny = nx+dx,ny+dy

        if stop[lx][ly] == 0:
            stop[lx][ly] = 1
            q.append([lx,ly])


ans = 0
for i in range(n):
    ans += sum(vis[i])
print(ans)