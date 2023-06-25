import sys
sys.setrecursionlimit(4*10**5)

class Unionfind:
     
    def __init__(self,n):
        self.uf = [-1]*n
        self.edges = [0]*n
        self.ans = [0]*n
        self.score = 0
        self.history = []
 
    def find(self,x):
        if self.uf[x] < 0:
            return x
        else:
            return self.find(self.uf[x])
            
 
    def same(self,x,y):
        return self.find(x) == self.find(y)
 
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            x_uf = self.uf[x]
            x_score = self.ans[x]
            x_edge = self.edges[x]
            self.score -= x_score

            self.uf[x] = x_uf
            self.edges[x] = x_edge + 1
            self.ans[x] = min(-x_uf,x_edge+1)

            self.score += self.ans[x]
            self.history.append([[x,x_uf,x_score,x_edge,self.ans[x]-x_score]])


            return False
        if self.uf[x] > self.uf[y]:
            x,y = y,x

        
        x_uf = self.uf[x]
        x_score = self.ans[x]
        x_edge = self.edges[x]
        self.score -= x_score

        y_uf = self.uf[y]
        y_score = self.ans[y]
        y_edge = self.edges[y]
        self.score -= y_score


        self.uf[x] = x_uf + y_uf
        self.edges[x] = x_edge + 1 + y_edge
        self.ans[x] = min( -x_uf - y_uf,x_edge + 1 + y_edge)
        self.score += self.ans[x]

        self.uf[y] = x
        self.edges[y] = 0
        self.ans[y] = 0
        self.score += self.ans[y]

        self.history.append([[x,x_uf,x_score,x_edge,self.ans[x]-x_score],[y,y_uf,y_score,y_edge,self.ans[y]-y_score]])

        return True
 
    def size(self,x):
        x = self.find(x)
        return -self.uf[x]


    def roll_back(self):
        hist = self.history.pop()
        for x,x_uf,x_score,x_edge,dscore in hist:
            self.uf[x] = x_uf
            self.ans[x] = x_score
            self.edges[x] = x_edge
            self.score -= dscore


n = int(input())
AB = [[int(x)-1 for x in input().split()] for i in range(n)]

e = [[] for i in range(n)]
for _ in range(n-1):
    u,v = [int(x)-1 for x in input().split()]
    e[u].append(v)
    e[v].append(u)

ans = [0]*n
uf = Unionfind(n)

q = [(0,-1)]


# def dfs(now,p):
#     a,b = AB[now]
#     uf.union(a,b)
#     ans[now] = uf.score
#     for nex in e[now]:
#         if nex == p:
#             continue
#         dfs(nex,now)
#     uf.roll_back()

#     return

# dfs(0,-1)

while q:
    now,p = q.pop()
    if now < 0:
        uf.roll_back()
        continue
    
    a,b = AB[now]
    uf.union(a,b)
    ans[now] = uf.score

    for nex in e[now]:
        if p == nex:
            continue
        q.append((~nex,now))
        q.append((nex,now))

print(*ans[1:])
