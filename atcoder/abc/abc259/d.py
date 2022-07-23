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
sx,sy,tx,ty = map(int,input().split())

XYR = [list(map(int,input().split())) for i in range(n)]

s = []
t = []
for i,(x,y,r) in enumerate(XYR):
    if (x-sx)**2+(y-sy)**2 == r**2:
        s.append(i)

    if (x-tx)**2+(y-ty)**2 == r**2:
        t.append(i)

if s == [] or t == []:
    print("No")
    exit()

uf = Unionfind(n)
for i in range(n):
    x,y,r = XYR[i]
    for j in range(i):
        nx,ny,nr = XYR[j]

        d = (x-nx)**2+(y-ny)**2
        if (r-nr)**2 <= d <= (r+nr)**2:
            uf.union(i,j)


for i in s:
    for j in t:
        if uf.same(i,j):
            print("Yes")
            exit()
print("No")