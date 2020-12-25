import sys
input = sys.stdin.readline
class SegTree:
    """ define what you want to do with 0 index, ex) size = tree_size, func = min or max, sta = default_value """
    
    def __init__(self,size,sta):
        self.n = size
        self.size = 1 << size.bit_length()
        self.sta = sta
        self.tree = [sta]*(2*self.size)

    def build(self, list):
        """ set list and update tree"""
        for i,x in enumerate(list,self.size):
            self.tree[i] = x

        for i in range(self.size-1,0,-1):
            self.tree[i] = self.tree[i<<1]+self.tree[i<<1 | 1]

    def set(self,i,x):
        i += self.size
        self.tree[i] = x
        while i > 1:
            i >>= 1
            self.tree[i] = self.tree[i<<1]+self.tree[i<<1 | 1]

    
    def get(self,l,r):
        """ take the value of [l r) with func (min or max)"""
        l += self.size
        r += self.size
        res = self.sta

        while l < r:
            if l & 1:
                res = self.tree[l]+res
                l += 1
            if r & 1:
                res = self.tree[r-1]+res
            l >>= 1
            r >>= 1
        return res
h,w,m = map(int,input().split())
xy = [list(map(int,input().split())) for i in range(m)]

H = [w]*h
W = [h]*w
Hl = [[w] for i in range(h)]
for x,y in xy:
    x -= 1
    y -= 1
    H[x] = min(H[x],y)
    W[y] = min(W[y],x)
    Hl[x].append(y)

ans = 0
for i in range(H[0]):
    ans += W[i]

seg = SegTree(w+1,0)
l = [0]*(H[0])+[1]*(w-H[0])
seg.build(l)
for i in range(1,W[0]):
    mi = min(Hl[i])
    ans += seg.get(0,mi)
    for j in Hl[i]:
        if j != w:

            seg.set(j,1)
print(ans)
