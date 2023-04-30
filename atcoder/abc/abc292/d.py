n,m = map(int,input().split())
e = [[] for i in range(n)]

for i in range(m):
    u,v = [int(x)-1 for x in input().split()]
    e[u].append(v)
    e[v].append(u)


vis = [0]*n

for i in range(n):
    if vis[i]:
        continue

    q = [i]
    size = 0
    vis[i] = 1
    count = 0
    while q:
        now = q.pop()
        size += 1
        count += len(e[now])
        for nex in e[now]:
            if vis[nex]:
                continue
            vis[nex] = 1
            q.append(nex)

    if size*2 != count:
        print("No")
        exit()
print("Yes")
            