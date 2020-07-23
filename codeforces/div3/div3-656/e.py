from collections import deque

def topo(g):
    par = [0]*(n+1)
    for now in g:
        for nex in now:
            par[nex] += 1

    q = deque([])
    order = []
    for i in range(1,n+1):
        if par[i] == 0:
            q.append(i)
    while q:
        v = q.popleft()
        order.append(v)
        for nex in g[v]:
            par[nex] -= 1
            if par[nex] == 0:
                q.append(nex)
    return order

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    e = [[] for i in range(n+1)]
    l = []
    for i in range(m):
        a,x,y = map(int,input().split())
        if a == 1:
            e[x].append(y)
        l.append([x,y])

    order = topo(e)
    if len(order) < n:
        print("NO")
    else:
        print("YES")
        ind = [-1]*(n+1)
        for i in range(len(order)):
            ind[order[i]] = i
        for i,j in l:
            if ind[i] > ind[j]:
                i,j = j,i
            print(i,j)
