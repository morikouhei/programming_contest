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


h,w = map(int,input().split())
S = [input() for i in range(h)]

hid = [[-1]*w for i in range(h)]
wid = [[-1]*w for i in range(h)]

num = 0
for i in range(h):
    for j in range(w):
        if S[i][j] == ".":
            hid[i][j] = num
        else:
            num += 1
    num += 1

hsize = num
for i in range(w):
    for j in range(h):
        if S[j][i] == ".":
            wid[j][i] = num
        else:
            num += 1
    num += 1

wsize = num-hsize

s = num
t = s+1

mf = MaxFlow(t+1)
for i in range(hsize):
    mf.add_edge(s,i,1)
for i in range(hsize,hsize+wsize):
    mf.add_edge(i,t,1)

inf = 10**10
for i in range(h):
    for j in range(w):
        if hid[i][j] == -1 or wid[i][j] == -1:
            continue    
        mf.add_edge(hid[i][j],wid[i][j],inf)

ans = mf.flow(s,t)
print(ans)