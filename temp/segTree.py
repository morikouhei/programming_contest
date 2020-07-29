class segtree:
    ## define what you want to do ,(min, max)
    sta = float("INF")
    func = min

    def __init__(self,n):
        self.n = n
        self.tree = [self.sta]*(2*n)

    def build(self, list):
        for i,x in enumerate(list,self.n):
            self.tree[i] = x

        for i in range(self.n-1,0,-1):
            self.tree[i] = self.func(self.tree[i<<1],self.tree[i<<1 | 1])

    def set(self,i,x):
        i += self.n
        self.tree[i] = x
        while i > 1:
            i >>= 1
            self.tree[i] = self.func(self.tree[i<<1],self.tree[i<<1 | 1])

    ## take the value of [l,r) 
    def get(self,l,r):
        l += self.n
        r += self.n
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
