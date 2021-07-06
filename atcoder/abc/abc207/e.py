n = int(input())
A = list(map(int,input().split()))+[0]
mod = 10**9+7
dp = [[0]*(n+2) for i in range(n+2)]
dp[0][0] = 1
cum = 0
for i in range(n):
    for j in range(n):
        if dp[i][j] == 0:
            continue
        las = cum%(j+1)
        now = las
        for k in range(i,n):
            now += A[k]
            now %= j+1
            if las == now:
                dp[k+1][j+1] += dp[i][j]
                print(i,j,k)
                dp[k+1][j+1] %= mod
                break
ans = sum(dp[n])
print(ans)