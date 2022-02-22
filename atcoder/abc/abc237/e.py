from heapq import heappush, heappop

n,m = map(int,input().split())
H = list(map(int,input().split()))
inf = 10**15
e = [[] for i in range(n)]
for i in range(m):
    u,v = [int(x)-1 for x in input().split()]
    hu,hv = H[u],H[v]
    if hu >= hv:
        e[u].append((v,0))
        e[v].append((u,hu-hv))
    else:
        e[u].append((v,hv-hu))
        e[v].append((u,0))

mod = 1<<32
dis = [inf]*n
dis[0] = 0
h = [0]
ans = 0
while h:
    d,now = divmod(heappop(h),mod)
    if dis[now] != d:
        continue

    ans = max(ans,H[0]-H[now]-d)
    for nex,cost in e[now]:
        if d+cost < dis[nex]:
            dis[nex] = d+cost
            heappush(h,nex + ((d+cost)<<32))

print(ans)