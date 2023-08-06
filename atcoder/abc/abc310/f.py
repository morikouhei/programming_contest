n = int(input())
A = list(map(int,input().split()))
mod = 998244353

dp = [0]*(1<<11)
dp[1<<10] = 1

for a in A:
    ndp = [0]*(1<<11)
    inva = pow(a,mod-2,mod)
    for b in range(1<<11):
        if dp[b] == 0:
            continue
        for i in range(1,11):
            if i > a:
                continue
            ndp[b|(b >> i)] += dp[b] * inva
            ndp[b|(b >> i)] %= mod
        ndp[b] += dp[b] * inva * max(0,a-10)
        ndp[b] %= mod
    dp = ndp

ans = 0
for i in range(1<<11):
    if i & 1:
        ans += dp[i]
        ans %= mod
print(ans)