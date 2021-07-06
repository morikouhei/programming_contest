n,m = map(int,input().split())
e = [[] for i in range(n)]
deg = [0]*n
for i in range(m):
    a,b = [int(x)-1 for x in input().split()]
    e[a].append(b)
    e[b].append(a)
    deg[a] += 1
    deg[b] += 1

col = [1]*n
last = [-1]*n
lim = int((2*m)**0.5)
large = []
for i in range(n):
    if deg[i] > lim:
        large.append(i)
lla = len(large)
link = [[0]*lla for i in range(n)]
for i in range(lla):
    for j in e[large[i]]:
        link[j][i] = 1
    link[large[i]][i] = 1


q = int(input())
Q = [list(map(int,input().split())) for i in range(q)]
for i,(x,y) in enumerate(Q):
    x -= 1
    m = last[x]
    ind = x
    if deg[x] > lim:
        for nex in range(lla):
            if link[x][nex]:
                if last[large[nex]] > m:
                    m = last[large[nex]]
                    ind = large[nex]
        print(col[ind])
    else:
    
        for nex in e[x]:
            if deg[nex] <= lim:
                continue
            if last[nex] > m:
                m = last[nex]
                ind = nex
        print(col[ind])
        for nex in e[x]:
            col[nex] = y
    col[x] = y
    last[x] = i