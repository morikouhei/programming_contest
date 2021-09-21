a,b,x,y = map(int,input().split())
mod = 10**9+7

### for bigger prime 
fact = [1,1]
finv = [1,1]
inv = [0,1]
 
for i in range(2,3*10**6+5):
    fact.append((fact[-1]*i)%mod)
    inv.append((inv[mod%i]*(mod-mod//i))%mod)
    finv.append((finv[-1]*inv[-1])%mod)
 
def nCr(n,r,mod):
    if r > n:
        return 0
    else: 
        return fact[n]*finv[r]%mod*finv[n-r]%mod

ans = 0
r = (b+4)//4
u = (b+3)//4
l = (b+2)//4
d = (b+1)//4

for i in range(a+1):
    if i < x:
        continue
    base = nCr(i+r-1,r-1,mod)
    nl = i-x
    if nl+i > a:
        continue
    if nl and l == 0:
        continue
    base *= nCr(nl+l-1,l-1,mod)
    base %= mod
    ud = a-i-nl
    if ud < abs(y):
        continue
    if (ud-abs(y))%2:
        continue
    if y >= 0:
        nu = y+(ud-y)//2
        if nu and u == 0:
            continue
        base *= nCr(nu+u-1,u-1,mod)

        nd = (ud-y)//2
        if nd and d == 0:
            continue
        base *= nCr(nd+d-1,d-1,mod)
        
    else:
        nd = -y+(ud+y)//2
        if nd and d == 0:
            continue
        base *= nCr(nd+d-1,d-1,mod)

        nu = (ud+y)//2
        if nu and u == 0:
            continue
        base *= nCr(nu+u-1,u-1,mod)
    ans += base%mod
    ans %= mod
print(ans)