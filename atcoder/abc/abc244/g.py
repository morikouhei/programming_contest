import sys
sys.setrecursionlimit(3*10**5)
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
uf = Unionfind(n)
e = [[] for i in range(n)]
icount = [0]*n
for i in range(m):
    u,v = [int(x)-1 for x in input().split()]
    if uf.same(u,v):
        continue
    e[u].append(v)
    e[v].append(u)
    icount[u] += 1
    icount[v] += 1
    uf.union(u,v)
S = [int(i) for i in input()]

for i in range(n):
    if icount[i] == 1:
        p = i
        break

p2 = e[p][0]

count = [0]*n
ans = []

def dfs(x,p):
    ans.append(x+1)
    count[x] ^= 1

    for nex in e[x]:
        if nex == p:
            continue
        dfs(nex,x)
        ans.append(x+1)
        count[x] ^= 1
    
    if count[x] != S[x]:
        ans.append(p+1)
        count[p] ^= 1
        ans.append(x+1)
        count[x]^= 1
    return 

dfs(p2,p)

now = p2
for i in range(10):
    if count[p2] == S[p2] and count[p] == S[p]:
        break
    if now == p2:
        ans.append(p+1)
        now = p
        count[p] ^= 1
    else:
        ans.append(p2+1)
        now = p2
        count[p2] ^= 1

print(len(ans))
print(*ans)


