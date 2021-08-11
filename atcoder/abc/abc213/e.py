from collections import deque
h,w = map(int,input().split())
S = [input() for i in range(h)]
dis = [[h*w+5]*w for i in range(h)]
dis[0][0] = 0

q = deque([[0,0]])
now = [[0,0]]
while now:
    nex = []
    while q:
        x,y = q.popleft()
        for i,j in zip([0,1,0,-1],[-1,0,1,0]):
            nx = x+i
            ny = y+j
            if 0 <= nx < h and 0 <= ny < w and S[nx][ny] == "." and dis[nx][ny] > dis[x][y]:
                dis[nx][ny] = dis[x][y]
                now.append([nx,ny])
                q.append([nx,ny])
    for x,y in now:
        for i in range(-2,3):
            for j in range(-2,3):
                if abs(i)+abs(j) > 3:
                    continue
                nx = x+i
                ny = y+j
                if 0 <= nx < h and 0 <= ny < w and S[nx][ny] == "#" and dis[nx][ny] > dis[x][y]+1:
                    dis[nx][ny] = dis[x][y]+1
                    nex.append([nx,ny])
                    q.append([nx,ny])
    now = nex
print(dis[-1][-1])

