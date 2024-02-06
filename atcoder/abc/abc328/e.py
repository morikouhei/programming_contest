import itertools

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

n,m,k = map(int,input().split())

UVW = []
for i in range(m):
    u,v,w = map(int,input().split())
    u,v = u-1,v-1
    UVW.append([u,v,w])

ans = 10**20

for l in itertools.combinations(range(m),n-1):

    uf = Unionfind(n)

    cost = 0
    for ind in l:
        u,v,w = UVW[ind]
        uf.union(u,v)
        cost += w

    if uf.size(0) == n:
        ans = min(ans,cost%k)
print(ans)
