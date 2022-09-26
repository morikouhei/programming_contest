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
X = list(map(int,input().split()))
Y = list(map(int,input().split()))
ABZ = []
for i in range(m):
    a,b,z = map(int,input().split())
    ABZ.append([a-1,b-1,z])
inf = 10**20

costX = []
costY = []

for i,x in enumerate(X):
    costX.append([i,n,x])
for i,y in enumerate(Y):
    costY.append([i,n+1,y])


def calc(costs):
    costs.sort(key=lambda x:x[2])

    count = 0
    uf = Unionfind(n+2)
    for u,v,c in costs:
        if uf.same(u,v):
            continue
        uf.union(u,v)
        count += c

    p = uf.find(0)
    for i in range(n):
        if uf.find(i) != p:
            return inf
    return count

ans = calc(ABZ)
ans = min(ans,calc(ABZ+costX))
ans = min(ans,calc(ABZ+costY))
ans = min(ans,calc(ABZ+costX+costY))
print(ans)