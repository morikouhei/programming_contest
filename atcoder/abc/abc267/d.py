n,m = map(int,input().split())
A = list(map(int,input().split()))
inf = 10**20
dp = [-inf]*(m+1)
dp[0] = 0

for a in A:
    for i in range(m)[::-1]:
        if dp[i] == -inf:
            continue
        dp[i+1] = max(dp[i+1],dp[i]+a*(i+1))
print(dp[m])