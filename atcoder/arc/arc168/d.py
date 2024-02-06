import sys
input = sys.stdin.readline

n,m = map(int,input().split())

cross = [[0]*(n+1) for i in range(n+1)]
dp = [[0]*(n+1) for i in range(n+1)]

for i in range(m):
    l,r = map(int,input().split())
    l -= 1
    cross[l][r] = 1

for i in range(n):
    for j in range(n+1):
        cross[i+1][j] += cross[i][j]

for i in range(n+1):
    for j in range(n):
        cross[i][j+1] += cross[i][j]


def check(l1,l2,r1,r2):

    count = cross[l2][r2]
    if l1:
        count -= cross[l1-1][r2]
    if r1:
        count -= cross[l2][r1-1]
    
    if l1 and r1:
        count += cross[l1-1][r1-1]
    
    return count > 0

for le in range(1,n+1):

    for l in range(n):

        r = l+le
        if r > n:
            break

        ma = 0
        for i in range(l,r):
            ma = max(ma,dp[l][i]+dp[i+1][r]+check(l,i,i+1,r))
        
        dp[l][r] = ma

print(dp[0][n])