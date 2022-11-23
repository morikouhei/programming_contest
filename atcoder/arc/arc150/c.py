from heapq import heappush,heappop
n,m,k = map(int,input().split())
e = [[] for i in range(n)]
for _ in range(m):
    u,v = [int(x)-1 for x in input().split()]
    e[u].append(v)
    e[v].append(u)

A = [int(x)-1 for x in input().split()]
B = [int(x)-1 for x in input().split()]

dist = [k+1]*n

if A[0] == B[0]:
    d = 1
else:
    d = 0
dist[0] = d
h = []
heappush(h,[d,0])
while h:
    d,now = heappop(h)
    if dist[now] != d:
        continue
    for nex in e[now]:
        if d < k and A[nex] == B[d]:
            nd = d+1
        else:
            nd = d
        if dist[nex] > nd:
            dist[nex] = nd
            heappush(h,[nd,nex])

if dist[-1] == k:
    print("Yes")
else:
    print("No")