n,m = map(int,input().split())
A = list(map(int,input().split()))

inf = 10**5

dp = [[inf]*2 for i in range(m+1)]
dp[0][1] = 0

for a in A:
    ndp = [[inf]*2 for i in range(m+1)]
    for i in range(m+1):
        if dp[i][0] != inf:
            ndp[i][0] = min(ndp[i][0],dp[i][0])
            if i+a <= m:
                ndp[i+a][1] = min(ndp[i+a][1],dp[i][0])

        if dp[i][1] != inf:
            ndp[i][0] = min(ndp[i][0],dp[i][1]+1)
            if i+a <= m:
                ndp[i+a][1] = min(ndp[i+a][1],dp[i][1])
    dp = ndp
    # print(dp)

for i in range(1,m+1):
    ans = min(dp[i])
    if ans == inf:
        ans = -1
    print(ans)