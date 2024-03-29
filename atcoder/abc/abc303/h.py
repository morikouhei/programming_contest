mod = 998244353
g = 3
ginv = 332748118
W = [pow(g, (mod-1)>>i, mod) for i in range(24)]
Winv = [pow(ginv, (mod-1)>>i, mod) for i in range(24)]

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

n,k = map(int,input().split())
S = list(map(int,input().split()))

facts = [1]*(n+1)
for i in range(2,n+1):
    facts[i] = facts[i-1]*i%mod

f = [0]*n
for s in S:
    f[s-1] = pow(facts[s-1],mod-2,mod)

base = [1]
size = n
while n:
    if n & 1:
        base = convolution(base,f)
        base = base[:size]
    
    f = convolution(f,f)
    f = f[:size]
    n >>= 1
print(base[size-2]*facts[size-2]%mod)
