from collections import deque

h,w,t = map(int,input().split())
A = [list(input()) for i in range(h)]

candys = []
for i in range(h):
    for j in range(w):
        if A[i][j] == "S":
            sx,sy = i,j
        if A[i][j] == "G":
            gx,gy = i,j

        if A[i][j] == "o":
            candys.append([i,j])


candys = [[sx,sy],[gx,gy]]+ candys

inf = 10**10
le = len(candys)
dist_all = [[inf]*le for i in range(le)]

for i in range(le):

    x,y = candys[i]

    dist = [[inf]*w for i in range(h)]
    dist[x][y] = 0
    q = deque([[x,y]])
    while q:
        nx,ny = q.popleft()

        for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nnx,nny = nx+dx,ny+dy
            if 0 <= nnx < h and 0 <= nny < w and A[nnx][nny] != "#":
                if dist[nnx][nny] > dist[nx][ny]+1:
                    dist[nnx][nny] = dist[nx][ny]+1
                    q.append([nnx,nny])


    
    for j in range(le):
        nx,ny = candys[j]
        print(x,y,nx,ny,dist[nx][ny])
        dist_all[i][j] = dist[nx][ny]




dp = [[inf]*le for i in range(1<<le)]
dp[1][0] = 0
print(candys)
ans = 0
print(dist_all)
for bi in range(1<<le):
    for i in range(le):
        if dp[bi][i] == inf:
            continue

        d = dp[bi][i]
        for j in range(le):
            if bi >> j & 1:
                continue
            nd = dist_all[i][j]+d
            if nd > t or nd >= dp[bi|1<<j][j]:
                continue
            dp[bi|1<<j][j] = nd


for bi in range(1<<le):
    if dp[bi][1] <= t:
        ans = max(ans,bin(bi).count("1")-2)
print(ans)