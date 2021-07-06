# https://atcoder.jp/contests/practice2/submissions/16598132
# 上記のリンクの提出をいじらせてもらってます。
# https://atcoder.jp/contests/practice2/submissions/16784996 を使用
class mf_graph:

    def __init__(self, N):
        self.N = N
        self.graph = [[] for _ in range(N)]
        self.capacities = [dict() for _ in range(N)]
        self.dir = [dict() for _ in range(N)]

    def add_edge(self, v, w, cap,dir):
        self.graph[v].append(w)
        self.graph[w].append(v)
        self.capacities[v][w] = cap
        self.capacities[w][v] = 0
        self.dir[v][w] = dir

    def bfs(self, s, t):
        self.level = [-1] * self.N
        q = [s]
        self.level[s] = 0
        while q:
            nq = []
            for v in q:
                for w, cap in self.capacities[v].items():
                    if cap and self.level[w] == -1:
                        self.level[w] = self.level[v] + 1
                        if w == t:
                            return True
                        nq.append(w)
            q = nq
        return False

    def dfs(self, s, t, up):
        st = [t]
        while st:
            v = st[-1]
            if v == s:
                flow = up
                for i in range(len(st) - 2):
                    if flow > self.capacities[st[i + 1]][st[i]]:
                        flow = self.capacities[st[i+1]][st[i]]
                for i in range(len(st) - 1):
                    self.capacities[st[i]][st[i+1]] += flow
                    self.capacities[st[i+1]][st[i]] -= flow
                return flow
            while self.it[v] < len(self.graph[v]):
                w = self.graph[v][self.it[v]]
                cap = self.capacities[w][v]
                if cap and self.level[w] != -1:
                    if self.level[v] > self.level[w]:
                        st.append(w)
                        break
                self.it[v] += 1
            else:
                st.pop()
                self.level[v] = self.N
        return 0

    def flow(self, s, t, flow_limit=18446744073709551615):
        flow = 0
        while flow < flow_limit and self.bfs(s, t):
            self.it = [0]*self.N
            while flow < flow_limit:
                f = self.dfs(s, t, flow_limit - flow)
                if not f:
                    break
                flow += f
        return flow

    def get_edge(self,n):
        ans = []
        for i in range(n):
            for nex in self.graph[i]:
                if self.capacities[i][nex]:
                    continue
                ans.append(self.dir[i][nex]+1)
                break
        return ans





n,T = map(int,input().split())
dx = [1,1,0,-1,-1,-1,0,1]
dy = [0,1,1,1,0,-1,-1,-1]
A = [tuple(map(int,input().split())) for i in range(n)]
B = [tuple(map(int,input().split())) for i in range(n)]
dic = {}
for i,(x,y) in enumerate(B,n):
    dic[(x,y)] = i
s = 2*n
t = s+1
flow = mf_graph(t+1)
for id,(x,y) in enumerate(A):
    flow.add_edge(s,id,1,0)
    flow.add_edge(id+n,t,1,0)
    for i in range(8):
        nx = x+dx[i]*T
        ny = y+dy[i]*T
        if (nx,ny) in dic:
            flow.add_edge(id,dic[(nx,ny)],1,i)
if flow.flow(s,t) != n:
    print("No")
    exit()
ans = flow.get_edge(n)
print("Yes")
print(*ans)