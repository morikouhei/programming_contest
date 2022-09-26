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

n,m,e = map(int,input().split())
edges = [[int(x)-1 for x in input().split()] for i in range(e)]
cut = [0]*e
q = int(input())
X = [int(input())-1 for i in range(q)]
for x in X:
    cut[x] = 1
ans = [0]*q
uf = Unionfind(n+m+1)
for i,(u,v) in enumerate(edges):
    if cut[i]:
        continue
    uf.union(u,v)

s = n+m
for i in range(m):
    uf.union(s,i+n)

for i in range(q)[::-1]:
    ans[i] = uf.size(s)-m-1
    u,v = edges[X[i]]
    uf.union(u,v)

for i in ans:
    print(i)