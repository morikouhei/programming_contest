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
A = [list(map(int,input().split())) for i in range(n)]
mod = 10**9+7

uf = Unionfind(n)
for i in range(n):
    for j in range(i):
        if A[i][j] == 1:
            if uf.same(i,j):
                print(0)
                exit()
            uf.union(i, j)

m = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(i):
        if A[i][j] == -1:
            x,y = uf.find(i),uf.find(j)
            m[x][x] += 1
            m[y][y] += 1
            m[x][y] -= 1
            m[y][x] -= 1

for i in range(n):
    x = uf.find(i)
    y = i
    m[x][x] += 1
    m[y][y] += 1
    m[x][y] -= 1
    m[y][x] -= 1

n -= 1
ans = 1
for i in range(n):

    for j in range(i+1,n):
        if m[j][i] != 0:
            m[i],m[j] = m[j],m[i]
            ans *= -1
            break
    if m[i][i] == 0:
        print(0)
        exit()
    ans *= m[i][i]
    ans %= mod

    inv = pow(m[i][i],mod-2,mod)
    for j in range(i,n):
        m[i][j] *= inv
        m[i][j] %= mod

    for j in range(i+1,n):
        x = m[j][i]
        for k in range(i,n):
            m[j][k] -= m[i][k]*x
            m[j][k] %= mod
print(ans)

