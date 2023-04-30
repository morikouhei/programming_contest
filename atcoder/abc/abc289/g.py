from collections import deque

class ConvexHullTrick():

    def __init__(self):
        self.q = deque()


    def _f(self,fi,x):
        return fi[0]*x + fi[1]

    def _check(self,f1,f2,f3):
        return (f2[0] - f1[0]) * (f3[1] - f2[1]) >= (f2[1] - f1[1]) * (f3[0] - f2[0])

    def add(self,a,b):
        fi = (a,b)
        while len(self.q) >= 2 and self._check(self.q[-2],self.q[-1],fi):
            self.q.pop()
        self.q.append(fi)


    def query(self,x):
        while len(self.q) >= 2 and self._f(self.q[0],x) <= self._f(self.q[1],x):
            self.q.popleft()
        return self._f(self.q[0],x)


n,m = map(int,input().split())
B = sorted(list(map(int,input().split())),reverse=True)
C = list(map(int,input().split()))

cht = ConvexHullTrick()
for i,b in enumerate(B,1):
    cht.add(i,b*i)

sC = sorted([[c,i] for i,c in enumerate(C)])
ans = [0]*m

for c,i in sC:
    ans[i] = cht.query(c)

print(*ans)