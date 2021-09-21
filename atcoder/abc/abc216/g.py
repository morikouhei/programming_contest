from heapq import heappop, heappush

n,m = map(int,input().split())
e = [[] for i in range(n+1)]
for i in range(n):
    e[i].append((i+1,0))
    e[i+1].append((i,1))

for i in range(m):
    l,r,x = map(int,input().split())
    y = r-l+1-x
    e[r].append((l-1,y))

dis = [10**10]*(n+1)
dis[n] = 0 
h = [[0,n]]
while h:
    d,now = heappop(h)
    if dis[now] != d:
        continue
    for nex,c in e[now]:
        if dis[nex] > d+c:
            dis[nex] = d+c
            heappush(h,[dis[nex],nex])


for i in range(n+1):
    dis[i] += i

ans = [dis[i+1]-dis[i] for i in range(n)]
print(*ans)