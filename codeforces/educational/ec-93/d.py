R,G,B = map(int,input().split())
r = sorted(list(map(int,input().split())), reverse=True)
g = sorted(list(map(int,input().split())), reverse=True)
b = sorted(list(map(int,input().split())), reverse=True)

dp = [[[0]*(B+1) for i in range(G+1)] for j in range(R+1)]
ans = 0
for i in range(R+1):
    for j in range(G+1):
        for k in range(B+1):
            if j*k > 0:
                dp[i][j][k] = max(dp[i][j-1][k-1]+g[j-1]*b[k-1],dp[i][j][k])
            if i*k > 0:
                dp[i][j][k] = max(dp[i-1][j][k-1]+r[i-1]*b[k-1],dp[i][j][k])
            if i*j > 0:
                dp[i][j][k] = max(dp[i-1][j-1][k]+g[j-1]*r[i-1],dp[i][j][k])
            ans = max(ans,dp[i][j][k])
print(ans)