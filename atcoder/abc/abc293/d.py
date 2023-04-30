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
ABCD = [list(input().split()) for i in range(m)]

uf = Unionfind(n)
loop = 0

for a,b,c,d in ABCD:
    a,c = int(a)-1,int(c)-1
    if uf.same(a,c):
        loop += 1
    uf.union(a,c)

gr = 0
for i in range(n):
    if uf.find(i) == i:
        gr += 1

print(loop,gr-loop)