import sys
input = sys.stdin.readline
from heapq import heappush, heappop

class mincostflow:

    class edge:
        def __init__(self, from_, to, cap, flow, cost):
            self.from_ = from_
            self.to = to
            self.cap = cap
            self.flow = flow
            self.cost = cost
    class _edge:
        def __init__(self, to, rev, cap, cost):
            self.to = to
            self.rev = rev
            self.cap = cap
            self.cost = cost

    def __init__(self, n):
        self.n = n
        self.pos = []
        self.g = [[] for i in range(n)]

    def add_edge(self, from_, to, cap, cost):
        m = len(self.pos)
        self.pos.append((from_, len(self.g[from_])))
        self.g[from_].append(self.__class__._edge(to, len(self.g[to]), cap, cost))
        self.g[to].append(self.__class__._edge(from_, len(self.g[from_])-1, 0, -cost))
        return m

    def get_edge(self, i):
        _e = self.g[self.pos[i][0]][self.pos[i][1]]
        _re = self.g[_e.to][_e.rev]
        return self.edge(self.pos[i][0], _e.to, _e.cap + _re.cap, _re.cap, _e.cost)

    def edges(self):
        result = []
        for i in range(len(self.pos)):
            result.append(self.get_edge(i))
        return result

    def slope(self, s, t, flow_limit=10**20, inf=10**20):
        dual = [0]*self.n
        dist = [inf]*self.n
        pv = [-1]*self.n
        pe = [-1]*self.n
        vis = [False]*self.n

        def _dual_ref():
            nonlocal dual, dist, pv, pe, vis
            dist = [inf]*self.n
            pv = [-1]*self.n
            pe = [-1]*self.n
            vis = [False]*self.n

            que = [(0,s)]
            dist[s] = 0
            while que:
                _,v = heappop(que)
                if vis[v]:
                    continue
                vis[v] = True

                if v == t:
                    break
                for i in range(len(self.g[v])):
                    e = self.g[v][i]
                    if vis[e.to] or e.cap == 0:
                        continue
                    cost = e.cost - dual[e.to] + dual[v]
                    if dist[e.to] > dist[v] + cost:
                        dist[e.to] = dist[v] + cost
                        pv[e.to] = v
                        pe[e.to] = i
                        heappush(que, (dist[e.to],e.to))
            if not vis[t]:
                return False

            for v in range(self.n):
                if not vis[v]:
                    continue
                dual[v] -= dist[t] - dist[v]
            return True
        
        flow = 0
        cost = 0
        prev_cost = -1

        result = [(flow, cost)]
        while flow < flow_limit:
            if not _dual_ref():
                break
            c = flow_limit - flow
            v = t
            while v != s:
                c = min(c, self.g[pv[v]][pe[v]].cap)
                v = pv[v]

            v = t
            while v != s:
                e = self.g[pv[v]][pe[v]]
                e.cap -= c
                self.g[v][e.rev].cap += c
                v = pv[v]
            
            d = -dual[s]
            flow += c
            cost += c * d
            if prev_cost == d:
                result.pop()
            result.append((flow, cost))
            prev_cost = cost
        return result

    def flow(self, s, t, flow_limit=10**20):
        return self.slope(s, t, flow_limit)[-1]
    

s = 2*155
t = s+1
g = mincostflow(t+1)
M = 10**9
n = int(input())
for i in range(150):
    g.add_edge(s,i,1,0)
    g.add_edge(i+150,t,1,0)
for _ in range(n):
    a,b,c = map(int,input().split())
    a,b = a-1,b-1
    g.add_edge(a,b+150,1,M-c)
 

f = g.slope(s,t,M)
ans = []
now = 0
last = 0
for i in range(1,len(f)):
    x,y = f[i]
    y = x*M-y
    dx = (y-last)//(x-now)
    if x == now+1:
        ans.append(y)
    else:

        for j in range(now,x):
            ans.append(last+dx*(j+1))
    
    now = x
    last = y
print(len(ans))
for i in ans:
    print(i)