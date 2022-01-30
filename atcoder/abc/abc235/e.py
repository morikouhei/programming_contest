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

n,m,q = map(int,input().split())

E = [list(map(int,input().split())) for i in range(m+q)]
iC = [[E[i][2],i] for i in range(m+q)]
iC.sort()


uf = Unionfind(n+1)
ans = [0]*q

for _,ind in iC:
    x,y,_ = E[ind]
    if uf.same(x,y):
        continue
    if ind < m:
        uf.union(x,y)
    else:
        ans[ind-m] = 1

for i in ans:
    print("Yes" if i else "No")