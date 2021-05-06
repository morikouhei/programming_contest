n = int(input())
A = [list(map(int,input().split())) for i in range(n)]
friend = [[1]*n for i in range(n)]
m = int(input())
for i in range(m):
    x,y = map(int,input().split())
    x -= 1
    y -= 1
    friend[x][y] = friend[y][x] = 0

inf = 10**10
dp = [[inf]*n for i in range(1<<n)]
for i in range(n):
    dp[1<<i][i] = A[i][0]

for i in range(1<<n):
    for j in range(n):
        if dp[i][j] == inf:
            continue
        num = bin(i).count("1")
        for k in range(n):
            if i >> k & 1 or friend[j][k] == 0:
                continue
            dp[i|1<<k][k] = min(dp[i|1<<k][k],A[k][num]+dp[i][j])

ans = min(dp[-1])
if ans == inf:
    ans = -1
print(ans)
