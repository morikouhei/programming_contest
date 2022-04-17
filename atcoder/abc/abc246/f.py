n,l = map(int,input().split())
S = []
for _ in range(n):
    b = 0
    for i in input():
        b |= 1<<(ord(i)-ord("a"))
    S.append(b)

mod = 998244353

ans = 0
dp = [(1<<26)-1]*(1<<n)

for i in range(1<<n):
    for j in range(n):
        if i >> j & 1:
            continue
        dp[i|1<<j] = dp[i] & S[j]
    if i == 0:
        continue

    p = pow(bin(dp[i]).count("1"),l,mod)
    if bin(i).count("1")%2 == 0:
        p = -p
    ans = (ans+p)%mod
print(ans)

