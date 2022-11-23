import sys
input = sys.stdin.readline
from collections import defaultdict

h,w = map(int,input().split())
A = [list(map(int,input().split())) for i in range(h)]

sH = []
mod = 1<<32
for a in A:
    mi = 10**10
    ma = -1
    for i in a:
        if i == 0:
            continue
        ma = max(ma,i)
        mi = min(mi,i)
    if ma == -1:
        continue
    sH.append((mi<<32)+ma)

sH.sort()
for a,sa in zip(sH,sH[1:]):
    if a%mod > sa>>32:
        print("No")
        exit()

edges = [[] for i in range(w)]
size = w
for a in A:
    W = defaultdict(list)
    for i,x in enumerate(a):
        if x:
            W[x].append(i)

    keys = sorted(W.keys())
    for x,nx in zip(keys,keys[1:]):
        edges.append([])
        for t in W[x]:
            edges[size].append(t)
        for t in W[nx]:
            edges[t].append(size)
        size += 1    

def topological_sort(edges):
    n = len(edges)

    count = [0]*n
    for u in range(n):
        for v in edges[u]:
            count[v] += 1

    q = []
    for i in range(n):
        if count[i] == 0:
            q.append(i)

    while q:
        now = q.pop()
        for nex in edges[now]:
            count[nex] -= 1
            if count[nex] == 0:
                q.append(nex)
    return sum(count) == 0
    


if topological_sort(edges):
    print("Yes")
else:
    print("No")
