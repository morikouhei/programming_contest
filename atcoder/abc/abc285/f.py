import sys
input = sys.stdin.readline

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



def s2int(s):
    return ord(s)-ord("a")

n = int(input())
S = [s2int(s) for s in input().rstrip()]
q = int(input())
Q = [input().split() for i in range(q)]

sta = 0

def func(X,Y):
    return X+Y

segs = [SegTree(n,func,sta) for i in range(26)]
for i,s in enumerate(S):
    segs[s].set(i,1)

Snum = [0]*26
for s in S:
    Snum[s] += 1
for a,b,c in Q:
    if a == "1":
        b,c = int(b)-1,s2int(c)
        bef = S[b]
        segs[bef].set(b,0)
        segs[c].set(b,1)
        Snum[bef] -= 1
        Snum[c] += 1
        S[b] = c

    else:
        l,r = int(b)-1,int(c)

        first = 1
        last = 0
        ok = 1
        nl = l
        for i in range(26):
            num = segs[i].get(nl,r)
            nex = segs[i].get(nl,nl+num)
            if nex != num:
                ok = 0
                break
            if first:
                if num == 0:
                    continue
                else:
                    first = 0
                    nl += num
            else:
                if nex == Snum[i]:
                    nl += num
                    
                else:
                    if last:
                        ok = 0
                        break
                    elif nl+num == r:
                        nl += num
                    else:
                        ok = 0
                        break

        print("Yes" if ok else "No")


