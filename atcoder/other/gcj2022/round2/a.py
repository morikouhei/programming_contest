from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]
def solve():
    n,k = map(int,input().split())
    if k%2:
        return "IMPOSSIBLE"
    if k < n-1:
        return "IMPOSSIBLE"

    g = [[0]*n for i in range(n)]
    g[0][0] = 1
    x,y = 0,0
    dir = 0
    while g[x][y] != n**2:
        nx = x+dx[dir]
        ny = y+dy[dir]
        if 0 <= nx < n and 0 <= ny < n and g[nx][ny] == 0:
            g[nx][ny] = g[x][y]+1
            x = nx
            y = ny
        else:
            dir = (dir+1)%4
    ans = []
    turn = k-1
    x,y = 0,0
    while g[x][y] != n**2:
        for dir in range(4):
            nx,ny = x+dx[dir],y+dy[dir]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if g[nx][ny] < g[x][y]:
                continue
            need = n**2-g[nx][ny]
            if need >= turn:
                if g[nx][ny] > g[x][y]+1:
                    ans.append(g[x][y])
                    ans.append(g[nx][ny])
                x,y = nx,ny

                turn -= 1
    return ans


t = int(input())
for i in range(t):
    ans = solve()
    print("Case #{}:".format(i+1),end=" ")
    if ans == "IMPOSSIBLE":
        print(ans)
        continue
    print(len(ans)//2)
    for i in range(len(ans)//2):
        print(ans[2*i],ans[2*i+1])