
INF = 10**18
class LazySegTree:

    def __init__(self, n, op, e, mapping, composition, id):
        self.n = n
        self.op = op
        self.e = e
        self.mapping = mapping
        self.composition = composition
        self.id = id
        self.log = (n-1).bit_length()
        self.size = 1 << self.log
        self.data = [e]*(2*self.size)
        self.lazy = [id]*(self.size)

    def update(self, k):
        self.data[k] = self.op(self.data[2*k],self.data[2*k+1])

    def all_apply(self, k, f):
        self.data[k] = self.mapping(f, self.data[k])
        if k < self.size:
            self.lazy[k] = self.composition(f, self.lazy[k])

    def push(self, k):
        self.all_apply(2*k, self.lazy[k])
        self.all_apply(2*k+1, self.lazy[k])
        self.lazy[k] = self.id

    def build(self, lis):
        for i, l in enumerate(lis,self.size):
            self.data[i] = l
        for i in range(self.size-1, 0, -1):
            self.update(i)

    def set(self, p, x):
        p += self.size
        for i in range(self.log, 0, -1):
            self.push(p >> i)
        self.data[p] = x
        for i in range(1,self.log+1):
            self.update(p>>i)

    def get(self, p):
        p += self.size
        for i in range(1, self.log+1):
            self.push(p >> i)
        return self.data[p]

    def prod(self, l, r):
        if l == r:
            return self.e
        l += self.size
        r += self.size
        for i in range(self.log, 0, -1):
            if ((l>>i) <<i) != l:
                self.push(l>>i)
            if ((r>>i) <<i) != r:
                self.push(r>>i)
        sml = smr = self.e
        while l < r:
            if l & 1:
                sml = self.op(sml, self.data[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self.op(self.data[r], smr)
            l >>= 1
            r >>= 1
        return self.op(sml, smr)

    def all_prod(self):
        return self.data[1]

    def apply(self, p, f):
        p += self.size
        for i in range(self.log, 0, -1):
            self.push(p >> i)
        self.data[p] = self.mapping(f, self.data[p])
        for i in range(1, self.log+1):
            self.update(p >> i)

    def range_apply(self, l, r, f):
        if l == r:
            return 
        l += self.size
        r += self.size
        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l:
                self.push(l >> i)
            if ((r >> i) << i) != r:
                self.push((r-1) >> i)
        l2 = l
        r2 = r
        while l2 < r2:
            if l2 & 1:
                self.all_apply(l2, f)
                l2 += 1
            if r2 & 1:
                r2 -= 1
                self.all_apply(r2, f)
            l2 >>= 1
            r2 >>= 1
        for i in range(1, self.log+1):
            if ((l >> i) << i) != l:
                self.update(l >> i)
            if ((r >> i) << i) != r:
                self.update((r-1) >> i)

    def max_right(self, l, g):
        if l == self.n:
            return self.n
        l += self.size
        for i in range(self.log, 0, -1):
            self.push(l >> i)
        sm = self.e
        while True:
            while l % 2 == 0:
                l >>= 1
            if not g(self.op(sm, self.data[l])):
                while l < self.size:
                    self.push(l)
                    l <<= 1
                    if g(self.op(sm, self.data[l])):
                        sm = self.op(sm, self.data[l])
                        l += 1
                return l - self.size
            sm = self.op(sm, self.data[l])
            l += 1
            if (l & -l) == l:
                return self.n

    def min_left(self, r, g):
        if r == 0:
            return 0
        r += self.size
        for i in range(self.log, 0, -1):
            self.push((r-1) >> i)
        sm = self.e
        while True:
            r -= 1
            while r > 1 and r % 2:
                r >>= 1
            if not g(self.op(self.data[r], sm)):
                while r < self.size:
                    self.push(r)
                    r = 2*r + 1
                    if g(self.op(self.data[r], sm)):
                        sm = self.op(self.data[r], sm)
                        r -= 1
                return r + 1 - self.size
            sm = self.op(self.data[r], sm)
            if (r & -r) == r:
                return 0

mod = 998244353
po32 = pow(2,32)
n,q = map(int,input().split())

def op(x, y):
    xv,xr = divmod(x,po32)
    yv,yr = divmod(y,po32)
    return ((xv+yv)%mod)*po32 + (xr+yr)%mod

def mapping(p, x):
    xv,xr = divmod(x, po32)
    if p == INF:
        return x
    return (p*xr % mod)*po32+xr

def composition(p, q):
    if p == INF:
        return q
    return p

lis = [0]*n
ten = 1
for i in range(n-1,-1,-1):
    lis[i] = ten%mod
    ten = (ten*10) % mod

l = [i*po32+i for i in lis]
e = 0
id = INF
lazyseg = LazySegTree(n, op, e, mapping, composition, id)
lazyseg.build(l)

for i in range(q):
    l,r,d = map(int,input().split())
    lazyseg.range_apply(l-1,r,d)
    print(lazyseg.all_prod()//po32)