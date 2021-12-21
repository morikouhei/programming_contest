h,w,k = map(int,input().split())
x1,y1,x2,y2 = map(int,input().split())
mod = 998244353
dp = [0]*4

if x1 == x2 and y1 == y2:
    dp[0] = 1

if x1 == x2 and y1 != y2:
    dp[2] = 1

if x1 != x2 and y1 == y2:
    dp[1] = 1

if x1 != x2 and y1 != y2:
    dp[3] = 1


for i in range(k):
    ndp = [0]*4
    ndp[0] = (dp[1]+dp[2])%mod
    ndp[1] = (dp[0]*(h-1)+dp[1]*(h-2)+dp[3])%mod
    ndp[2] = (dp[0]*(w-1)+dp[2]*(w-2)+dp[3])%mod
    ndp[3] = (dp[1]*(w-1)+dp[2]*(h-1)+dp[3]*(w+h-4))%mod
    dp = ndp
print(dp[0]%mod)