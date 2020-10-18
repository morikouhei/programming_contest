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


t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    UF = Unionfind(n+1)
    l = [list(map(int,input().split())) for i in range(m)]
    for a,b in l:
        UF.union(a,b)
    count = 0
    for a,b in l:
        if UF.same(a,n) and UF.same(b,n):
            count += 1
    x = UF.size(n)
    print(x,count,n-x)
    cal = (n-x)*(n-x-1)//2-(m-count)
    if cal%2:
        print("First")
    else:
        print("First")