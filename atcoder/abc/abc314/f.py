class Unionfind:
     
    def __init__(self,n):
        self.uf = [-1]*n
 
    def find(self,x):
        if self.uf[x] < 0:
            return x
        else:
            self.uf[x] = self.find(self.uf[x])
            return self.uf[x]
 
    def same(self,x,y):
        return self.find(x) == self.find(y)
 
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.uf[x] > self.uf[y]:
            x,y = y,x
        self.uf[x] += self.uf[y]
        self.uf[y] = x
        return True
 
    def size(self,x):
        x = self.find(x)
        return -self.uf[x]


n = int(input())
mod = 998244353

uf = Unionfind(n)

match = []

for i in range(n-1):
    p,q = [int(x)-1 for x in input().split()]
    p = uf.find(p)
    q = uf.find(q)

    sp = uf.size(p)
    sq = uf.size(q)

    uf.union(p,q)

    c = uf.find(p)

    match.append([c,p,q,sp,sq])

ans = [0]*n
for c,p,q,sp,sq in match[::-1]:
    s = sp+sq
    invs = pow(s,mod-2,mod)
    base = ans[c]

    ans[p] = (base + sp * invs) % mod
    ans[q] = (base + sq * invs) % mod
print(*ans)
