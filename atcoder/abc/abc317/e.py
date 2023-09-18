from collections import deque
h,w = map(int,input().split())
A = [input() for i in range(h)]
move = [[1]*w for i in range(h)]

for i in range(h):

    watch = 0
    for j in range(w):
        if A[i][j] == "S":
            sx,sy = i,j
        if A[i][j] == "G":
            gx,gy = i,j

        if A[i][j] == "#":
            move[i][j] = 0
            watch = 0
        
        elif A[i][j] == ">":
            move[i][j] = 0
            watch = 1
        
        elif A[i][j] == "." and watch:
            move[i][j] = 0
        else:
            watch = 0


    watch = 0
    for j in range(w)[::-1]:        
        if A[i][j] == "<":
            move[i][j] = 0
            watch = 1
        
        elif A[i][j] == "." and watch:
            move[i][j] = 0
        
        else:
            watch = 0
        

for j in range(w):

    watch = 0
    for i in range(h):        
        if A[i][j] == "v":
            move[i][j] = 0
            watch = 1
        
        elif A[i][j] == "." and watch:
            move[i][j] = 0
        else:
            watch = 0

    watch = 0
    for i in range(h)[::-1]:        
        if A[i][j] == "^":
            move[i][j] = 0
            watch = 1
        
        elif A[i][j] == "." and watch:
            move[i][j] = 0
        else:
            watch = 0

inf = 10**7
dist = [[inf]*w for i in range(h)]

q = deque([[sx,sy]])
dist[sx][sy] = 0
while q:
    x,y = q.popleft()

    for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
        nx,ny = x+dx,y+dy
        if 0 <= nx < h and 0 <= ny < w and move[nx][ny]:
            if dist[nx][ny] > dist[x][y]+1:
                dist[nx][ny] = dist[x][y]+1
                q.append([nx,ny])

ans = dist[gx][gy]
if ans == inf:
    ans = -1
print(ans)