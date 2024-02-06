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
ABW = []
for _ in range(m):
    a,b,w = map(int,input().split())
    a,b = a-1,b-1
    ABW.append([w,a,b])

ABW.sort()

uf = Unionfind(n)
e = [[] for i in range(n)]
for _,a,b in ABW:
    if uf.same(a,b):
        continue
    uf.union(a,b)
    e[a].append(b)
    e[b].append(a)

vis = [0]*n
color = [0]*n

vis[0] = 1

q = [0]
while q:
    now = q.pop()

    for nex in e[now]:
        if vis[nex]:
            continue
        vis[nex] = 1
        color[nex] = color[now]^1
        q.append(nex)


ans = 10**10

we = [[] for i in range(n)]
for w,a,b in ABW:
    if color[a] == color[b]:
        ans = min(ans,w)
    else:
        we[a].append(w)
        we[b].append(w)

for w in we:
    if len(w) < 2:
        continue
    w.sort()
    ans = min(ans,w[0]+w[1])
print(ans)