import sys
input = sys.stdin.readline
from collections import defaultdict
  
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

n,Q = map(int,input().split())
c = list(map(int,input().split()))
q = [tuple(map(int,input().split())) for i in range(Q)]

l = [defaultdict(int) for i in range(n)]

uf = Unionfind(n)
for i in range(n):
    l[i][c[i]] = 1

ans = []
for x,a,b in q:
    if x == 1:
        a -= 1
        b -= 1
        pa = uf.find(a)
        pb = uf.find(b)
        if pa == pb:
            continue
        if uf.size(pa) < uf.size(pb):
            pa,pb = pb,pa
        for j,t in l[pb].items():
            l[pa][j] += t 
        uf.union(a,b)
    else:
        a -= 1
        pa = uf.find(a)
        ans.append(l[pa][b])
for i in ans:
    print(i)
     