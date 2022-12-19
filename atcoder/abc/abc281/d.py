n,k,d = map(int,input().split())
A = list(map(int,input().split()))

dp = [[-1]*d for i in range(k+1)]
dp[0][0] = 0

for a in A:
    for i in range(k)[::-1]:
        for j in range(d):
            if dp[i][j] == -1:
                continue
            dp[i+1][(j+a)%d] = max(dp[i+1][(j+a)%d],dp[i][j]+a)

ans = dp[k][0]
print(ans)