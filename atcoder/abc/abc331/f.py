
mod = 998244353

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


def func(x,y):
    return (x+y)%mod

n,q = map(int,input().split())
S = input()
Q = [input().split() for i in range(q)]

seg1 = SegTree(n,func,0)
seg2 = SegTree(n,func,0)


L1 = [0]*n
L2 = [0]*n

base = 37

pows = [1]*(n+1)
for i in range(n):
    pows[i+1] = (pows[i]*base)%mod
def add(i,s):

    c = ord(s)-ord("a")+1

    nl1 = c * pows[i]
    dif = nl1 - L1[i]

    seg1.set(i,nl1)

    L1[i] = nl1

    nl2 = c * pows[n-1-i]
    dif = nl2 - L2[n-1-i]

    seg2.set(n-1-i,nl2)
    L2[n-1-i] = nl2


def get(l,r):

    val = seg1.get(l,r+1) * pow(pows[l],mod-2,mod) #* pows[r-l+1]
    val %= mod

    nl,nr = n-1-l,n-1-r
    val2 = seg2.get(nr,nl+1) * pow(pows[nr],mod-2,mod)#- seg2.get(0,nr) #* pows[r-l+1]
    val2 %= mod

    return "Yes" if val == val2 else "No"

for i,s in enumerate(S):
    add(i,s)

for q in Q:
    t,l,r = q
    t = int(t)

    if t == 1:
        add(int(l)-1,r)
    else:
        ans = get(int(l)-1,int(r)-1)
        print(ans)

