from collections import deque
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

    def min_cut(self,s):
        visited = [0]*self.n
        q = deque([s])
        while q:
            v = q.pop()
            visited[v] = 1
            for e in self.graph[v]:
                if e.cap and not visited[e.to]:
                    q.append(e.to)
        return visited



n,m = map(int,input().split())
res = [[-1]*n for i in range(n)]
for i in range(m):
    w,l = [int(x)-1 for x in input().split()]
    res[w][l] = 1
    res[l][w] = 0

for i in range(n):
    res[i][i] = 0
ans = []


for i in range(n):

    wins = []
    for j in range(n):
        num = res[j].count(1)
        if j == i:
            num += res[j].count(-1)
        wins.append(num)
    w = wins[i]
    for j in range(n):
        if j != i and wins[j] >= w:
            w = -1

    if w == -1:
        continue
    s = n**2+n
    t = s+1
    mf = MaxFlow(t+1)
    match = 0
    for j in range(n):
        for k in range(j):
            if j == i or k == i:
                continue
            
            if res[j][k] == -1:
                mid = n*j+k
                match += 1
                mf.add_edge(s,mid,1)
                mf.add_edge(mid,n**2+j,1)
                mf.add_edge(mid,n**2+k,1)
    for j in range(n):
        if i == j:
            continue
        mf.add_edge(n**2+j,t,w-wins[j]-1)
    if mf.flow(s,t) == match:
        ans.append(i+1)

print(*ans)