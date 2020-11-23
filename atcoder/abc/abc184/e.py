from collections import deque
import sys
sys.setrecursionlimit(10**7)
h,w = map(int,input().split())
s = [list(input()) for i in range(h)]

l = [[] for i in range(26)]
for i in range(h):
    for j in range(w):
        if s[i][j] == "S":
            sx,sy = i,j
            continue
        if s[i][j] == "G":
            gx,gy = i,j
            continue
        if s[i][j] == "." or s[i][j] == "#":
            continue
        t = s[i][j]
        l[ord(t)-ord("a")].append((i,j))

al = list("abcdefghijklmnopqrstuvwxyz")
dis = [[10**10]*w for i in range(h)]
dis[sx][sy] = 0
use = [0]*26
q = deque([(sx,sy)])
dx = [1,-1,0,0]
dy = [0,0,1,-1] 
while q:
    x,y = q.popleft()
    t = s[x][y]

    if t in al and use[ord(t)-ord("a")] == 0:
        use[ord(t)-ord("a")] = 1
        d = dis[x][y]
        for i,j in l[ord(t)-ord("a")]:
            if dis[i][j] > d+1:
                dis[i][j] = d+1
                q.append((i,j))
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < h and 0 <= ny < w and s[nx][ny] != "#":
            if dis[nx][ny] > dis[x][y]+1:
                dis[nx][ny] = dis[x][y]+1
                q.append((nx,ny))

if dis[gx][gy] == 10**10:
    print(-1)
else:
    print(dis[gx][gy]) 
