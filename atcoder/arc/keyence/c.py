h,w,k = map(int,input().split())
mod = 998244353

g = [["a"]*w for i in range(h)]
p = pow(3,h*w-k,mod)
div = 2*pow(3,mod-2,mod)
for i in range(k):
    x,y,c = input().split()
    g[int(x)-1][int(y)-1] = c

dp = [[0]*(w+1) for i in range(h+1)]
dp[0][0] = p
for i in range(h):
    for j in range(w):
        s = g[i][j]
        num = dp[i][j]
        if s == "a":
            dp[i][j+1] += num*div
            dp[i][j+1] %= mod
            dp[i+1][j] += num*div
            dp[i+1][j] %= mod
        elif s == "R":
            dp[i][j+1] += num
            dp[i][j+1] %= mod
        elif s == "D":
            dp[i+1][j] += num
            dp[i+1][j] %= mod
        else:
            dp[i][j+1] += num
            dp[i][j+1] %= mod
            dp[i+1][j] += num
            dp[i+1][j] %= mod
print(dp[-2][-2])
