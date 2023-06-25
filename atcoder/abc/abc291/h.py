import sys
sys.setrecursionlimit(3*10**5)
n = int(input())
e = [[] for i in range(n)]
deg = [0]*n
for _ in range(n-1):
    a,b = [int(x)-1 for x in input().split()]
    e[a].append(b)
    e[b].append(a)
    

P = [-1]*n
size = [0]*n
par = [-1]*n
used = [0]*n
def calcSize(x,p):
    size[x] = 1
    for nex in e[x]:
        if used[nex] or nex == p:
            continue
        calcSize(nex,x)
        size[x] += size[nex]


def dfs(x,p):
    calcSize(x,-1)

    tot = size[x]
    ok = 0
    pp = -1

    while ok == 0:
        ok = 1
        for nex in e[x]:
            if (used[nex] == 0 and nex != pp and 2*size[nex] > tot):
                pp = x
                x = nex
                ok = 0
                break
    par[x] = p
    used[x] = 1
    for nex in e[x]:
        if used[nex]:
            continue
        dfs(nex,x)

dfs(0,-1)
for i in range(n):
    if par[i] != -1:
        par[i] += 1
print(*par)