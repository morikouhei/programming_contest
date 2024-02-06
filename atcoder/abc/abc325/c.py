h,w = map(int,input().split())
S = [input() for i in range(h)]

vis = [[0]*w for i in range(h)]

ans = 0

for i in range(h):
    for j in range(w):
        if S[i][j] == "." or vis[i][j]:
            continue

        vis[i][j] = 1
        q = [[i,j]]
        ans += 1

        while q:
            x,y = q.pop()

            for dx in range(-1,2):
                for dy in range(-1,2):
                    nx,ny = x+dx,y+dy
                    if 0 <= nx < h and 0 <= ny < w:
                        if vis[nx][ny]:
                            continue
                        vis[nx][ny] = 1
                        if S[nx][ny] == "#":
                            q.append([nx,ny])

print(ans)