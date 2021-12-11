from collections import deque
n = int(input())
e = [[] for i in range(n)]
T = []
for i in range(n):
    l = list(map(int,input().split()))
    for j in l[2:]:
        e[i].append(j-1)
    T.append(l[0])

vis = [0]*n
vis[-1] = 1
q = deque([n-1])
while q:
    now = q.popleft()
    for nex in e[now]:
        if vis[nex]:
            continue
        vis[nex] = 1
        q.append(nex)
ans = 0
for i in range(n):
    if vis[i]:
        ans += T[i]
print(ans)
