n,x = map(int,input().split())
AB = [list(map(int,input().split())) for i in range(n)]

dp = [-1]*(x+1)
dp[0] = 0
for a,b in AB:
    ndp = [-1]*(x+1)
    for i in range(x+1):
        if dp[i] >= 0:
            ndp[i] = b
        if i >= a:
            ndp[i] = max(ndp[i],ndp[i-a]-1)
    dp = ndp
    # print(dp,a,b)
print("Yes" if dp[-1] >= 0 else "No")