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

ST = [input().split() for i in range(n)]

names = set()
for s,t in ST:
    names.add(s)
    names.add(t)


l = len(names)
names = sorted(names)
dic = {s:i for i,s in enumerate(names)}

uf = Unionfind(l)
for s,t in ST:
    s,t = dic[s],dic[t]
    if uf.same(s,t):
        print("No")
        exit()
    uf.union(s,t)
print("Yes")