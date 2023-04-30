h,w,k = map(int,input().split())

mod = 998244353


### for bigger prime 
N = h*w+5
fact = [1]*N
finv = [1]*N
 
for i in range(2,N):
    fact[i] = (fact[i-1]*i)%mod
finv[-1] = pow(fact[-1],mod-2,mod)
for i in range(1,N)[::-1]:
    finv[i-1] = (finv[i]*i)%mod

def nCr(n,r):
    if r > n:
        return 0
    else: 
        return fact[n]*finv[r]%mod*finv[n-r]%mod

def nPr(n,r,mod):
    if r > n:
        return 0
    else: 
        return fact[n]*finv[n-r]%mod




ans = 0
for i in range(1,h+1):
    for j in range(1,w+1):


        size = i*j
        add = size * (h-i+1) * (w-j+1)
        if size < k:
            continue

        ### all
        pat = nCr(size,k)

        ### 1
        pat -= nCr((i-1)*j,k)*2
        pat -= nCr(i*(j-1),k)*2
        pat %= mod

        ### 2
        if i >= 2:
            pat += nCr((i-2)*j,k)
        if j >= 2:
            pat += nCr(i*(j-2),k)
        pat %= mod

        if i and j:
            pat += nCr((i-1)*(j-1),k)*4
        pat %= mod


        ### 3
        if i >= 2 and j:
            pat -= nCr((i-2)*(j-1),k)*2
        if i and j >= 2:
            pat -= nCr((i-1)*(j-2),k)*2
        pat %= mod

        if i >= 2 and j >= 2:
            pat += nCr((i-2)*(j-2),k)
        pat %= mod
        ans += pat*add
        ans %= mod


        # print(i,j,size,pat)
        



ans *= pow(nCr(h*w,k),mod-2,mod)
ans %= mod
print(ans)

        