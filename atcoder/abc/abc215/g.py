from collections import Counter
n = int(input())
C = Counter(list(map(int,input().split())))
L = Counter(C.values())
mod = 998244353

### for bigger prime 
fact = [1,1]
finv = [1,1]
inv = [0,1]
 
for i in range(2,n+5):
    fact.append((fact[-1]*i)%mod)
    inv.append((inv[mod%i]*(mod-mod//i))%mod)
    finv.append((finv[-1]*inv[-1])%mod)
 
def nCr(n,r,mod):
    if r > n:
        return 0
    else: 
        return fact[n]*finv[r]%mod*finv[n-r]%mod

for i in range(1,n+1):
    all = nCr(n,i,mod)
    count = 0
    for j,x in L.items():
        count += (all-nCr(n-j,i,mod))*x%mod
        count %= mod
    count *= pow(all,mod-2,mod)
    print(count%mod)
