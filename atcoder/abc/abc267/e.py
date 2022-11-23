from collections import deque
n,m = map(int,input().split())
A = list(map(int,input().split()))

e = [[] for i in range(n)]

base = [0]*n
for _ in range(m):
    u,v = map(int,input().split())
    u,v = u-1,v-1
    e[u].append(v)
    e[v].append(u)
    base[v] += A[u]
    base[u] += A[v]


cost = [0]*n
vis = [0]*n
def calc(x):

    q = deque([])
    for i in range(n):
        cost[i] = base[i]
        vis[i] = 0
        if cost[i] > x:
            continue
        q.append(i)
        vis[i] = 1

    while q:
        now = q.popleft()
        for nex in e[now]:
            cost[nex] -= A[now]
        for nex in e[now]:
            if vis[nex] or cost[nex] > x:
                continue
            q.append(nex)
            vis[nex] = 1
    if sum(vis) == n:
        return 1
    else:
        return 0


l = -1
r = 10**15
while r > l + 1:
    m = (r+l)//2
    if calc(m):
        r = m
    else:
        l = m
print(r)