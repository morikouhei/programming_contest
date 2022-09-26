n,m = map(int,input().split())
a,b,c,d,e,f = map(int,input().split())
XY = [tuple(map(int,input().split())) for i in range(m)]
mod = 998244353
move = [[a,b],[c,d],[e,f]]
XY = set(XY)

dp = [[0]*(n+1) for i in range(n+1)]
dp[0][0] = 1

for i in range(n):
    ndp = [[0]*(n+1) for i in range(n+1)]
    for j in range(n):
        for k in range(n):
            if j+k > n:
                break
            if dp[j][k] == 0:
                continue
            l = (i-j-k)
            if l < 0:
                continue
            bx = a*j+c*k+e*l
            by = b*j+d*k+f*l

            if (bx+a,by+b) not in XY:
                ndp[j+1][k] += dp[j][k]
                ndp[j+1][k] %= mod

            if (bx+c,by+d) not in XY:
                ndp[j][k+1] += dp[j][k]
                ndp[j][k+1] %= mod

            if (bx+e,by+f) not in XY:
                ndp[j][k] += dp[j][k]
                ndp[j][k] %= mod
    dp = ndp

ans = 0
for i in dp:
    ans += sum(i)%mod
    ans %= mod
print(ans)