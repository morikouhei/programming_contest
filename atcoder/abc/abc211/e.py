from collections import deque
ans = set()
n = int(input())
k = int(input())
S = [input() for i in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(n):
    for j in range(n):
        if S[i][j] == ".":
            ans.add(1<<(i*n+j))

for i in range(1,k):
    nans = set()
    for s in ans:
        for j in range(n**2):
            if s >> j & 1:
                x,y = divmod(j,n)
                for t in range(4):
                    nx = x+dx[t]
                    ny = y+dy[t]
                    if 0 <= nx < n and 0 <= ny < n and S[nx][ny] == "." and (not s >> (nx*n+ny) & 1):
                        nans.add(s|1<<(nx*n+ny))
    ans = nans

print(len(ans))    
