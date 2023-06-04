import sys
input = sys.stdin.readline
from heapq import heappush,heappop

class SCC:

    def __init__(self,n):
        self.n = n
        self.edges = []

    def csr(self):
        self.start = [0]*(self.n+1)
        self.elist = [0]*len(self.edges)
        for e in self.edges:
            self.start[e[0]+1] += 1
        for i in range(1,self.n+1):
            self.start[i] += self.start[i-1]
        counter = self.start[:]
        for e in self.edges:
            self.elist[counter[e[0]]] = e[1]
            counter[e[0]] += 1

    def add_edge(self,u,v):
        self.edges.append((u,v))

    def scc_ids(self):
        self.csr()
        n = self.n
        now_ord = group_num = 0
        visited = []
        low = [0]*n
        order = [-1]*n
        ids = [0]*n
        parent = [-1]*n
        stack = []
        for i in range(n):
            if order[i] == -1:
                stack.append(i)
                stack.append(i)
                while stack:
                    v = stack.pop()
                    if order[v] == -1:
                        low[v] = order[v] = now_ord
                        now_ord += 1
                        visited.append(v)
                        for i in range(self.start[v],self.start[v+1]):
                            to = self.elist[i]
                            if order[to] == -1:
                                stack.append(to)
                                stack.append(to)
                                parent[to] = v
                            else:
                                low[v] = min(low[v],order[to])
                    else:
                        if low[v] == order[v]:
                            while True:
                                u = visited.pop()
                                order[u] = n
                                ids[u] = group_num
                                if u == v:
                                    break
                            group_num += 1
                        if parent[v] != -1:
                            low[parent[v]] = min(low[parent[v]],low[v])
        for i,x in enumerate(ids):
            ids[i] = group_num-1-x

        return group_num,ids


    def scc(self):
        group_num,ids = self.scc_ids()
        groups = [[] for i in range(group_num)]
        for i,x in enumerate(ids):
            groups[x].append(i)

        return groups


n,m = map(int,input().split())
scc = SCC(n)
e = [[] for i in range(n)]
for _ in range(m):
    s,t = [int(x)-1 for x in input().split()]
    scc.add_edge(s,t)
    e[s].append(t)

topo = scc.scc()
for t in topo:
    if len(t) != 1:
        print("No")
        exit()

topo = [t[0] for t in topo]
LR = [list(map(int,input().split())) for i in range(n)]
for now in topo:
    for nex in e[now]:
        LR[nex][0] = max(LR[nex][0],LR[now][0]+1)

for now in topo[::-1]:
    for nex in e[now]:
        LR[now][1] = min(LR[nex][1]-1,LR[now][1])

event = [[] for i in range(n+1)]
for i,(l,r) in enumerate(LR):
    if l > r:
        print("No")
        exit()

    event[l].append([r,i])

ans = [-1]*n
h = []
for i in range(1,n+1):
    for r,ind in event[i]:
        heappush(h,[r,ind])
    
    if h == []:
        print("No")
        exit()
    r,ind = heappop(h)
    if r < i:
        print("No")
        exit()
    ans[ind] = i

print("Yes")
print(*ans)

