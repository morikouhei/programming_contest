n = int(input())
L = [list(map(int,input().split())) for i in range(n)]
M = 5005
dp = [0]*M
L.sort()
for d,c,s in L:
    for i in range(M)[::-1]:
        if i+c > d:
            continue
        dp[i+c] = max(dp[i+c],dp[i]+s)

print(max(dp))