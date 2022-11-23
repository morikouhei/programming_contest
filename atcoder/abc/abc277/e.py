from collections import deque

n,m,k = map(int,input().split())
e = [[] for i in range(n)]
for _ in range(m):
    u,v,a = map(int,input().split())
    u,v = u-1,v-1
    e[u].append([v,a])
    e[v].append([u,a])
S = [0]*n
for s in list(map(int,input().split())):
    S[s-1] = 1
inf = 10**10
dist = [[inf,inf] for i in range(n)]
dist[0][0] = 0
q = deque()
q.append([0,0])
while q:
    now,m = q.popleft()

    for nex,t in e[now]:
        if m^t and dist[nex][m] > dist[now][m]+1:
            dist[nex][m] = dist[now][m]+1
            q.append([nex,m])

    if S[now] == 0:
        continue
    if dist[now][m^1] > dist[now][m]:
        dist[now][m^1] = dist[now][m]
        q.appendleft([now,m^1])
ans = min(dist[-1])
if ans == inf:
    ans = -1
print(ans)