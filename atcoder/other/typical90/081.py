n,k = map(int,input().split())
AB = [list(map(int,input().split())) for i in range(n)]
M = 5005
dp = [[0]*(M) for i in range(M)]
for a,b in AB:
    dp[a][b] += 1
for i in range(M):
    for j in range(M-1):
        dp[i][j+1] += dp[i][j] 
for i in range(M):
    for j in range(M-1):
        dp[j+1][i] += dp[j][i] 

ans = 0
for i in range(1,M-k):
    for j in range(1,M-k):
        ans = max(ans,dp[i+k][j+k]+dp[i-1][j-1]-dp[i+k][j-1]-dp[i-1][j+k])
print(ans)