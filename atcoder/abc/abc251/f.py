from collections import deque

n,m = map(int,input().split())
edges = [[int(x)-1 for x in input().split()] for i in range(m)]
e = [[] for i in range(n)]
for i,(u,v) in enumerate(edges):
    e[u].append([v,i])
    e[v].append([u,i])

T2 = []

used = [0]*n
used[0] = 1
q = deque([0])
while q:
    now = q.popleft()
    for nex,ind in e[now]:
        if used[nex]:
            continue

        T2.append([now+1,nex+1])

        used[nex] = 1
        q.append(nex)

T1 = []

par = [-1]*n
vis = [0]*n

q = deque([0])
while q:
    now = q.pop()
    if vis[now]:
        continue
    vis[now] = 1
    
    for nex,ind in e[now]:
        if vis[nex]:
            continue

        par[nex] = now
        q.append(nex)

for i in range(1,n):
    T1.append([i+1,par[i]+1])
for i in T1:
    print(*i)
for i in T2:
    print(*i)