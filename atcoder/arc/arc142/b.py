n = int(input())

ans = [[0]*n for i in range(n)]
now = 0
edge = n
X,Y = 0,0
dx = [0,1,0,-1]
dy = [1,0,-1,0]
while edge > 0:
    nex = (edge-1)*4
    L = now+1
    R = now+nex
    dir = 0
    ans[X][Y] = L
    x,y = X,Y

    while L < R:

        nx = x+dx[dir]*2
        ny = y+dy[dir]*2
        nnx = x+dx[dir]
        nny = y+dy[dir]
        if 0 <= nx < n and 0 <= ny < n and ans[nx][ny] == 0:
            L += 1
            ans[nx][ny] = L
            L += 1
            ans[nnx][nny] = L
            x,y = nx,ny
        elif 0 <= nnx < n and 0 <= nny < n and ans[nnx][nny] == 0:
            L += 1
            ans[nnx][nny] = L
            x,y = nnx,nny
        else:
            dir += 1

    now = R
    edge -= 2

    X,Y = X+1,Y+1

for i in ans:
    print(*i)
    
# for i in range(n):
#     for j in range(n):
#         mi = 0
#         ma = 0
#         for x in range(-1,2):
#             for y in range(-1,2):
#                 nx = i+x
#                 ny = j+y
#                 if 0 <= nx < n and 0 <= ny < n:
#                     if ans[nx][ny] < ans[i][j]:
#                         mi += 1
#                     elif ans[nx][ny] > ans[i][j]:
#                         ma += 1
#         if mi == ma:
#             print(i,j)
#             exit()