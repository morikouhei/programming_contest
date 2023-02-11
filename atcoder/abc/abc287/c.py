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
UV = [[int(x)-1 for x in input().split()] for i in range(m)]

if m != n-1:
    print("No")
    exit()


nums = [0]*n
for u,v in UV:
    nums[u] += 1
    nums[v] += 1

if nums.count(1) != 2 or nums.count(2) != n-2:
    print("No")
    exit()

uf = Unionfind(n)
for u,v in UV:
    uf.union(u,v)

if uf.size(0) == n:
    print("Yes")
else:
    print("No")