from heapq import heappop, heappush
n,m,x,y = map(int,input().split())
x -= 1
y -= 1
e = [[] for i in range(n)]
for i in range(m):
    a,b,t,k = map(int,input().split())
    a -= 1
    b -= 1
    e[a].append((b,t,k))
    e[b].append((a,t,k))


inf = 10**20

dis = [inf]*n
dis[x] = 0

h = [(0,x)]
while h:
    time,now = heappop(h)
    if dis[now] < time:
        continue
    for nex,t,k in e[now]:
        need = k-time%k
        if need == k:
            need = 0
        if dis[nex] > time+need+t:
            dis[nex] = time+need+t
            heappush(h,(dis[nex],nex)) 
    
ans = dis[y]
if ans == inf:
    ans = -1
print(ans)