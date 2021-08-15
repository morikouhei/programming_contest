from collections import deque
import sys
input = sys.stdin.buffer.readline

n,m = map(int,input().split())
e = [[] for i in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    e[a].append(b)
    e[b].append(a)

dis = [n]*n
par = [-1]*n
q = deque([0])
dis[0] = 0
while q:
    now = q.popleft()
    for nex in e[now]:
        if dis[nex] > dis[now]+1:
            q.append(nex)
            dis[nex] = dis[now]+1
            par[nex] = now

def solve():
    Q = [int(x)-1 for x in input().split()]
    dic = {}
    id = set()
    for i in Q[1:]:
        p = par[i]
        if p < 1:
            continue
        if dis[p] in dic and dic[dis[p]] != p:
            return 0
        dic[dis[p]] = p
        id.add(p)
    if len(id) == 0:
        return 1
    dep = 0
    ind = -1
    for i in id:
        if dep < dis[i]:
            dep = dis[i]
            ind = i
    
    for i in range(dep):
        if ind in id:
            id.remove(ind)
        ind = par[ind]
    return len(id) == 0
    
    
for _ in range(m):
    print("YES" if solve() else "NO")