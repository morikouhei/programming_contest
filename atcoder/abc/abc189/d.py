n = int(input())
S = [input() for i in range(n)]
dp = [[0]*2 for i in range(n+1)]
dp[0] = [1,1]
for i,s in enumerate(S):
    if s == "AND":
        dp[i+1][0] += dp[i][0]
        dp[i+1][1] += dp[i][1]*2+dp[i][0]
    else:
        dp[i+1][0] += dp[i][0]*2+dp[i][1]
        dp[i+1][1] += dp[i][1]
print(dp[-1][0])
