import sys

n = 400
m = 1995
XY = [list(map(int,input().split())) for i in range(n)]

edges = [[int(x) for x in input().split()] for i in range(m)]

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



mincosts = []
for u,v in edges:
    x1,y1 = XY[u]
    x2,y2 = XY[v]
    cost = (x1-x2)**2+(y1-y2)**2
    mincosts.append(cost)
minlists = [[x,i] for i,x in enumerate(mincosts)]
minlists.sort()

use = [0]*m

uf_prepare = Unionfind(n)
for i,(x,ind) in enumerate(minlists):
    u,v = edges[ind]
    if uf_prepare.same(u,v):
        continue
    uf_prepare.union(u,v)
    use[ind] = 1

uf = Unionfind(n)
count = 0
for i in range(m):
    costnow = int(input())

    ans = use[i]

    u,v = edges[i]

    if uf.same(u,v):
        ans = 0

    print(ans)
    sys.stdout.flush()
    if ans:
        uf.union(u,v)
        count += costnow





