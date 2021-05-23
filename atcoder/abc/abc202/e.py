from collections import deque,defaultdict
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
P = list(map(int,input().split()))
e = [[] for i in range(n)]
for i,p in enumerate(P,1):
    e[p-1].append(i)
    e[i].append(p-1)
q = int(input())
Q = [list(map(int,input().split())) for i in range(q)]

l = [[] for i in range(n)]
for i,(u,d) in enumerate(Q):
    l[u-1].append((d,i))
ans = [0]*q
dis = [n+1]*n
dis[0] = 0
q = deque([0])
order = []
while q:
    now = q.pop()
    order.append(now)
    for nex in e[now]:
        if dis[nex] == n+1:
            dis[nex] = dis[now]+1
            q.append(nex)

lis = [defaultdict(int) for i in range(n)]
uf = Unionfind(n)
for i in order[::-1]:
    cand = []
    add = []
    ms = -1
    p = -1
    ind = -1
    for nex in e[i]:
        if dis[nex] < dis[i]:
            continue
        add.append(nex)
        if uf.size(nex) > ms:
            ms = uf.size(nex)
            ind = nex
    if ind == -1:
        lis[i][dis[i]] += 1 
        for d, ind in l[i]:
            ans[ind] = lis[i][d]
    else:
        p = uf.find(ind)
        uf.union(p,i)

        for nex in add:
            if nex == ind:
                continue

            for x,y in lis[uf.find(nex)].items():
                lis[p][x] += y
            uf.union(p,nex)
        lis[p][dis[i]] += 1
        for d, ind in l[i]:
            ans[ind] = lis[p][d]
        
    #print(p,i,lis[p],lis[i])
for i in ans:
    print(i)
        
    

