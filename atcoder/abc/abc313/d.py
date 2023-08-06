import sys

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

n,k = map(int,input().split())

X = [i for i in range(1,k+1)]

def query(X):
    print("?",*X)
    sys.stdout.flush()

    return int(input())

uf = Unionfind(n)
base = k-1

tbase = query(X)
opp = -1
asked = [0]*n
asked[base] = 1

last = base

for i in range(base+1,n):

    asked[i] = 1

    X.pop()
    X.append(i+1)
    
    ti = query(X)

    if tbase == ti:
        uf.union(base,i)
    else:
        if opp == -1:
            opp = i
        else:
            uf.union(opp,i)
tn = ti
X.append(base+1)

dif = tn^tbase
for i in range(base):
    X.remove(i+1)

    ti = query(X)
    asked[i] = 1
    if ti == tn:
        uf.union(base,i)
    else:
        if opp == -1:
            opp = i
        else:
            uf.union(opp,i)
    X.append(i+1)

X.pop()
count = 0
for i in X:
    if uf.same(base,i-1):
        count += 1

if count%2:
    if ti:
        baseans = 1
    else:
        baseans = 0
else:
    if ti:
        baseans = 0
    else:
        baseans = 1

ans = []
for i in range(n):
    if uf.same(i,base):
        ans.append(baseans)
    else:
        ans.append(baseans^1)

print("!",*ans)
sys.stdout.flush()