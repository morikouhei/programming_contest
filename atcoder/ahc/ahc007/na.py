import sys

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



n = 400
m = 1995
XY = [list(map(int,input().split())) for i in range(n)]

edges = [[int(x) for x in input().split()] for i in range(m)]


mincosts = []
for u,v in edges:
    x1,y1 = XY[u]
    x2,y2 = XY[v]
    cost = int(((x1-x2)**2+(y1-y2)**2)**0.5*1.8)
    mincosts.append(cost)
minlists = [[x,i] for i,x in enumerate(mincosts)]
minlists.sort()

use = [0]*m
sumlength = 0
uf_pre = Unionfind(n)
for i,(x,ind) in enumerate(minlists):
    u,v = edges[ind]
    if uf_pre.same(u,v):
        continue
    uf_pre.union(u,v)
    use[ind] = 1
    sumlength += x

lengths = [0]
now = 0
for i in range(m):
    if use[i]:
        now += mincosts[i]
    lengths.append(now)
# print(len(lengths),"length")

def update(index,done):
    nuf = Unionfind(n)
    nuse = [0]*m
    for i in range(index):
        if done[i]:
            u,v = edges[i]
            nuf.union(u,v)
            nuse[i] = 1

    for i,(x,ind) in enumerate(minlists):
        if ind <= index: continue
        u,v = edges[ind]
        if nuf.same(u,v):
            continue
        nuf.union(u,v)
        nuse[ind] = 1

    nlengths = [0]
    now = 0
    for i in range(m):
        if nuse[i]:
            now += mincosts[i]
        nlengths.append(now)

    if nuf.size(0) != n:
        nlengths[-1] = 10**20
    return nuse,nlengths


def update2(index,done):
    nuf = Unionfind(n)
    nuse = [0]*m
    for i in range(index+1):
        if done[i] or i == index:
            u,v = edges[i]
            nuf.union(u,v)
            nuse[i] = 1

    for i,(x,ind) in enumerate(minlists):
        if ind <= index: continue

        u,v = edges[ind]
        if nuf.same(u,v):
            continue
        nuf.union(u,v)
        nuse[ind] = 1

    nlengths = [0]
    now = 0
    for i in range(m):
        if nuse[i]:
            now += mincosts[i]
        nlengths.append(now)

    if nuf.size(0) != n:
        nlengths[-1] = 10**20

    return nuse,nlengths

uf = Unionfind(n)
done = [0]*m
for i in range(m):
    costnow = int(input())
    ans = use[i]
    u,v = edges[i]

    if uf.same(u,v):
        ans = 0
        print(ans)
        sys.stdout.flush()
        continue

    if ans and costnow > mincosts[i]:
        nuse,nlengths = update(i,done)
        if nlengths[-1] < lengths[-1]+costnow-mincosts[i]:
            # print(lengths[-1]+costnow-mincosts[i]-nlengths[-1],"dif")
            use = nuse
            lengths = nlengths
            ans = 0
    elif ans == 0 and costnow < mincosts[i]:
        nuse,nlengths = update2(i,done)
        if nlengths[-1]-(mincosts[i]-costnow) < lengths[-1]:

            # print(lengths[-1]+costnow-mincosts[i]-nlengths[-1],"dif")
            use = nuse
            lengths = nlengths
            ans = 1
        
    print(ans)
    sys.stdout.flush()
    if ans:
        uf.union(u,v)
        done[i] = 1




