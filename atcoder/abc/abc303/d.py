x,y,z = map(int,input().split())
S = input()
inf = 10**20
dp = [0,z]

for s in S:
    ndp = [inf,inf]

    if s == "a":
        ndp[0] = min(ndp[0],dp[0]+x)
        ndp[1] = min(ndp[1],dp[1]+y)

        ndp[1] = min(ndp[1],dp[0]+x+z)
        ndp[0] = min(ndp[0],dp[1]+y+z)

    else:
        ndp[1] = min(ndp[1],dp[1]+x)
        ndp[0] = min(ndp[0],dp[0]+y)

        ndp[0] = min(ndp[0],dp[1]+x+z)
        ndp[1] = min(ndp[1],dp[0]+y+z)

    dp = ndp

print(min(dp))