n,d = map(int,input().split())
mod = 998244353

ans = 0
p2 = [1]
for i in range(2*10**6+1):
    p2.append(p2[-1]*2%mod)

for i in range(n):
    if 2*(n-1-i) < d:
        continue
    l = min(n-1-i,d)
    r = max(d-l,0)
    if r == 0:
        ans += p2[i]*p2[d-1]*(l-r-1)%mod+p2[i]*p2[d]*2%mod
        ans %= mod
    else:
        ans += p2[i]*p2[d-1]*(l-r+1)%mod
        ans %= mod
print(ans)