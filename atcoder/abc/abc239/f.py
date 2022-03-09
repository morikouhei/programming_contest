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
D = list(map(int,input().split()))

uf = Unionfind(n)
for i in range(m):
    a,b = [int(x)-1 for x in input().split()]
    uf.union(a,b)
    D[a] -= 1
    D[b] -= 1


one = []
cand = [[] for i in range(n)]
for i in range(n):
    if D[i] < 0:
        print(-1)
        exit()
    p = uf.find(i)
    for j in range(D[i]):
        cand[p].append(i+1)

for i in range(n):
    if len(cand[i]) == 1:
        one.append(cand[i].pop())

ans = []
for i in range(n):
    if cand[i] == []:
        continue

    for j in range(len(cand[i])-1):
        if one == []:
            print(-1)
            exit()
        ans.append([one.pop(),cand[i].pop()])
        uf.union(ans[-1][0],ans[-1][1])
    one.append(cand[i].pop())

if len(one) != 2:
    print(-1)
    exit()
ans.append([one[0],one[1]])
uf.union(ans[-1][0],ans[-1][1])
if uf.size(0) != n:
    print(-1)
    exit()
    
for i in ans:
    print(*i)