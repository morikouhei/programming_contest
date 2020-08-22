from collections import deque

h,w = map(int,input().split())

sx,sy = map(int,input().split())
gx,gy = map(int,input().split())
sx -= 1
sy -= 1
gx -= 1
gy -= 1

l = [list(input()) for i in range(h)]

dp = [[float("INF")]*w for i in range(h)]

dp[sx][sy] = 0

q = deque([])
q.append([sx,sy])
dx = [0,0,1,-1]
dy = [1,-1,0,0]
count = 0
while True:
    cq = []
    while q:
        x,y = q.popleft()
        cq.append((x,y))
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < h and 0 <= ny < w and l[nx][ny] == "." and dp[nx][ny] > count:
                dp[nx][ny] = count
                q.append([nx,ny])
    if dp[gx][gy] < float("INF"):
        print(dp[gx][gy])
        exit()
    count += 1
    if len(cq) == 0:
        break
    for x,y in cq:
        for i in range(-2,3):
            for j in range(-2,3):
                nx = x+i
                ny = y+j
                if 0 <= nx < h and 0 <= ny < w and l[nx][ny] == "." and dp[nx][ny] > count:
                    dp[nx][ny] = count
                    q.append([nx,ny])

if dp[gx][gy] == float("INF"):
    print(-1)
