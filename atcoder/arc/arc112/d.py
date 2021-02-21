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

h,w = map(int,input().split())
S = [list(input()) for i in range(h)]
S[0][0] = S[-1][0] = S[0][-1] = S[-1][-1] = "#"

useh = [0]*h
usew = [0]*w
uf = Unionfind(h+w)
for i in range(h):
    for j in range(w):
        if S[i][j] == "#":
            useh[i] = 1
            uf.union(i,h+j)

sh = set()
sw = set()
for i in range(h):
    sh.add(uf.find(i))
for i in range(h,h+w):
    sw.add(uf.find(i))
print(min(len(sh),len(sw))-1)