mod = 998244353
n,k = map(int,input().split())
a = [list(map(int,input().split())) for i in range(n)]

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

ux = Unionfind(n)
uy = Unionfind(n)
for i in range(n-1):
    for j in range(i+1,n):
        check = True
        for t in range(n):
            if a[i][t]+a[j][t] > k:
                check = False
                break
        if check:
            ux.union(i,j)
for i in range(n-1):
    for j in range(i+1,n):
        check = True
        for t in range(n):
            if a[t][i]+a[t][j] > k:
                check = False
                break
        if check:
            uy.union(i,j)

used = [0]*n
fact = [1,1]
for i in range(2,n+1):
    fact.append(fact[-1]*i%mod)
ans = 1
for i in range(n):
    p = ux.find(i)
    if used[p]:
        continue
    used[p] = 1
    s = ux.size(i)
    ans *= fact[s]
    ans %= mod

used = [0]*n
for i in range(n):
    p = uy.find(i)
    if used[p]:
        continue
    used[p] = 1
    s = uy.size(i)
    ans *= fact[s]
    ans %= mod
print(ans)