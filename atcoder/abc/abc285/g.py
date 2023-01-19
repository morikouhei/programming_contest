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
C = [input() for i in range(h)]

s = h*w
t = s+1
S = t+1
T = S+1
mf = MaxFlow(T+1)

def id(i,j):
    return i*w+j

left2 = 0
right2 = 0
for i in range(h):
    for j in range(w):
        c = C[i][j]
        if c == "1":
            continue

        sid = id(i,j)

        if (i+j)%2:
            if c == "2":
                left2 += 1
                mf.add_edge(S,sid,1)
            else:
                mf.add_edge(s,sid,1)

            for (dx,dy) in ((0,1),(0,-1),(1,0),(-1,0)):
                nx = i+dx
                ny = j+dy
                if 0 <= nx < h and 0 <= ny < w and C[nx][ny] != "1":
                    nid = id(nx,ny)
                    mf.add_edge(sid,nid,1)
        else:
            if c == "2":
                right2 += 1
                mf.add_edge(sid,T,1)
            else:
                mf.add_edge(sid,t,1)

mf.add_edge(s,T,left2)
mf.add_edge(S,t,right2)

ST = mf.flow(S,T)
sT = mf.flow(s,T)
St = mf.flow(S,t)

num2 = left2+right2
if ST + St == num2 and ST + sT == num2:
    print("Yes")
else:
    print("No")