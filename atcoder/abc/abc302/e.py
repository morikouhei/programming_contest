n,q = map(int,input().split())
e = [[] for i in range(n)]

edges = [0]*n

ans = n
used = [0]*q
for ind in range(q):
    l = list(map(int,input().split()))
    if l[0] == 1:

        u,v = l[1:]
        u,v = u-1,v-1
        if edges[u] == 0:
            ans -= 1
        if edges[v] == 0:
            ans -= 1

        edges[u] += 1
        edges[v] += 1
        e[u].append([v,ind])
        e[v].append([u,ind])

    else:
        v = l[1]-1
        for u,id in e[v]:
            if used[id] == 0:
                used[id] = 1
                edges[u] -= 1
                if edges[u] == 0:
                    ans += 1
        
        if edges[v]:
            ans += 1
        edges[v] = 0
        e[v] = []
    print(ans)
