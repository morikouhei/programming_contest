h,w = map(int,input().split())
mod = 10**9+7
s = [list(input()) for i in range(h)]

dp = [[0]*(w+1) for i in range(h+1)]
dph = [[0]*(w+1) for i in range(h+1)]
dpw = [[0]*(w+1) for i in range(h+1)]
dpc = [[0]*(w+1) for i in range(h+1)]
dp[1][1] = 1

for i in range(1,h+1):
    for j in range(1,w+1):
        
        if s[i-1][j-1] == "#":
            continue
        dp[i][j] += dph[i][j-1]+dpw[i-1][j]+dpc[i-1][j-1]
        dp[i][j] %= mod
        dph[i][j] += dp[i][j]+dph[i][j-1]
        dph[i][j] %= mod
        dpw[i][j] += dp[i][j]+dpw[i-1][j]
        dpw[i][j] %= mod
        dpc[i][j] += dp[i][j]+dpc[i-1][j-1]
        dpc[i][j] %= mod

print(dp[-1][-1])
