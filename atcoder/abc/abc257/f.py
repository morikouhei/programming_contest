from collections import deque
n,m = map(int,input().split())

e = [[] for i in range(n)]
nd = [0]*n
for _ in range(m):
    u,v = [int(x)-1 for x in input().split()]
    if u == -1:
        nd[v] = 1
    else:
        e[u].append(v)
        e[v].append(u)


def bfs(x):
    dis = [n]*n
    dis[x] = 0
    q = deque([x])
    while q:
        now = q.popleft()
        for nex in e[now]:
            if dis[nex] > dis[now]+1:
                dis[nex] = dis[now]+1
                q.append(nex)
    return dis
dis1 = bfs(0)
disn = bfs(n-1)

d1 = 2*n
dn = 2*n
for i in range(n):
    if nd[i] == 0:
        continue
    d1 = min(d1,dis1[i])
    dn = min(dn,disn[i])

base = dis1[-1]
for i in range(n):
    ans = base
    c1 = dis1[i]+disn[i]
    ans = min(ans,c1)
    c1 = d1+1+disn[i]
    ans = min(ans,c1)
    c1 = dis1[i]+1+dn
    ans = min(ans,c1)
    c1 = d1+1+dn+1
    ans = min(ans,c1)
    if ans == n:
        ans = -1
    print(ans)
