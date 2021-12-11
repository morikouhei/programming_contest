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
        if y > x:
            x,y = y,x
        self.uf[x] += self.uf[y]
        self.uf[y] = x
        return True
 
    def size(self,x):
        x = self.find(x)
        return -self.uf[x]

q = int(input())
n = 1<<20
A = [-1]*n
TX = [list(map(int,input().split())) for i in range(q)]


uf = Unionfind(n)
for t,x in TX:
    if t == 1:
        now = x%n
        if A[now] == -1:
            A[now] = x
            if now != n-1:
                uf.union(now+1,now)
            continue

        while True:
            cand = uf.find(now)
            if A[cand] == -1:
                break
            if cand < n-1:
                uf.union(cand,cand+1)
                now = cand
            else:
                now = 0
        A[cand] = x


    if t == 2:
        print(A[x%n])
