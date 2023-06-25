import sys
input = sys.stdin.readline
from heapq import heappush,heappop
n,m,k = map(int,input().split())
e = [[] for i in range(n)]
for _ in range(m):
    a,b = [int(x)-1 for x in input().split()]
    e[a].append(b)
    e[b].append(a)



dist = [1]*n
ok = [0]*n

h = []
for _ in range(k):
    p,a = [int(x) for x in input().split()]
    p -= 1
    dist[p] = -a
    ok[p] = 1
    heappush(h,[-a,p])

while h:
    d,now = heappop(h)
    if dist[now] != d or d == 0:
        continue
    for nex in e[now]:
        if dist[nex] > d+1:
            dist[nex] = d+1
            ok[nex] = 1
            heappush(h,[d+1,nex])

ans = []
for i,f in enumerate(ok,1):
    if f:
        ans.append(i)

print(len(ans))
print(*ans)