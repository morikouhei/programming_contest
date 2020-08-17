import sys
input = sys.stdin.readline
r,c,k = map(int,input().split())
l = [[0]*c for i in range(r)] 
for i in range(k):
    x,y,v = map(int,input().split())
    l[x-1][y-1] = v
dp = [[0]*4 for i in range(c+1)]

for i in range(r):
    ndp = [[0]*4 for i in range(c+1)]
    for j in range(c):
        M = max(dp[j+1])
        if l[i][j]>0:
            v = l[i][j]
            ndp[j+1][0] = max(M,dp[j][0],ndp[j][0])
            ndp[j+1][1] = max(M+v,dp[j][0]+v,ndp[j][0]+v,dp[j][1],ndp[j][1])
            ndp[j+1][2] = max(dp[j][1]+v,ndp[j][1]+v,dp[j][2],ndp[j][2])
            ndp[j+1][3] = max(dp[j][2]+v,ndp[j][2]+v,dp[j][3],ndp[j][3])
        else:
            ndp[j+1][0] = max(M,dp[j][0],ndp[j][0])
            ndp[j+1][1] = max(dp[j][1],ndp[j][1])
            ndp[j+1][2] = max(dp[j][2],ndp[j][2])
            ndp[j+1][3] = max(dp[j][3],ndp[j][3])
    dp = ndp
print(max(dp[-1]))