from heapq import heappop, heappush

class MinCostFlow:
    inf = 10**18

    class E:
        def __init__(self,to,cap,cost,nx):
            self.to = to
            self.cap = cap
            self.cost = cost
            self.nx = nx
            self.rev = None

    def __init__(self, n):
        self.n = n
        self.head = [None]*n
        self.h = [0]*n
        self.d = [0]*n
        self.pre = [None]*n

    def add_edge(self, fr, to, cap, cost):
        head = self.head
        head[fr] = self.E(to,cap,cost,head[fr])
        head[to] = self.E(fr, 0, -cost, head[to])
        head[fr].rev = head[to]
        head[to].rev = head[fr]

    def go(self, s, t, f):
        inf = self.inf
        n = self.n
        head = self.head
        h = self.h
        d = self.d
        pre = self.pre
        pq = [(0,s)]

        d[0] = 0
        d[1:] = [inf]*(n-1)
        while pq:
            a,v = heappop(pq)
            if d[v] < a:
                continue
            if v == t:
                break
            e = head[v]
            while e is not None:
                if e.cap > 0:
                    w = d[v]+e.cost+h[v] - h[e.to]
                    if w < d[e.to]:
                        d[e.to] = w
                        heappush(pq,(w,e.to))
                        pre[e.to] = e
                e = e.nx

        if d[t] == inf:
            return 0,0
        
        for i in range(n):
            h[i] = min(h[i]+min(d[i],d[t]), inf)

        a = f
        v = t
        while v != s:
            a = min(a, pre[v].cap)
            v = pre[v].rev.to

        v = t
        while v != s:
            x = pre[v]
            y = x.rev
            x.cap -= a
            y.cap += a
            v = y.to

        return a,h[t]

    def calc(self, s, t, f=None):
        if f is None:
            f = self.inf
        amount = 0
        cost = 0
        while f > 0:
            a,c = self.go(s,t,f)
            if a == 0:
                break
            amount += a
            f -= a
            cost += a*c
        return amount, cost

n,m = map(int,input().split())
e = [list(input()) for i in range(n)]
idx = [[-1]*m for _ in range(n)]
s = 0
ps = []

for i in range(n):
    for j in range(m):
        if e[i][j] == "o":
            ps.append((i,j))
        if e[i][j] != "#":
            idx[i][j] = s
            s += 1

ans = 0
mcf = MinCostFlow(1+s+1)
for i,j in ps:
    ans += n-i+m-j
    mcf.add_edge(0,1+idx[i][j],1,0)

for i in range(n):
    for j in range(m):
        if idx[i][j] != -1:
            mcf.add_edge(1+idx[i][j],1+s,1,n-i+m-j)
            if i+1 < n and idx[i+1][j] != -1:
                mcf.add_edge(1+idx[i][j],1+idx[i+1][j],mcf.inf,0)
            if j+1 < m and idx[i][j+1] != -1:
                mcf.add_edge(1+idx[i][j],1+idx[i][j+1],mcf.inf,0)

f,cost = mcf.calc(0,1+s)
print(ans-cost)