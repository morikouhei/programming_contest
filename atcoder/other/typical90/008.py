n = int(input())
S = input()
mod = 10**9+7

dp = [0]*8
dp[0] = 1
l = "atcoder"
for s in S:
    if s not in l:
        continue
    for i in range(7)[::-1]:
        if s == l[i]:
            dp[i+1] += dp[i]
            dp[i+1] %= mod
print(dp[-1])