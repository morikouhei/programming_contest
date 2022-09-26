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


import sys
sys.setrecursionlimit(3*10**5)
n = int(input())
e = [[] for i in range(n)]
for _ in range(n):
    u,v = [int(x)-1 for x in input().split()]
    e[u].append(v)
    e[v].append(u)

q = int(input())
XY = [[int(x)-1 for x in input().split()] for i in range(q)]

par = [-1]*n
vis = [0]*n
cycle = []
def dfs(x,p=-1):

    vis[x] = 1
    for nex in e[x]:
        if nex == p:
            continue
        if vis[nex]:
            # print("here",nex)
            cycle.append(x)
            return nex
        else:
            find = dfs(nex,x)
            if find >= 0:
                cycle.append(x)
                if find == x:
                    return -1
                else:
                    return find
    return -1

dfs(0)
# print(cycle)
uf = Unionfind(n)

cycle = set(cycle)
for i in range(n):
    if i in cycle:
        continue
    for nex in e[i]:
        uf.union(i,nex)


for x,y in XY:
    if uf.same(x,y):
        print("Yes")
    else:
        print("No")