n,m = map(int,input().split())
X = list(map(int,input().split()))
CY = [list(map(int,input().split())) for i in range(m)]
bonus = [0]*(n+1)
for c,y in CY:
    bonus[c] = y

inf = 10**15
dp = [-inf]*(n+1)
dp[0] = 0
for x in X:
    ndp = [-inf]*(n+1)
    for i in range(n+1):
        if dp[i] == -inf:
            continue
        ndp[i+1] = max(ndp[i+1],dp[i]+x+bonus[i+1])
        ndp[0] = max(ndp[0],dp[i])
    dp = ndp
print(max(dp))