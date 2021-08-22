n = int(input())
S = input()
mod = 998244353
dp = [[0]*(11) for i in range(1<<10)]
dp[0][10] = 1
for s in S:
    id = ord(s)-ord("A")
    for j in range(1<<10)[::-1]:
        for k in range(11):
            if dp[j][k] == 0:
                continue
            if (j >> id & 1) and k != id:
                continue

            dp[j|1<<id][id] += dp[j][k]
            dp[j|1<<id][id] %= mod
ans = -1
for d in dp:
    ans += sum(d)
    ans %= mod
print(ans)

