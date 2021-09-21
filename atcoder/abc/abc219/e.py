from collections import deque
A = [list(map(int,input().split())) for i in range(4)]

ans = 0
def check(i):
    B = [[0]*4 for i in range(4)]
    for j in range(16):
        x,y = divmod(j,4)
        if i >> j & 1:
            B[x][y] = 1
        if A[x][y] and B[x][y] == 0:
            return 0
    vis = [[0]*4 for i in range(4)]
    q = deque()
    for i in range(4):
        if B[0][i] == 0:
            q.append((0,i))
            vis[0][i] = 1
        if B[-1][i] == 0:
            q.append((3,i))
            vis[-1][i] = 1
    for i in range(4):
        if B[i][0] == 0:
            q.append((i,0))
            vis[i][0] = 1
        if B[i][3] == 0:
            q.append((i,3))
            vis[i][3] = 1

    while q:
        x,y = q.popleft()
        for i,j in ((-1,0),(0,-1),(1,0),(0,1)):
            nx = x+i
            ny = y+j
            if 0 <= nx < 4 and 0 <= ny < 4 and B[nx][ny] == 0 and vis[nx][ny] == 0:
                q.append((nx,ny))
                vis[nx][ny] = 1

    for i in range(4):
        for j in range(4):
            if B[i][j] == 0 and vis[i][j] == 0:
                return 0
            if B[i][j] and len(q) == 0:
                q.append((i,j))
                B[i][j] = 0

    while q:
        x,y = q.popleft()
        for i,j in ((-1,0),(0,-1),(1,0),(0,1)):
            nx = x+i
            ny = y+j
            if 0 <= nx < 4 and 0 <= ny < 4 and B[nx][ny] == 1:
                q.append((nx,ny))
                B[nx][ny] = 0
    for i in range(4):
        for j in range(4):
            if B[i][j]:
                return 0
    return 1

for i in range(1,1<<16):
    ans += check(i)

print(ans)