n,W = map(int,input().split())
l = [tuple(map(int,input().split())) for i in range(n)]
dp = [0]*(W+1)

for w,v in l:
    ndp = [0]*(W+1)
    for i in range(W+1):
        ndp[i] = max(dp[i],ndp[i])
        if i + w <= W:
            ndp[i+w] = max(ndp[i+w],dp[i]+v)
    dp = ndp
print(dp[-1])