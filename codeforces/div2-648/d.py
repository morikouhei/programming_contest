from collections import deque

t = int(input())
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for _ in range(t):
    n,m = map(int,input().split())
    l = [list(input()) for i in range(n)]
    count = 0
    for i in l:
        count += i.count("G")
    if count == 0:
        print("Yes")
        continue

    used = [[0]*m for i in range(n)]
    check = True
    for i in range(n):
        for j in range(m):
            if l[i][j] == "B":
                q = deque([])
                q.append((i,j))
                used[i][j] = 1
                while q:
                    x,y = q.popleft()
                    for k in range(4):
                        nx = x+dx[k]
                        ny = y+dy[k]
                        if 0 <= nx < n and 0 <= ny < m:
                            if l[nx][ny] == ".":
                                l[nx][ny] = "#"
                                continue
                            if l[nx][ny] == "G":
                                check = False
                                break
                            if l[nx][ny] == "B" and not used[nx][ny]:
                                used[nx][ny] = 1
                                q.append((nx,ny))
    if check == False or l[-1][-1] == "#":
        print("No")
        continue
    used = [[0]*m for i in range(n)]
    q = deque([])
    q.append((n-1,m-1))
    used[-1][-1] = 1
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if l[nx][ny] == "." or l[nx][ny] == "G":
                    if used[nx][ny]:
                        continue
                    used[nx][ny] = 1
                    q.append((nx,ny))
    for i in range(n):
        for j in range(m):
            if l[i][j] == "G" and not used[i][j]:
                check = False
                break
    if check:
        print("Yes")
    else:
        print("No")