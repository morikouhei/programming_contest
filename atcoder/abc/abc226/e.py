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


n,m = map(int,input().split())

mod = 998244353

loop = [0]*n
uf = Unionfind(n)
for i in range(m):
    u,v = [int(x)-1 for x in input().split()]
    if uf.same(u,v):
        loop[u] += 1
    else:
        uf.union(u,v)

ans = 1

ok = [0]*n
for i in range(n):
    if uf.find(i) == i:
        ans *= 2
        ans %= mod
    if loop[i]:
        ok[uf.find(i)] += 1

for i in range(n):
    if uf.find(i) != i:
        continue
    if ok[i] == 1:
        continue
    ans = 0
print(ans)