n,m = map(int,input().split())
P = [int(x)-1 for x in input().split()]

mod = 998244353
ans = pow(m,n,mod)
used = [0]*n

same = 1
for i in range(n):
    if used[i]:
        continue
    same *= m
    same %= mod
    now = i
    while used[now] == 0:
        used[now] = 1
        now = P[now]
ans -= same
ans %= mod
ans *= pow(2,mod-2,mod)
print(ans%mod)