from collections import deque
import sys
sys.setrecursionlimit(10**6)
class MaxFlow:
    inf = 10**18

    class E:
        def __init__(self,to,cap):
            self.to = to
            self.cap = cap
            self.rev = None

    def __init__(self,n):
        self.n = n
        self.graph = [[] for _ in range(n)]

    def add_edge(self, fr, to, cap):
        graph = self.graph
        edge = self.E(to,cap)
        edge2 = self.E(fr,0)
        edge.rev = edge2
        edge2.rev = edge
        graph[fr].append(edge)
        graph[to].append(edge2)

    def bfs(self, s, t):
        level = self.level = [self.n]*self.n
        q = deque([s])
        level[s] = 0
        while q:
            now = q.popleft()
            lw = level[now]+1
            for e in self.graph[now]:
                if e.cap and level[e.to]> lw:
                    level[e.to] = lw
                    if e.to == t:
                        return True
                    q.append(e.to)
        return False

    def dfs(self, s, t, up):
        graph = self.graph
        it = self.it
        level = self.level

        st = deque([t])
        while st:
            v = st[-1]
            if v == s:
                st.pop()
                flow = up
                for w in st:
                    e = graph[w][it[w]].rev
                    flow = min(flow, e.cap)
                for w in st:
                    e = graph[w][it[w]]
                    e.cap += flow
                    e.rev.cap -= flow
                return flow
            lv = level[v]-1
            while it[v] < len(graph[v]):
                e = graph[v][it[v]]
                re = e.rev
                if re.cap == 0 or lv != level[e.to]:
                    it[v] += 1
                    continue
                st.append(e.to)
                break
            if it[v] == len(graph[v]):
                st.pop()
                level[v] = self.n

        return 0

    def flow(self,s,t,flow_limit=inf):
        flow = 0
        while flow < flow_limit and self.bfs(s,t):
            self.it = [0]*self.n
            while flow < flow_limit:
                f = self.dfs(s,t,flow_limit-flow)
                if f == 0:
                    break
                flow += f
        return flow

n = int(input())
C = [list(input()) for i in range(n)]


s = n*n
t = s+1
f = MaxFlow(t+1)
M = 10**10

for i in range(n):
    for j in range(n):
        if (i+j)%2 or C[i][j] == "?":
            continue
        if C[i][j] == "W":
            C[i][j] = "B"
        else:
            C[i][j] = "W"
for i in range(n):
    for j in range(n):
        a = i*n+j
        if C[i][j] == "B":
            f.add_edge(s,a,M)
        if C[i][j] == "W":
            f.add_edge(a,t,M)
        if i != 0:
            f.add_edge(a-n,a,1)
            f.add_edge(a,a-n,1)
        if j != 0:
            f.add_edge(a-1,a,1)
            f.add_edge(a,a-1,1)

ans = 2*n*(n-1)-f.flow(s,t)
print(ans)

