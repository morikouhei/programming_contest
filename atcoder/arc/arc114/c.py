n,m = map(int,input().split())
mod = 998244353

ans = n*pow(m,n,mod)%mod

pow2 = []
for i in range(m+1):
    l = [1]
    for j in range(n+1):
        l.append(l[-1]*i%mod)
    pow2.append(l)
for j in range(1,m+1):
    for k in range(n-1):
        ans -= (n-1-k)*pow2[m-j][k]%mod*pow2[m][n-k-2]
        ans %= mod

print(ans)

