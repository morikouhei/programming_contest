n = int(input())
x,y = map(int,input().split())
AB = [list(map(int,input().split())) for i in range(n)]
dp = [[n+1]*(y+1) for i in range(x+1)]
dp[0][0] = 0
for a,b in AB:
    for i in range(x+1)[::-1]:
        for j in range(y+1)[::-1]:
            if dp[i][j] == n+1:
                continue
            nx = i+a
            ny = j+b
            if nx > x:
                nx = x
            if ny > y:
                ny = y
            dp[nx][ny] = min(dp[nx][ny],dp[i][j]+1)
if dp[-1][-1] == n+1:
    dp[-1][-1] = -1
print(dp[-1][-1])