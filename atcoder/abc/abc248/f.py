n,mod = map(int,input().split())


dp = [[0]*2 for i in range(n)]
dp[0][0] = 1
dp[1][1] = 1

for i in range(n-1):
    ndp = [[0]*2 for i in range(n)]
    for j in range(n):
        if j+2 < n:
            ndp[j+2][1] += 2*dp[j][0]
            ndp[j+2][1] %= mod
        
        if j+1 < n:
            ndp[j+1][0] += 3*dp[j][0]
            ndp[j+1][0] %= mod

        ndp[j][0] += dp[j][0]
        ndp[j][0] %= mod

        if j+1 < n:
            ndp[j+1][1] += dp[j][1]
            ndp[j+1][1] %= mod
        
        ndp[j][0] += dp[j][1]
        ndp[j][0] %= mod

    dp = ndp
ans = [dp[i][0] for i in range(1,n)]
print(*ans)
    

        



