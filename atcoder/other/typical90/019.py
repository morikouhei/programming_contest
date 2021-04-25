n = int(input())
A = list(map(int,input().split()))
inf = 10**6

dp = [[inf]*2*n for i in range(2*n)]
for i in range(2*n-1):
    dp[i][i+1] = abs(A[i]-A[i+1])

for i in range(3,2*n+1,2):
    for j in range(2*n):
        if j+i >= 2*n:
            continue
        dp[j][j+i] = abs(A[j]-A[j+i])+dp[j+1][j+i-1]
        for k in range(j+1,j+i,2):
            dp[j][j+i] = min(dp[j][j+i],dp[j][k]+dp[k+1][j+i])
print(dp[0][-1])
