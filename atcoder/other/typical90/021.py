import sys
input = sys.stdin.readline
sys.setrecursionlimit(3*10**5)

class SCC:

    def __init__(self, n):
        self.n = n
        self.graph = [[] for i in range(n)]
        self.graph_rev = [[] for i in range(n)]
        self.used = [False]*n

    def add_edge(self, fr, to):
        if fr == to:
            return
        self.graph[fr].append(to)
        self.graph_rev[to].append(fr)

    def dfs(self, node, graph):
        self.used[node] = True
        for nex in graph[node]:
            if self.used[nex]:
                continue
            self.dfs(nex,graph)
        self.order.append(node)

    def first_dfs(self):
        self.used = [False]*self.n
        self.order = []
        for i in range(self.n):
            if self.used[i]:
                continue
            self.dfs(i,self.graph)
    
    def second_dfs(self):
        self.used = [False]*self.n
        self.ans = []
        for node in reversed(self.order):
            if self.used[node]:
                continue
            self.used[node] = True
            self.order = []
            self.dfs(node, self.graph_rev)
            self.ans.append(self.order)

    def scc(self):
        self.first_dfs()
        self.second_dfs()
        return self.ans

n,m = map(int,input().split())
scc = SCC(n)
for i in range(m):
    a,b = map(int,input().split())
    scc.add_edge(a-1, b-1)

order = scc.scc()
ans = 0
for i in order:
    ans += len(i)*(len(i)-1)//2
print(ans)