from collections import deque
n,m = map(int,input().split())
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
uf = Unionfind(n)
e = [[] for i in range(n)]

for i in range(m):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    e[a].append(b)
    e[b].append(a)
    uf.union(a,b)

def calc(x,cands):
    s = uf.size(x)
    count = 0
    
    for i in range(1<<s):
        color = [0]*n
        base = 1
        for j in range(s):
            if i >> j & 1:
                color[cands[j]] = 1
        for j in cands:
            if color[j] == 0:
                continue
            for k in e[j]:
                if color[k]:
                    base = 0
        if base == 0:
            continue
        dis = [-1]*n
        for j in cands:
            if dis[j] != -1 or color[j]:
                continue
            q = deque([j])
            dis[j] = 0
            while q:
                now = q.popleft()
                for nex in e[now]:
                    if color[nex]:
                        continue
                    if dis[nex] == dis[now]:
                        base = 0
                        break
                    if dis[nex] == -1:
                        dis[nex] = dis[now]^1
                        q.append(nex)
            if base == 0:
                break
            base *= 2
        count += base

    return count

ans = 1
for i in range(n):
    if uf.find(i) == i:
        cand = []
        for j in range(n):
            if uf.find(j) == i:
                cand.append(j)
        ans *= calc(i,cand)
        
print(ans)
