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
P = list(map(int,input().split()))
Q = list(map(int,input().split()))
mod = 998244353

def calc(x):
    if x == 1:
        return 1

    num = 0
    dp = [0]*(x+5)
    dp[0] = 1
    for i in range(x):
        dp[i+1] += dp[i]
        dp[i+2] += dp[i]
        dp[i+1] %= mod
        dp[i+2] %= mod
    num += dp[x]
    dp = [0]*(x+5)
    dp[1] = 1
    for i in range(x):
        dp[i+1] += dp[i]
        dp[i+2] += dp[i]
        dp[i+1] %= mod
        dp[i+2] %= mod
    num += dp[x+1]
    return num%mod



pind = [0]*n
qind = [0]*n
for i,p in enumerate(P):
    pind[p-1] = i

for i,q in enumerate(Q):
    qind[q-1] = i
uf = Unionfind(n)
for i in range(n):
    p = P[i]
    uf.union(i,qind[p-1])
    q = Q[i]
    uf.union(i,pind[q-1])

ans = 1
for i in range(n):
    if uf.find(i) == i:

        ans *= calc(uf.size(i))
        ans %= mod
print(ans)