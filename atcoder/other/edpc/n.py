n = int(input())
A = list(map(int,input().split()))

cum = [0]
for a in A:
    cum.append(cum[-1]+a)
inf = 10**15
dp = [[0]*(n+1) for i in range(n+1)]

for i in range(2,n+1):
    for l in range(n):
        r = l+i
        if r > n:
            continue
        dp[l][r] = inf
        for m in range(l+1,r):
            dp[l][r] = min(dp[l][r],dp[l][m]+dp[m][r]+cum[r]-cum[l])
print(dp[0][n])


