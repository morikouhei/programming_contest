n = int(input())
A = [list(map(int,input().split())) for i in range(n)]
need = 0
ok = 0
for i in range(n):
    c = 0
    for j in range(n):
        if A[i][j] == 0:
            c += 1
        if A[i][j] == 1:
            need += 1
        
    if c == n:
        print(0)
        exit()
need //= 2
if need > n-1:
    print(0)
    exit()

mod = 10**9+7

fact = [1,1]
finv = [1,1]
inv = [0,1]
 
for i in range(2,n*1000+5):
    fact.append((fact[-1]*i)%mod)
    inv.append((inv[mod%i]*(mod-mod//i))%mod)
    finv.append((finv[-1]*inv[-1])%mod)
 
def nCr(n,r,mod):
    if r > n:
        return 0
    else: 
        return fact[n]*finv[r]*finv[n-r]%mod

cand = [0]*n
for i in range(n):
    can = 0
    for j in range(i+1,n):
        if A[i][j] == -1:
            can += 1
    cand[i] = can
print(sum(cand))
base = nCr(sum(cand), n-1-need, mod)
mi = -1
for i in range(1,n+1):
    c = nCr(n, i, mod)
    print(sum(cand)-i*(n-1)+i*(i-1)//2)
    base += mi*c*(nCr(sum(cand)-i*(n-1)+i*(i-1)//2, n-1-need, mod))
    base %= mod
    mi *= -1
print(base)


