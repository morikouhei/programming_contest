from collections import Counter
t = int(input())
mod = 10**9+7

fact = [1,1]
finv = [1,1]
inv = [0,1]
 
for i in range(2,1005):
    fact.append((fact[-1]*i)%mod)
    inv.append((inv[mod%i]*(mod-mod//i))%mod)
    finv.append((finv[-1]*inv[-1])%mod)
 
def nCr(n,r,mod):
    if r > n:
        return 0
    else: 
        return fact[n]*finv[r]*finv[n-r]%mod

def solve():
    n,k = map(int,input().split())
    A = list(map(int,input().split()))
    C = Counter(A)
    s = sorted(list(set(A)))
    now = 0
    for i in s[::-1]:
        if C[i]+now < k:
            now += C[i]
            continue
        need = k-now
        size = C[i]
        return nCr(size,need,mod)

for _ in range(t):
    ans = solve()
    print(ans)