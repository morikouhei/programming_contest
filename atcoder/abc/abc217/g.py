n,m = map(int,input().split())
mod = 998244353
fact = [1,1]
finv = [1,1]
inv = [0,1]
 
for i in range(2,n+5):
    fact.append((fact[-1]*i)%mod)
    inv.append((inv[mod%i]*(mod-mod//i))%mod)
    finv.append((finv[-1]*inv[-1])%mod)
 
def nPr(n,r,mod):
    if r > n:
        return 0
    else: 
        return fact[n]*finv[n-r]%mod
group = [0]*m
for i in range(n):
    group[i%m] += 1
ans = [0]*(n+1)


for i in range(1,n+1):
    count = 1
    for g in group:
        count *= nPr(i,g,mod)
        count %= mod
    for j in range(1,i):
        count -= nPr(i,i-j,mod)*ans[i-j]
        count %= mod
    ans[i] = count*finv[i]%mod
for i in range(1,n+1):
    print(ans[i])