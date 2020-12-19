n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

dp = [[2500]*(m+1) for i in range(n+1)]
for i in range(n+1):
    dp[i][0] = i
for i in range(m+1):
    dp[0][i] = i
for i in range(n):
    for j in range(m):
        dp[i+1][j+1] = min(dp[i][j]+(a[i] != b[j]),dp[i+1][j]+1,dp[i][j+1]+1)
      
print(dp[n][m])
