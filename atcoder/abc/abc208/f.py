n,m,k = map(int,input().split())
mod = 10**9+7
s = m+k

def fast_pow(p,k):
    ans = 1
    while k:
        if k&1:
            ans *= p
            if ans > mod:
                ans %= mod
        k //= 2
        p = p*p
        if p > mod:
            p %= mod
    return ans
dp = [fast_pow(i,k) for i in range(s+1)]
for _ in range(m):
    for i in range(s):
        dp[i+1] += dp[i]
        dp[i+1] %= mod

fac = 1
for i in range(1,s+1):
    fac *= i
    fac %= mod

inv = [0]*(s+1)
inv[-1] = fast_pow(fac,mod-2)
for i in range(s)[::-1]:
    inv[i] = inv[i+1]*(i+1)
    inv[i] %= mod

n %= mod
l = [1]*(s+1)
for i in range(s):
    l[i+1] = l[i]*(n-i)%mod
r = [1]*(s+1)
for i in range(1,s+1)[::-1]:
    r[i-1] = r[i]*(n-i)%mod

ans = 0
for i in range(s+1):
    count = dp[i]*l[i]%mod*r[i]%mod*inv[i]%mod*inv[s-i]%mod
    if s%2 == i%2:
        ans += count
    else:
        ans -= count
    ans %= mod
print(ans)