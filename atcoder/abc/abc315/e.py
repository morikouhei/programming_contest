
n = int(input())
e = [[] for i in range(n)]
se = [[] for i in range(n)]
edge = [0]*n
for i in range(n):
    c,*P = map(int,input().split())
    for p in P:
        e[i].append(p-1)
        se[p-1].append(i)
        edge[i] += 1


vis = [0]*n
vis[0] = 1

q = [0]
while q:
    now = q.pop()
    for nex in e[now]:
        if vis[nex]:
            continue
        vis[nex] = 1
        q.append(nex)


q = []
for i in range(n):
    if vis[i] and edge[i] == 0:
        q.append(i)

ans = []
while q:
    now = q.pop()
    ans.append(now+1)

    for nex in se[now]:
        if vis[nex] == 0:
            continue

        edge[nex] -= 1
        if edge[nex] == 0:
            q.append(nex)

ans.pop()
print(*ans)
