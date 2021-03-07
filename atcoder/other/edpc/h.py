H,W = map(int,input().split())
A = [input() for i in range(H)]

mod = 10**9+7
dp = [[0]*W for i in range(H)]
dp[0][0] = 1
for i in range(H):
    for j in range(W):
        if A[i][j] == "#":
            continue
        if i < H-1 and A[i+1][j] == ".":
            dp[i+1][j] += dp[i][j]
            dp[i+1][j] %= mod
        if j < W-1 and A[i][j+1] == ".":
            dp[i][j+1] += dp[i][j]
            dp[i][j+1] %= mod
print(dp[-1][-1])