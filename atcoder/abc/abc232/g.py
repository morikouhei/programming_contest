from heapq import heappush,heappop
from bisect import bisect_left
n,m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
B2 = [[b,i] for i,b in enumerate(B)]
B2.sort()
B.sort()



e = [[] for i in range(2*n)]
for i in range(n):
    e[i+n].append((B2[i][1],0))
    if i == n-1:
        continue

    e[i+n].append((n+(i+1)%n,(B[(i+1)%n]-B[i])%m))

for i,a in enumerate(A):
    ind = bisect_left(B,m-a)
    e[i].append((n,(a+B[0])%m))
    if ind != n:
        e[i].append((n+ind,(a+B[ind])%m))


inf = 1<<64
mod = 1<<20
dis = [inf]*(2*n)
dis[0] = 0
h = [0]
while h:
    d,now = divmod(heappop(h),mod)
    if dis[now] < d:
        continue
    for nex,cost in e[now]:
        if dis[nex] > d+cost:
            dis[nex] = d+cost
            heappush(h,(dis[nex]<<20)+nex)
print(dis[n-1])
