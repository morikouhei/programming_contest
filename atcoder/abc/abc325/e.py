from heapq import heappop,heappush
n,a,b,c = map(int,input().split())
D = [list(map(int,input().split())) for i in range(n)]

inf = 10**20
dist = [[inf]*2 for i in range(n)]

dist[0][0] = 0

h = [[0,0,0]]

while h:
    d,now,id = heappop(h)
    if dist[now][id] != d:
        continue
    
    for i in range(n):
        if i == now:
            continue
        
        nd = d + D[now][i]*b+c
        if dist[i][1] > nd:
            dist[i][1] = nd
            heappush(h,[nd,i,1])

        
        if id:
            continue

        nd = d + D[now][i]*a
        if dist[i][0] > nd:
            dist[i][0] = nd
            heappush(h,[nd,i,0])


print(min(dist[-1]))