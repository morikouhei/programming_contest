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
A = list(map(int,input().split()))


edges = []
for i in range(n):
    for j in range(i):
        a,na = A[i],A[j]
        cost = (pow(a,na,m)+pow(na,a,m))%m
        edges.append([cost,i,j])

ans = 0
uf = Unionfind(n)
edges.sort(reverse=True)
for cost,i,j in edges:
    if uf.same(i,j):
        continue
    ans += cost
    uf.union(i,j)
print(ans)