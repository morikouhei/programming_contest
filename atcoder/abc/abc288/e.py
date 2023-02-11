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



n,m = map(int,input().split())
A = list(map(int,input().split()))
C = list(map(int,input().split()))
X = [0]*n
seg = SegTree(n,min,10**10)
seg.build(C)
for x in map(int,input().split()):
    X[x-1] = 1


Cmin = [[10**10]*n for i in range(n)]
for i in range(n):
    for j in range(i,n):
        Cmin[i][j] = min(C[j],Cmin[i][j-1])
inf = 10**20

dp = [inf]*(n+1)
dp[0] = 0
for i in range(n):
    ndp = [inf]*(n+1)
    a = A[i]
    x = X[i]
    for j in range(n+1):
        if dp[j] == inf:
            continue
        
        ndp[j+1] = min(ndp[j+1],dp[j]+a+Cmin[max(i-j,0)][i])
        # print(i,j,i-j,i+1)
        if x == 0:
            ndp[j] = min(ndp[j],dp[j])
    dp = ndp
    # print(dp)
print(min(dp))
