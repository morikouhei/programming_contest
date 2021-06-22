h,w = map(int,input().split())
C = [input() for i in range(h)]
M = h*w
ans = -1
for id in range(M):
    dp = [[0]*M for i in range(1<<M)]
    dp[0][id] = 1
    for i in range(1<<M):
        for j in range(M):
            if dp[i][j] == 0:
                continue
            x,y = divmod(j,w)
            for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
                nx = x+dx
                ny = y+dy
                nid = nx*w+ny
                if 0 <= nx < h and 0 <= ny < w and C[nx][ny] != "#":
                    if i >> nid & 1:
                        continue
                    dp[i|1<<nid][nid] = 1

            if j == id:
                ans = max(ans,bin(i).count("1"))
if ans < 3:
    ans = -1
print(ans)
