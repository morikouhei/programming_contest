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
XY = []
for i in range(n):
    x,y = map(int,input().split())
    XY.append([x+1000,y+1000])


uf = Unionfind(2001**2)


s = set()
s.add((-1,-1))
s.add((-1,0))
s.add((0,-1))
s.add((0,1))
s.add((1,0))
s.add((1,1))
for i in range(n):
    x,y = XY[i]
    for j in range(i):
        nx,ny = XY[j]
        dx = x-nx
        dy = y-ny
        if (dx,dy) in s:
            uf.union(x*2001+y,nx*2001+ny)
            # print(i,j,dx,dy)

ans = 0
for i in range(n):
    x,y = XY[i]
    if uf.find(x*2001+y) == x*2001+y:
        ans += 1
print(ans)
        