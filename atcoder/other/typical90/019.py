n = int(input())
A = list(map(int,input().split()))
inf = 10**20

dp = [[inf]*(2*n+1) for i in range(2*n+1)]
for i in range(2*n-1):
    dp[i][i+1] = abs(A[i]-A[i+1])

for i in range(1,2*n+1,2):
    for j in range(2*n-i):
        for k in range(j+1,j+i,2):
            print(i,j,k)
            dp[j][j+i] = min(dp[j][j+i],dp[j][k]+dp[k+1][j+i]+abs(A[k]-A[k+1]))
        #print(i,j,k,dp[j][j+i])

print(dp[0][-1])
for i in dp:
    print(*i)