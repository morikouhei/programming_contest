n,m,k = map(int,input().split())
s = [0]*(n+1)
for i in map(int,input().split()):
    s[i] = 1

dp = [0]*(n+1)
dp0 = [0]*(n+1)
now = 0
now0 = 0
r = 0
for i in range(n-1,-1,-1):
    if s[i]:
        r += 1
        dp0[i] = 1
    else:
        if r == m:
            print(-1)
            exit()
        dp[i] = 1 + now/m
        dp0[i] = now0/m
    now += dp[i]
    now0 += dp0[i]
    if i+m <= n:
        now -= dp[i+m]
        now0 -= dp0[i+m]
        r -= s[i+m]

print(dp[0]/(1-dp0[0]))

