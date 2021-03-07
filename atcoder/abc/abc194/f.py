n,k = input().split()
le = len(n)
k = int(k)
mod = 10**9+7

dp = [[0]*18 for i in range(le)]
f = int(n[0],16)
dp[0][1] = f-1
s = set()
s.add(f)
for i in range(1,le):
    num = int(n[i],16)
    for j in range(17):
        if j < num:
            if j in s:
                dp[i][len(s)] += 1
            else:
                dp[i][len(s)+1] += 1
        dp[i][j] += dp[i-1][j]*j
        dp[i][j] %= mod
        dp[i][j+1] += dp[i-1][j]*(16-j)
        dp[i][j+1] %= mod
    dp[i][1] += 15
    s.add(num)
ans = dp[-1][k]
if len(s) == k:
    ans = (ans+1)%mod
print(ans)
print(dp)