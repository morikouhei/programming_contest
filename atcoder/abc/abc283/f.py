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


n = int(input())
P = list(map(int,input().split()))

inf = 1<<31

ans = [inf]*n

sP = [[p,i] for i,p in enumerate(P)]

sP.sort()

rseg = SegTree(n,min,inf)
lseg = SegTree(n,min,inf)

for p,ind in sP[::-1]:

    rmin = rseg.get(ind,n)
    if rmin != inf:
        cost = p+ind
        ans[ind] = min(ans[ind],rmin-cost)

    lmin = lseg.get(0,ind)
    if lmin != inf:
        cost = p-ind
        ans[ind] = min(ans[ind],lmin-cost)

    rseg.set(ind,p+ind)
    lseg.set(ind,p-ind)

rseg = SegTree(n,min,inf)
lseg = SegTree(n,min,inf)

for p,ind in sP:

    rmin = rseg.get(ind,n)
    if rmin != inf:
        cost = -p+ind
        ans[ind] = min(ans[ind],rmin-cost)

    lmin = lseg.get(0,ind)
    if lmin != inf:
        cost = -p-ind
        ans[ind] = min(ans[ind],lmin-cost)

    rseg.set(ind,-p+ind)
    lseg.set(ind,-p-ind)

print(*ans)