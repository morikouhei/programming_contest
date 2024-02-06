class SegTree:
    """ define what you want to do with 0 index, ex) size = tree_size, func = min or max, sta = default_value """
    
    def __init__(self,size,func,sta):
        self.n = size
        self.size = 1 << size.bit_length()
        self.func = func
        self.sta = sta
        self.tree = [sta]*(2*self.size)

    def build(self, list):
        """ set list and update tree"""
        for i,x in enumerate(list,self.size):
            self.tree[i] = x

        for i in range(self.size-1,0,-1):
            self.tree[i] = self.func(self.tree[i<<1],self.tree[i<<1 | 1])

    def set(self,i,x):
        i += self.size
        self.tree[i] = x
        while i > 1:
            i >>= 1
            self.tree[i] = self.func(self.tree[i<<1],self.tree[i<<1 | 1])

    
    def get(self,l,r):
        """ take the value of [l r) with func (min or max)"""
        l += self.size
        r += self.size
        res = self.sta

        while l < r:
            if l & 1:
                res = self.func(self.tree[l],res)
                l += 1
            if r & 1:
                res = self.func(self.tree[r-1],res)
            l >>= 1
            r >>= 1
        return res


n,k = map(int,input().split())
P = list(map(int,input().split()))


difs = [1 if np > p else 0 for p,np in zip(P,P[1:])]

accum = [0]
for d in difs:
    accum.append(d+accum[-1])

for i in range(n-k+1):
    if accum[i+k-1] - accum[i] == k-1:
        print(*P)
        exit()


seg = SegTree(n,min,n+1)
seg.build(P)

last = -1
for i in range(max(0,n-2*k+2),n-k+1)[::-1]:
    p = P[i]
    if seg.get(i,i+k) != p:
        continue

    if last == i+1:
        last = i
    elif last == -1:
        last = i


ans = P[:]
ans[n-k:n] = sorted(ans[n-k:n])

if last != -1:
    P[last:last+k] = sorted(P[last:last+k])
    if ans < P:
        ans = P
print(*ans)