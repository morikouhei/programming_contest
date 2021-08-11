n,m = map(int,input().split())
mod = 998244353
e = [[int(x)-1 for x in input().split()] for i in range(m)]


edge = [0]*(1<<n)
for i in range(1<<n):
    for x,y in e:
        if (i >> x & 1 ) & (i >> y & 1):
            edge[i] += 1

dp = [0]*(1<<n)

for i in range(1<<n):
    if not i&1:
        continue
    dp[i] = pow(2,edge[i],mod)
    now = (i-1) & i
    while now:
        if now&1:
            dp[i] -= dp[now]*pow(2,edge[i^now],mod)
            dp[i] %= mod
        now = (now-1)&i

ans = [0]*n
for i in range(1<<n):
    if not i&1:
        continue
    for j in range(n):
        if i >> j & 1:
            ans[j] += dp[i]*pow(2,edge[((1<<n)-1)^i],mod)
            ans[j] %= mod

for i in ans[1:]:
    print(i)