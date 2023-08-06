n = int(input())
A = [list(map(int,input())) for i in range(n)]

base = A[0][0]

dirs = [[1,0],[0,1],[-1,0],[0,-1]]

dir = 0
x,y = 0,0
while dir <= 3:
    dx,dy = dirs[dir]

    nx,ny = x+dx,y+dy

    if 0 <= nx < n and 0 <= ny < n:
        A[x][y] = A[nx][ny]
        x,y = nx,ny
    else:
        dir += 1

A[0][1] = base

for i in A:
    print(*i,sep="")