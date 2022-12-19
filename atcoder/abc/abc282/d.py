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

n,m = map(int,input().split())
e = [[] for i in range(n)]
uf = Unionfind(n)
for _ in range(m):
    u,v = [int(x)-1 for x in input().split()]
    e[u].append(v)
    e[v].append(u)
    uf.union(u,v)

dist = [n+5]*n
used = [0]*n

ans = 0
base = 0
for i in range(n):
    if used[i]:
        continue
    used[i] = 1
    dist[i] = 0
    q = deque([i])
    nums = [0,0]
    nums[0] += 1
    count = 0
    while q:
        now = q.popleft()
        count += len(e[now])
        for nex in e[now]:
            if used[nex]:
                if dist[nex]%2 != (dist[now]+1)%2:
                    print(0)
                    exit()
            else:
                used[nex] = 1
                dist[nex] = dist[now]+1
                nums[dist[nex]%2] += 1
                q.append(nex)
    s = uf.size(i)
    base += sum(nums)*(n-s)
    ans += nums[0]*nums[1]-count//2
print(ans+base//2)
    

            