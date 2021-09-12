n,m = map(int,input().split())
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

E = [list(map(int,input().split())) for i in range(m)]

uf = Unionfind(n)
E.sort(key=lambda x:x[2])
ans = 0
for a,b,c in E:
    a -= 1
    b -= 1
    if uf.same(a,b):
        if c > 0:
            ans += c
    else:
        uf.union(a,b)
print(ans)
