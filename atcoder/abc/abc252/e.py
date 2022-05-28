from heapq import heappush,heappop

n,m = map(int,input().split())
e = [[] for i in range(n)]
for i in range(m):
    a,b,c = map(int,input().split())
    a,b = a-1,b-1
    e[a].append([b,c,i])
    e[b].append([a,c,i])

inf = 10**20
mod = 1<<20
ans = []
dis = [inf]*n
dis[0] = 0
h = [0]
last = [-1]*n
while h:
    d,now = divmod(heappop(h),mod)
    if dis[now] != d:
        continue
    for nex,c,ind in e[now]:
        if dis[nex] > d+c:
            dis[nex] = d+c
            last[nex] = ind
            heappush(h,((d+c)<<20)+nex)

for i in range(1,n):
    ans.append(last[i]+1)
print(*ans)