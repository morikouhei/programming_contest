from math import gcd

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



n,q = map(int,input().split())
A = list(map(int,input().split()))
dA = [0]+[abs(a-na) for a,na in zip(A,A[1:])]
B = list(map(int,input().split()))
dB = [0]+[abs(b-nb) for b,nb in zip(B,B[1:])]
segA = SegTree(n,gcd,0)
segA.build(dA)
segB = SegTree(n,gcd,0)
segB.build(dB)
for _ in range(q):
    h1,h2,w1,w2 = map(int,input().split())
    gA = segA.get(h1,h2)
    gB = segB.get(w1,w2)
    h1,w1 = h1-1,w1-1
    
    ans = gcd(A[h1]+B[w1],gA)
    ans = gcd(ans,gB)
    print(ans)