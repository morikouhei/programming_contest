n,m = map(int,input().split())

e = [[] for i in range(n)]
P = list(map(int,input().split()))

for i,p in enumerate(P,1):
    p -= 1
    e[i].append(p)
    e[p].append(i)



size = [0]*n

for _ in range(m):
    x,y = map(int,input().split())
    x -= 1
    size[x] = max(size[x],y+1)

vis = [0]*n
vis[0] = 1
q = [0]
while q:
    now = q.pop()
    si = size[now]-1

    for nex in e[now]:
        if vis[nex]:
            continue
        vis[nex] = 1
        size[nex] = max(size[nex],si)
        q.append(nex)

ans = 0
for i in size:
    if i:
        ans += 1
print(ans)