n = int(input())
A = list(map(int,input().split()))

inf = 10**15
dp = [[0]*n for i in range(n)]
for i in range(n):
    if n%2:
        dp[i][i] = A[i]
    else:
        dp[i][i] = -A[i]

for i in range(1,n):
    for j in range(n):
        if j+i >= n:
            continue
        if i%2 == n%2:
            dp[j][j+i] = max(dp[j][j+i-1]+A[j+i],dp[j+1][j+i]+A[j])
        else:
            dp[j][j+i] = min(dp[j][j+i-1]-A[j+i],dp[j+1][j+i]-A[j])
print(dp[0][-1])