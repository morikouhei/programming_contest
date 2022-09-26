import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
e = [[] for i in range(n)]
for _ in range(n-1):
    a,b = [int(x)-1 for x in input().split()]
    e[a].append(b)
    e[b].append(a)

q = int(input())
query = [[] for i in range(n)]
for _ in range(q):
    u,k = map(int,input().split())
    query[u-1].append((k,_))

ans = [-1]*q


def bfs(x):
    dist = [n]*n
    dist[x] = 0
    q = deque([x])
    while q:
        now = q.popleft()
        for nex in e[now]:
            if dist[nex] > dist[now]+1:
                dist[nex] = dist[now]+1
                q.append(nex)
    return dist

d1 = bfs(0)
lind = d1.index(max(d1))
d2 = bfs(lind)
rind = d2.index(max(d2))
def euler_tour(x):
    l = [-1]*n
    q = [~x,x]
    par = [-1]*n

    while q:
        now = q.pop()

        if now < 0:
            l.pop()
            continue
        for k,ind in query[now]:
            if l[-k] != -1:
                ans[ind] = l[-k]+1
        l.append(now)

        for nex in e[now]:
            if par[now] == nex:
                continue
            par[nex] = now
            q.append(~nex)
            q.append(nex)

euler_tour(lind)
euler_tour(rind)

for i in ans:
    print(i)