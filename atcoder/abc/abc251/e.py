n = int(input())
A = list(map(int,input().split()))
inf = 10**20
ans = inf

dp = [inf]*n
dp[1] = A[0]
dp[0] = A[0]
for i in range(n):
    if i+1 < n:
        dp[i+1] = min(dp[i+1],dp[i]+A[i+1])
        dp[i+1] = min(dp[i+1],dp[i]+A[i])
    if i+2 < n:
        dp[i+2] = min(dp[i+2],dp[i]+A[i+1])
ans = dp[-1]

dp = [inf]*(n-1)
dp[0] = A[-1]
for i in range(n-1):
    if i+1 < n-1:
        dp[i+1] = min(dp[i+1],dp[i]+A[i+1])
        dp[i+1] = min(dp[i+1],dp[i]+A[i])
    if i+2 < n-1:
        dp[i+2] = min(dp[i+2],dp[i]+A[i+1])
ans = min(ans,dp[-1])
print(ans)