n,m = map(int,input().split())
e = [[] for i in range(n)]
for i in range(m):
    u,v = [int(x)-1 for x in input().split()]
    e[u].append(v)


def bfs(x):

    vis = [0]*n

    vis[x] = 1
    q = [x]
    while q:
        now = q.pop()
        for nex in e[now]:
            if vis[nex]:
                continue
            vis[nex] = 1
            q.append(nex)

    return sum(vis)-1-len(e[x])

ans = 0
for i in range(n):
    ans += bfs(i)
print(ans)