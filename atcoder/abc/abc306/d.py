n = int(input())
XY = [list(map(int,input().split())) for i in range(n)]
inf = 10**20

dp = [0,0]

for x,y in XY:
    ndp = dp[:]

    if x == 0:
        ndp[0] = max(ndp[0],max(dp)+y)

    else:
        ndp[1] = max(ndp[1],dp[0]+y)
    dp = ndp
print(max(dp))