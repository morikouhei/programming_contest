n = int(input())
l = [tuple(map(int,input().split())) for i in range(n)]
dp = [0]*3
for a,b,c in l:
    ndp = [0]*3
    ndp[0] = max(dp[1],dp[2])+a
    ndp[1] = max(dp[2],dp[0])+b
    ndp[2] = max(dp[0],dp[1])+c
    dp = ndp
print(max(dp))