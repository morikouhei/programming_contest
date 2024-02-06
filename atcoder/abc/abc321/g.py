n,m = map(int,input().split())
R = [0]*n
for r in [int(x)-1 for x in input().split()]:
    R[r] += 1

B = [0]*n
for b in [int(x)-1 for x in input().split()]:
    B[b] += 1

mod = 998244353

facts = [1]*(m+1)
for i in range(2,m+1):
    facts[i] = facts[i-1]*i%mod

pat = [0]*(1<<n)
for i in range(1<<n):
    r,b = 0,0
    for j in range(n):
        if i >> j & 1:
            r += R[j]
            b += B[j]
    
    if r == b:
        pat[i] = facts[r]

dp = [0]*(1<<n)

ans = 0
for i in range(1,1<<n):
    if pat[i] == 0:
        continue
    dp[i] += pat[i]

    ni = i & (i-1)

    while ni > i^ni:
        dp[i] -= dp[ni] * pat[i^ni]
        dp[i] %= mod

        ni = (ni-1) & i

    num = 0
    for j in range(n):
        if i >> j & 1:
            num += R[j]
    ans += dp[i] * facts[m-num]
    ans %= mod
ans *= pow(facts[m],mod-2,mod)
ans %= mod

print(ans)