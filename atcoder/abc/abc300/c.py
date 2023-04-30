h,w = map(int,input().split())
C = [input() for i in range(h)]

ans = [0]*min(h,w)

dirs = [[1,-1],[1,1],[-1,1],[-1,-1]]

for i in range(h):
    for j in range(w):
        if C[i][j] == ".":
            continue

        x,y = i,j
        num = 0
        for dx,dy in dirs:
            nx = x+dx
            ny = y+dy
            if 0 <= nx < h and 0 <= ny < w and C[nx][ny] == "#":
                num += 1
        
        if num < 4:
            continue

        size = 1
        while True:
            num = 0
            for dx,dy in dirs:
                nx = x+dx*size
                ny = y+dy*size
                if 0 <= nx < h and 0 <= ny < w and C[nx][ny] == "#":
                    num += 1


            if num < 4:
                break

            size += 1
        
        ans[size-2] += 1
print(*ans)