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
C = [list(map(int,input().split())) for i in range(m)]
uf = Unionfind(n+1)
C.sort()
ans = 0
for c,l,r in C:
    if uf.same(l-1,r):
        continue
    uf.union(l-1,r)
    ans += c
if uf.size(0) == n+1:
    print(ans)
else:
    print(-1)