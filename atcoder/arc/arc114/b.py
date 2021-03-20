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
f = list(map(int,input().split()))
mod = 998244353

uf = Unionfind(n+1)
for i,x in enumerate(f,1):
    uf.union(x,i)
ans = 1
for i in range(1,n+1):
    if uf.find(i) == i:
        ans *= 2
        ans %= mod
print((ans-1)%mod)