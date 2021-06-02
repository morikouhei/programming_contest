import bisect
n,k = map(int,input().split())
A = list(map(int,input().split()))
A.sort()

inf = 10**10
dp = [[inf]*31 for i in range(n+1)]
dp[0][0] = 0
for i,a in enumerate(A[::-1]):
    ind = bisect.bisect_right(A,a//2)
    for j in range(31):
        if dp[i][j] == inf:
            continue
        dp[i+1][j] = min(dp[i][j]+1,dp[i+1][j])
        dp[n-ind][j+1] = min(dp[n-ind][j+1],dp[i][j])
for i in range(31):
    if dp[-1][i] <= k:
        print(i,dp[-1][i])
        exit()