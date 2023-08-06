n = int(input())
S = list(map(int,input()))
ans = 0

dp = [0,0]
for s in S:
    if s == 0:
        ans += sum(dp)
        dp = [1,sum(dp)]
    else:
        ans += dp[0]+1
        dp = [dp[1],dp[0]+1]
print(ans)
