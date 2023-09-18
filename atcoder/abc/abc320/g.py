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

n,m = map(int,input().split())
S = [list(map(int,input())) for i in range(n)]

nums = [[] for i in range(10)]
for i,s in enumerate(S):

    num = [[] for j in range(10)]

    for j,sj in enumerate(s):
        num[sj].append(j)
    
    for j in range(10):
        if num[j] == []:
            continue

        le = len(num[j])
        size = 0
        for k in range(n):
            if k and k%le == 0:
                size += 1
            
            nums[j].append([size*m+num[j][k%le],i])


ans = 10**20
for i in range(10):
    if len(nums[i]) != n*n:
        continue
    nums[i].sort()
    s = n+n**2+1
    t = s+1
    mf = MaxFlow(t+1)
    for j in range(n):
        mf.add_edge(j,t,1)
    for j in range(n**2):
        mf.add_edge(s,n+j,1)
    
    last = -1
    id = -1
    f = n
    for ti,ind in nums[i]:

        if last < ti:
            last = ti
            id += 1
        mf.add_edge(n+id,ind,1)
        f -= mf.flow(s,t,n)
        if f == 0:
            ans = min(ans,last)
            break
    
if ans == 10**20:
    ans = -1
print(ans)

