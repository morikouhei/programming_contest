n,k,mod = map(int,input().split())

M = n*n*k+10
dp = [[0]*M for i in range(n+1)]
dp[0][0] = 1
count = 0
for i in range(1,n+1):
    count += i
    for j in range(count*k):
        dp[i][j] += dp[i-1][j]
        if j < i*(k+1):
            dp[i][j] += dp[i][j-i]
        else:
            dp[i][j] += dp[i][j-i]-dp[i-1][j-i*(k+1)]
        dp[i][j] %= mod

for i in range(1,n+1):
    count = 0
    for j in range(M):
        count += dp[i-1][j]*dp[n-i][j]
        count %= mod
    count = (count*(k+1)-1)%mod
    print(count)