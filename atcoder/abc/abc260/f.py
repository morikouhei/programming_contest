s,t,m = map(int,input().split())
e = [[] for i in range(s+t)]
for _ in range(m):
    u,v = map(int,input().split())
    u,v = u-1,v-1
    e[u].append(v)
    e[v].append(u)


vis = [-1]*(s+t)
id = [-1]*(s+t)
time = 0
for now in range(s,s+t):
    vis[now] = time
    q = []
    for nex in e[now]:
        q.append(nex)

    for d in q:
        for nex in e[d]:
            if nex == now:
                continue
            if vis[nex] == time:
                print(now+1,nex+1,d+1,id[nex]+1)
                exit()
            vis[nex] = time
            id[nex] = d


    time += 1

print(-1)