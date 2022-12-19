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

    

n,m,q = map(int,input().split())

uf = Unionfind(n)
e = [[] for i in range(n)]

for i in range(m):
    a,b,c = map(int,input().split())
    a,b = a-1,b-1
    uf.union(a,b)

    e[a].append([b,c])
    e[b].append([a,-c])

vis = [0]*n
dis = [0]*n
inf = 10**20

def dfs(x):
    q = [x]
    vis[x] = 1
    inf_flag = False
    while q:
        now = q.pop()
        for nex,c in e[now]:
            if vis[nex]:
                if c+dis[now] != dis[nex]:
                    inf_flag = True
            else:
                vis[nex] = 1
                dis[nex] = dis[now]+c
                q.append(nex)
    if inf_flag:
        dis[x] = inf
    return 

for i in range(n):
    if vis[i]:
        continue
    p = uf.find(i)
    dfs(p)

for _ in range(q):
    x,y = map(int,input().split())
    x,y = x-1,y-1
    if uf.same(x,y):
        p = uf.find(x)
        if dis[p] == inf:
            print("inf")
        else:
            print(dis[y]-dis[x])
    else:
        print("nan")