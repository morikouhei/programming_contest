from collections import deque

n,m = map(int,input().split())

AB = [[int(x)-1 for x in input().split()] for i in range(m)]
C = list(map(int,input().split()))

vis = [0]*n

dist = [n+5]*n

e = [[] for i in range(n)]
se = [[] for i in range(n)]
for a,b in AB:
    if C[a] != C[b]:
        e[a].append(b)
        e[b].append(a)
    else:
        se[a].append(b)
        se[b].append(a)


for i in range(n):
    if vis[i]:
        continue

    q = deque([i])

    visit = set()
    vis[i] = 1

    while q:
        now = q.popleft()
        visit.add(now)

        for nex in e[now]:
            if vis[nex]:
                continue
            vis[nex] = 1
            dist[nex] = dist[now]+1
            q.append(nex)

    
    for now in visit:

        for nex in se[now]:
            if nex in visit and (dist[now]+dist[nex])%2 == 0:
                print("Yes")
                exit()
print("No")