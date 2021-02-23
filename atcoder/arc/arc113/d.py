n,m,k = map(int,input().split())
if n < m:
    n,m = m,n
mod = 998244353

ans = 0
if m == 1:
    ans += pow(k,n,mod)
else:
    for i in range(1,k+1):
        base = pow(i,n,mod) - pow(i-1,n,mod)
        base *= pow(k-i+1,m,mod)
        ans += base
        ans %= mod
print(ans)