from collections import deque

n,m = map(int,input().split())
e = [[] for i in range(n)]
for i in range(m):
    s,t = [int(x)-1 for x in input().split()]
    e[s].append((t,i))

par = [0]*n

def bfs(ban=-1):
    dis = [n]*n
    dis[0] = 0
    q = deque([0])
    while q:
        now = q.popleft()
        for nex,ind in e[now]:
            if dis[nex] == n and ind != ban:
                dis[nex] = dis[now]+1
                q.append(nex)
                par[nex] = now
    return dis

dis = bfs()
if dis[-1] == n:
    for i in range(m):
        print(-1)
    exit()
ans = dis[-1]
use = [0]*m
now = n-1
while now != 0:
    p = par[now]
    for nex,ind in e[p]:
        if nex == now:
            use[ind] = 1
    now = p
for i in range(m):
    if use[i]:
        dis = bfs(i)
        if dis[-1] == n:
            dis[-1] = -1
        print(dis[-1])
    else:
        print(ans)
