t = int(input())
for _ in range(t):
    n = int(input())
    S = [list(input()) for i in range(n)]
    ind = []
    for i in range(n):
        for j in range(n):
            if S[i][j] == "*":
                ind.append((i,j))

    x,y = ind[0]
    nx,ny = ind[1]
    if x == nx:

        x = (x+1)%n
        nx = (nx+1)%n
    elif y == ny:
        y = (y+1)%n
        ny = (ny+1)%n
    S[x][ny] = S[nx][y] = "*"
    for i in S:
        print(*i,sep="")