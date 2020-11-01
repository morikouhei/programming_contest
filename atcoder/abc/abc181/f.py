n = int(input())
xy = [list(map(int,input().split())) for i in range(n)]
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

uf = Unionfind(n+2)
l = []
for i in range(n):
    x,y = xy[i]
    l.append((100-y,i,n))
    l.append((y+100,i,n+1))
    for j in range(n):
        if i == j:
            continue
        a,b = xy[j]
        l.append((((a-x)**2+(b-y)**2)**0.5,i,j))
l.sort()
for dis,i,j in l:
    uf.union(i,j)
    if uf.same(n,n+1):
        print(dis/2)
        exit()