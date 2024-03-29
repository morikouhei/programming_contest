import sys
input = sys.stdin.readline
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

    def build(self, lis):
        for i, l in enumerate(lis,self.size):
            self.data[i] = l
        for i in range(self.size-1, 0, -1):
            self.update(i)

    def point_set(self, p, x):
        p += self.size
        for i in range(self.log, 0, -1):
            self.push(p >> i)
        self.data[p] = x
        for i in range(1,self.log+1):
            self.update(p>>i)

    def point_get(self, p):
        p += self.size
        for i in range(self.log, 0,-1):
            self.push(p >> i)
        return self.data[p]

    def apply(self, p, f):
        p += self.size
        for i in range(self.log, 0, -1):
            self.push(p >> i)
        self.data[p] = self.mapping(f, self.data[p])
        for i in range(1, self.log+1):
            self.update(p >> i)

    def range_apply(self, l, r, f):
        ''' change the value you define in "mapping" and "composition" of [l,r) '''
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

    def all_apply(self, k, f):
        self.data[k] = self.mapping(f, self.data[k])
        if k < self.size:
            self.lazy[k] = self.composition(f, self.lazy[k])

    def push(self, k):
        self.all_apply(2*k, self.lazy[k])
        self.all_apply(2*k+1, self.lazy[k])
        self.lazy[k] = self.id

    def prod(self, l, r):
        ''' get the value you define in "op" of [l,r) '''
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


def op(x, y):
    return max(x,y)

def mapping(p, x):
    return max(p,x)

def composition(p, q):
    return max(p,q)

e = -1
id = -1

n = int(input())
LR = [list(map(int,input().split())) for i in range(n)]
s = set()
for l,r in LR:
    s.add(l)
    s.add(r)
s.add(0)
s.add(10**10)
s = sorted(s)
dic = {x:i for i,x in enumerate(s)}
rdic = {i:x for i,x in enumerate(s)}

le = len(s)
lazyseg_score = LazySegTree(le, op, e, mapping, composition, id)
lazyseg_func = LazySegTree(le, op, e, mapping, composition, id)

dp = [-10**10]*(n+1)
# print(s)

for i,(l,r) in enumerate(LR):
    lid = dic[l]
    rid = dic[r]

    ## get the max value of point l
    # print(i,l,r)
    cand = lazyseg_score.prod(0,lid)
    
    lval = max(cand,0)+1
    
    id = lazyseg_func.point_get(lid)

    # print(lval,id)
    if id != -1:
        rval = dp[id]
        br = LR[id][1]
        lval = max(lval,rval- (br-l))
        # print("yes",id,rval,lval)

    rval = lval + r-l
    dp[i] = rval
    # print("score",rval)
    lazyseg_score.point_set(rid,rval)
    lazyseg_func.range_apply(lid,rid+1,i)

ans = lazyseg_score.prod(0,le)
print(ans)