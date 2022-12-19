n,mod = map(int,input().split())

nCr = [[0]*n for i in range(n)]
nCr[1][0] = nCr[1][1] = 1
for i in range(2,n):
    for j in range(i+1):
        if j == 0:
            nCr[i][j] = 1
        else:
            nCr[i][j] = (nCr[i-1][j]+nCr[i-1][j-1])%mod


dp = [[0]*n for i in range(n)]
twos = [1]*(n**2)
for i in range(1,n**2):
    twos[i] = twos[i-1]*2%mod

coef = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        coef[i][j] = pow(twos[i]-1,j,mod)

dp[1][1] = 1
for i in range(1,n):
    for j in range(i+1)[::-1]:
        if dp[i][j] == 0:
            continue
        for nj in range(1,n-i):
            count = nCr[n-1-i][nj]
            count *= twos[nj*(nj-1)//2]
            count %= mod
            count *= coef[j][nj]
            count %= mod
            dp[i+nj][nj] += dp[i][j]*count
            dp[i+nj][nj] %= mod

ans = 0
for i in range(1,n):
    if dp[n-1][i] == 0:
        continue
    count = twos[i]-1
    ans += dp[n-1][i]*count
    ans %= mod
print(ans)