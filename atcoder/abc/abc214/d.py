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
e = [list(map(int,input().split())) for i in range(n-1)]
e.sort(key=lambda x:x[2])
uf = Unionfind(n)
ans = 0
for u,v,w in e:
    u -= 1
    v -= 1
    if uf.same(u,v):
        continue
    ans += uf.size(u)*uf.size(v)*w
    uf.union(u,v)
print(ans)