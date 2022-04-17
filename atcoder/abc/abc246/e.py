from collections import deque

n = int(input())
sx,sy = [int(x)-1 for x in input().split()]
gx,gy = [int(x)-1 for x in input().split()]
S = [input() for i in range(n)]

inf = 10**9
dis = [[[inf]*4 for i in range(n)] for j in range(n)]

q = deque()
dx = [1,1,-1,-1]
dy = [1,-1,1,-1]

for i in range(4):
    dis[sx][sy][i] = 1
    q.append([sx,sy,i])

while q:
    x,y,dir = q.popleft()
    d = dis[x][y][dir]
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0 <= nx < n and 0 <= ny < n and S[nx][ny] != "#":
            dd = 0 if dir == i else 1

            if dis[nx][ny][i] > d + dd:
                dis[nx][ny][i] = d + dd
                if dd == 0:
                    q.appendleft([nx,ny,i])
                else:
                    q.append([nx,ny,i])

ans = min(dis[gx][gy])
if ans == inf:
    ans = -1
print(ans)