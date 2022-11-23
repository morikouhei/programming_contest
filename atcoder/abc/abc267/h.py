n,m = map(int,input().split())
A = list(map(int,input().split()))

mod = 998244353
g = 3
ginv = 332748118
W = [pow(g, (mod-1)>>i, mod) for i in range(24)]
Winv = [pow(ginv, (mod-1)>>i, mod) for i in range(24)]

N = n+5
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

def fft(k,f):
    for l in range(k,0,-1):
        d = 1 << l - 1
        U = [1]
        for i in range(d):
            U.append(U[-1]*W[l]%mod)
        for i in range(1<<k - l):
            for j in range(d):
                s = i*2*d + j
                f[s],f[s+d] = (f[s]+f[s+d])%mod, U[j]*(f[s]-f[s+d])%mod

def fftinv(k,f):
    for l in range(1,k+1):
        d = 1 << l - 1
        for i in range(1<<k - l):
            u = 1
            for j in range(i*2*d, (i*2+1)*d):
                f[j+d] *= u
                f[j],f[j+d] = (f[j]+f[j+d])%mod, (f[j]-f[j+d])%mod
                u *= Winv[l] 
                u %= mod

def convolution(a,b):
    le = len(a)+len(b)-1
    k = le.bit_length()
    n = 1 << k
    a = a + [0]*(n-len(a))
    b = b + [0]*(n-len(b))
    fft(k,a)
    fft(k,b)
    for i in range(n):
        a[i] *= b[i]
        a[i] %= mod
    fftinv(k,a)
    
    ninv = pow(n,mod-2,mod)
    for i in range(le):
        a[i] *= ninv
        a[i] %= mod
    
    return a[:le]


nums = [0]*(11)
for a in A:
    nums[a] += 1

plus = [1]
minus = [1]

for i,num in enumerate(nums):
    if num == 0:
        continue
    s = min(m,num*i)+1
    nplus = [0]*s
    nminus = [0]*s
    sign = 1
    for j in range(num+1):
        if j*i > m:
            break

        nplus[j*i] = nCr(num,j)
        nminus[j*i] = nCr(num,j)*sign
        sign *= -1
    plus = convolution(plus,nplus)
    minus = convolution(minus,nminus)

ans = 0
if len(plus) > m:
    ans += plus[m]
if len(minus) > m:
    ans -= minus[m]

ans *= pow(2,mod-2,mod)
print(ans%mod)