from collections import deque

n = int(input())
e = [[] for i in range(n)]
mod = 10**9+7
for i in range(n-1):
    u,v,w = map(int,input().split())
    u -= 1
    v -= 1
    e[u].append((v,w))
    e[v].append((u,w))

q = deque([[0,0]])
vis = [-1]*n
vis[0] = 0
while q:
    now,c = q.popleft()
    for nex,w in e[now]:
        if vis[nex] != -1:
            continue
        q.append([nex,c^w])
        vis[nex] = c^w
ans = 0
for i in range(60):
    c = 0
    for j in range(n):
        if vis[j] >> i & 1:
            c += 1
    ans += c*(n-c)*1<<i
    ans %= mod
print(ans)