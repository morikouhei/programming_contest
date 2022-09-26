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


n = int(input())
AB = [list(map(int,input().split())) for i in range(n)]
M = 2*10**7+5

def is_prime(x):
    for i in range(2,int(x**0.5)+1):
        if x%i == 0:
            return 0
    return 1

s = n+1
t = s+1
edges = []
for i in range(n):
    ok = 0
    a,b = AB[i]
    if a%2 and a != 1:
        edges.append((s,i,b))
    if a%2 == 0:
        edges.append((i,t,b))
        continue

    for j in range(n):
        if i == j:
            continue

        na,nb = AB[j]
        if is_prime(a+na):
            edges.append((i,j,max(b,nb)))

def cal_flow(edges):
    mf = MaxFlow(t+1)
    for a,b,c in edges:
        mf.add_edge(a,b,c)

    return mf.flow(s,t)

f0 = cal_flow(edges)
ind = -1
for i in range(n):
    a,b = AB[i]
    if a == 1:
        edges.append((s,i,b))
        ind = i

f1 = cal_flow(edges)

ans = f1
if ind != -1:
    ans += (AB[ind][1]-(f1-f0))//2
print(ans)