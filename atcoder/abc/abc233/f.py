from collections import deque

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
P = [int(x)-1 for x in input().split()]
m = int(input())
edges = []
dic = {}
uf = Unionfind(n)
e = [[] for i in range(n)]
edges = [[int(x)-1 for x in input().split()] for i in range(m)]
for i,(a,b) in enumerate(edges):
    dic[(a,b)] = dic[(b,a)] = i
    
    if uf.same(a,b):
        continue
    uf.union(a,b)
    e[a].append(b)
    e[b].append(a)


indP = [-1]*n
for i,p in enumerate(P):
    indP[p] = i

ans = []
dis = [n]*n
par = [-1]*n

for i in range(n):
    if P[i] == i:
        continue

    vis = []
    dis[i] = 0
    q = deque([i])
    while q:
        now = q.popleft()
        vis.append([dis[now],now])
        for nex in e[now]:
            if dis[nex] > dis[now]+1:
                dis[nex] = dis[now]+1
                par[nex] = now
                q.append(nex)

    vis.sort()
    for _,ind in vis:
        if not uf.same(ind,indP[ind]):
            print(-1)
            exit()

    for _,ind in vis[::-1]:
        ndis = [n]*n
        npar = [-1]*n
        q = deque([ind])
        ndis[ind] = 0
        while q:
            now = q.popleft()
            for nex in e[now]:
                if ndis[nex] == n:
                    ndis[nex] = ndis[now]+1
                    npar[nex] = now
                    q.append(nex)

        start = indP[ind]
        while start != ind:
            p = npar[start]
            ans.append(dic[(start,p)]+1)
            indP[P[start]],indP[P[p]] = indP[P[p]],indP[P[start]]
            P[start],P[p] = P[p],P[start]    
            start = p

print(len(ans))
print(*ans)

