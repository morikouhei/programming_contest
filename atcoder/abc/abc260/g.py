n,m = map(int,input().split())
grid = [[0]*(n+5) for i in range(n+5)]
grid2 = [[0]*(n+5) for i in range(n+5)]

for i in range(1,n+1):
    S = input()
    for j in range(1,n+1):
        if S[j-1] == "X":
            continue

        grid[i][j] += 1
        grid[min(i+m,n+1)][j] -= 1

        a = 2*(i+m)+j
        lx = min(i+m,n+1)
        rx = max(i,(a-n)//2)
        if lx <= rx:
            continue

        ry = -2*rx + a
        ly = -2*lx + a
        grid2[rx][ry] -= 1
        grid2[lx][ly] += 1

for i in range(1,n+2):
    for j in range(1,n+2):
        grid[i+1][j] += grid[i][j]

for i in range(1,n+2):
    for j in range(2,n+3):
        grid2[i+1][j-2] += grid2[i][j]

for i in range(n+2):
    for j in range(n+2):
        grid[i][j] += grid2[i][j]

for i in range(n+2):
    for j in range(n+2):
        grid[i][j+1] += grid[i][j]

q = int(input())
for _ in range(q):
    x,y = map(int,input().split())
    print(grid[x][y])

