n,x,y = map(int,input().split())
e = [[] for i in range(n+1)]
for _ in range(n-1):
    u,v = map(int,input().split())
    e[u].append(v)
    e[v].append(u)


par = [-1]*(n+1)
vis = [0]*(n+1)
vis[x] = 1

q = [x]
while q:
    now = q.pop()
    for nex in e[now]:
        if vis[nex]:
            continue
        vis[nex] = 1
        par[nex] = now
        q.append(nex)


ans = []
now = y
while par[now] != -1:
    ans.append(now)
    now = par[now]
ans.append(x)

print(*ans[::-1])