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
e = [[] for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    e[a].append(b)
    e[b].append(a)

ans = [0]*n
uf = Unionfind(n)
count = 0
for now in range(n-1,0,-1):
    count += 1
    for nex in e[now]:
        if nex > now:
            if uf.same(nex,now):
                continue
            uf.union(nex,now)
            count -= 1
    ans[now-1] = count
for i in ans:
    print(i)

