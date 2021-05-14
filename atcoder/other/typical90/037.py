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

    def point_get(self,i):
        i += self.size
        return self.tree[i]

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

def func(x,y):
    return max(x,y)

w,n = map(int,input().split())
lis = [tuple(map(int,input().split())) for i in range(n)]
seg = SegTree(w+5,func,-1)
seg.set(0,0)
for l,r,v in lis:
    for i in range(w+1)[::-1]:

        if i-l < 0:
            continue
        now = seg.point_get(i)
        x = seg.get(max(0,i-r),i-l+1)
        if x == -1:
            continue
        if now < x+v:
            seg.set(i,x+v)
print(seg.point_get(w))