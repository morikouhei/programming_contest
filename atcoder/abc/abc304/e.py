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
uf = Unionfind(n)
for i in range(m):
    u,v = [int(x)-1 for x in input().split()]
    uf.union(u,v)

k = int(input())
bans = set()
for i in range(k):
    a,b = [int(x)-1 for x in input().split()]
    a,b = uf.find(a),uf.find(b)
    bans.add((a<<20)+b)
    bans.add((b<<20)+a)

q = int(input())
for _ in range(q):
    a,b = [int(x)-1 for x in input().split()]
    a,b = uf.find(a),uf.find(b)

    if (a<<20)+b in bans or (b<<20)+a in bans:
        print("No")
    else:
        print("Yes")