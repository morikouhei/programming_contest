n,x = map(int,input().split())
a = list(map(int,input().split()))

ans = 10**20

for k in range(1,n+1):
    dp = [[-1]*k for i in range(k+1)]
    dp[0][0] = 0

    for i in range(n):
        ndp = [[-1]*k for q in range(k+1)]
        num = a[i]
        for j in range(k+1):
            for t in range(k):
                q = dp[j][t]
                if q == -1:
                    continue
                ndp[j][t] = max(ndp[j][t],dp[j][t])
                if j != k:
                    ndp[j+1][(num+q)%k] = max(ndp[j+1][(num+q)%k],num+q)
            
        dp = ndp
    if dp[-1][x%k] != -1:
        ans = min(ans,(x-dp[-1][x%k])//k)
print(ans)