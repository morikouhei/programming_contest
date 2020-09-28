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

    def max_right(self, l, x):
        """[l,r) が ok であるような最大の r を返す"""
        if l == self.n:
            return l
        l += self.size
        res = self.sta
        check = True
        while check or (l & -l) != l:
            check = False
            while l%2 == 0:
                l >>= 1
            if not self.func(res,self.tree[l]) < x:
                while l < self.size:
                    l <<= 1
                    if self.func(res,self.tree[l]) < x:
                        res = self.func(res,self.tree[l])
                        l += 1
                return l - self.size
            res = self.func(res,self.tree[l])
            l += 1
        return self.n

    def min_left(self, r, x):
        """(r が ok であるような最小の r を返す probably wrong"""
        if r == 0:
            return 0
        r += self.size
        res = self.sta
        check = True
        while check and (r & -r) != r:
            check = False
            r -= 1
            while (r > 1 and r%2):
                r >>= 1
            if not self.func(res, self.tree[r]) < x:
                while r < self.size:
                    r = 2*r + 1
                    if self.func(res, self.tree[r]) < x:
                        res = self.func(res, self.tree[r])
                        r -= 1
                return r + 1 - self.size
            res = self.func(self.tree[r],res)
        return 0


n,k = map(int,input().split())
M = 3*10**5+5
tree = SegTree(M,max,0)
for i in range(n):
    a = int(input())
    x = tree.get(max(0,a-k),min(a+k+1,M))
    tree.set(a,x+1)

print(tree.get(0,M))
