k = int(input())
if k%9:
    print(0)
    exit()

mod = 10**9+7
dp = [0]*(k+1)
dp[0] = 1
cum = 1
for i in range(1,k+1):
    dp[i] = cum
    cum += dp[i]
    if i >= 9:
        cum -= dp[i-9]
    cum %= mod
print(dp[-1])