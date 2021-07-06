n = int(input())
L = [ord(s)-ord("a") for s in input()]
inf = 10**10
dp = [[inf]*27 for i in range(n+1)]
dp[0][-1] = 0
for i,s in enumerate(L):
    for j in range(26):
        if dp[i][j] == -1:
            continue
        if j != s:
            dp[i+1][-1] = min(dp[i+1][-1],dp[i][j])
        dp[i+1][j] = min(dp[i][j],dp[i+1][j])
    if dp[i][-1] != inf:
        dp[i+1][s] = min(dp[i+1][s],dp[i][-1]+1)
ans = dp[-1][-1]
if ans == inf:
    ans = -1
print(ans)
