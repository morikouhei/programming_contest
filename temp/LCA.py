## library of LCA by class
## index start from 1

import sys
sys.setrecursionlimit(10**5+5)
from collections import deque

class LCA:
    def __init__(self,n):
        self.size = n+1
        self.bitlen = n.bit_length()
        self.ancestor = [[0]*self.size for i in range(self.bitlen)]
        self.depth = [-1]*self.size
        self.dis = [-1]*self.size
        self.depth[1] = 0
        self.dis[1] = 0

    ## using [log_n][n] [n][log_n]
    ## [log_n][n] is tend to faster than [n][log_n]
    ## get parent by bfs is probably faster than dfs
    def make(self,root):
        q = deque([root])
        while q:
            now = q.popleft()
            for nex,c,w in e[now]:
                if self.depth[nex]>= 0:
                    continue
                self.depth[nex] = self.depth[now]+1
                self.dis[nex] = self.dis[now]+w
                self.ancestor[0][nex] = now
                q.append(nex)
        for i in range(1,self.bitlen):
            for j in range(self.size):
                if self.ancestor[i-1][j] > 0:
                    self.ancestor[i][j] = self.ancestor[i-1][self.ancestor[i-1][j]]
    
    def lca(self,x,y):
        dx = self.depth[x]
        dy = self.depth[y]
        if dx < dy:
            x,y = y,x
            dx,dy = dy,dx
        dif = dx-dy
        while dif:
            s = dif & (-dif)
            x = self.ancestor[s.bit_length()-1][x]
            dif -= s
        while x != y:
            j = 0
            while self.ancestor[j][x] != self.ancestor[j][y]:
                j += 1
            if j == 0:
                return self.ancestor[0][x]
            x = self.ancestor[j-1][x]
            y = self.ancestor[j-1][y]
        return x

n,q = map(int,input().split())
e = [[] for i in range(n+1)]
for i in range(n-1):
    a,b,c,d = map(int,input().split())
    e[a].append((b,c,d))
    e[b].append((a,c,d))
    
lca = LCA(n)
lca.make(1)
