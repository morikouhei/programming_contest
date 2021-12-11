h,w,k = map(int,input().split())
A = [list(map(int,input().split())) for i in range(h)]
inf = 10**15

def search(x):
    dp = [[[inf]*(h+w+1) for i in range(w)] for j in range(h)]
    if A[0][0] >= x:
        dp[0][0][1] = A[0][0]
    else:
        dp[0][0][0] = 0

    for i in range(h):
        for j in range(w):
            for t in range(h+w):
                a = A[i][j]

                if i != 0:
                    if a < x:
                        dp[i][j][t] = min(dp[i][j][t],dp[i-1][j][t])
                    else:
                        dp[i][j][t] = min(dp[i][j][t],dp[i-1][j][t-1]+a)

                if j != 0:
                    if a < x:
                        dp[i][j][t] = min(dp[i][j][t],dp[i][j-1][t])
                    else:
                        dp[i][j][t] = min(dp[i][j][t],dp[i][j-1][t-1]+a)

    return dp

ans = inf

for i in range(h):
    for j in range(w):
        a = A[i][j]
        dp = search(a)
        for t in range(k,h+w):
            if dp[-1][-1][t] == inf:
                continue
            ans = min(ans,dp[-1][-1][t]-(t-k)*a)
print(ans)

