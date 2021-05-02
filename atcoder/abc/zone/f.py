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
count = [0]*n
for a in A:
    count[a] = 1

uf = Unionfind(n)

ans = []
for i in range(n):
    if count[i]:
        continue
    if uf.same(0,i):
        continue
    for j in range(n):
        x = j^i
        if uf.same(j,x):
            continue
        ans.append([j,x])
        uf.union(j,x)

if uf.size(0) == n:
    for i in ans:
        print(*i)
else:
    print(-1)