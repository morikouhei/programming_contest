from heapq import heappush,heappop
import heapq
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
road = [0]*n

uf = Unionfind(n)
for i in range(m):
    a,b = [int(x)-1 for x in input().split()]
    uf.union(a,b)
    road[a] += 1
    road[b] += 1

dif = 0
group = {}
for i in range(n):
    if road[i] > D[i]:
        print(-1)
        exit()
    dif += D[i]-road[i]

if dif//2 != n-m-1:
    print(-1)
    exit()


for i in range(n):
    p = uf.find(i)
    if p not in group:
        group[p] = []

    
    if D[i] > road[i]:
        heappush(group[p],[-D[i]+road[i],i+1])

if len(group) > 1:
    for v in group.values():
        if v == []:
            print(-1)
            exit()


ans = []

h = []
for g,v in group.items():
    count = 0
    for x in v:
        count += x[0]
    a,b = heappop(v)
    heappush(h,[count,a,b])
print(h)
while h and len(h) > 1:
    print(h)
    s1,n1,i1 = heappop(h)
    s2,n2,i2 = heappop(h)
    ans.append([i1,i2])
    print(n1,i1,n2,i2)
    n1 += 1
    s1 += 1
    n2 += 1
    s2 += 1
    p1 = uf.find(i1-1)
    p2 = uf.find(i2-1)
    uf.union(i1-1,i2-1)
    if len(group[p1]) > len(group[p2]):
        p1,p2 = p2,p1
    for l in group[p1]:
        heappush(group[p2],l)

    if uf.find(p2) != p2:
        uf.uf[p2] = uf.uf[p1]
        uf.uf[p1] = p2
    print(uf.uf)
    del group[p1]
    if n1 != 0:
        heappush(h,[s1+s2,n1,i1])
        heappush(group[p2],[n2,i2])
    elif n2 != 0:
        heappush(h,[s1+s2,n2,i2])
    else:
        if group[p2]:
            a,b = heappop(group[p2])

            heappush(h,[s1+s2,a,b])

if uf.size(0) != n:
    print(-1)
    exit()

all = group[uf.find(0)]
if h:
    _a,b = heappop(h)
    heappush(all,[a,b])
print(all)
while True:
    if all:
        n1,i1 = heappop(all)
        n2,i2 = heappop(all)
        ans.append([i1,i2])
        n1 += 1
        n2 += 1
        if n1 != 0:
            heappush(all,[n1,i1])
        if n2 != 0:
            heappush(all,[n2,i2])

    else:
        break

for i in ans:
    print(*i)