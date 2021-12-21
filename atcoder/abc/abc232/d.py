h,w = map(int,input().split())
C = [input() for i in range(h)]
dp = [[-1]*w for i in range(h)]
dp[0][0] = 1
ans = 0
for i in range(h):
    for j in range(w):
        if dp[i][j] < 0:
            continue
        ans = max(ans,dp[i][j])
        if i != h-1:
            if C[i+1][j] == ".":
                dp[i+1][j] = dp[i][j]+1
        
        if j != w-1:
            if C[i][j+1] == ".":
                dp[i][j+1] = dp[i][j]+1

print(ans)