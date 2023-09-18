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



class RelaxedMultiplication:

    def __init__(self):
        self.f = []
        self.h = []
        self.n = 0

    def calc(self,l1,r1,l2,r2):

        self.h += [0] * (r1 + r2 - 1 - len(self.h))

        for i,a in enumerate(convolution(self.f[l1:r1],self.f[l2:r2]),l1+l2):
            self.h[i] = (self.h[i]+a) % mod

    
    def append(self,a):
        self.f.append(a)

        self.n += 1

        n = self.n

        m = (n+1) & -(n+1)

        s = 0
        if m <= n:
            a = 1
            while a <= m:
                self.calc(n-a,n,s,s+a)
                self.calc(s,s+a,n-a,n)
                s += a
                a <<= 1

        else:
            a = 1
            while a < m >> 1:
                self.calc(n-a,n,s,s+a)
                self.calc(s,s+a,n-a,n)
                s += a
                a <<= 1
            self.calc(n-a,n,s,s+a)

        return self.h[n-1]
n = int(input())
A = list(map(int,input().split()))

rm = RelaxedMultiplication()

ans = []

num = rm.append(1)

for a in A:

    f = num*a%mod
    ans.append(f)

    f = rm.append(f)

    num = (num+f) % mod
print(*ans)