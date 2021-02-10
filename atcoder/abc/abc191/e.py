from heapq import heappush, heappop
from collections import deque
n,m = map(int,input().split())
e = [[] for i in range(n+1)]

abc = [tuple(map(int,input().split())) for i in range(m)]
dic = {}
for a,b,c in abc:
    if (a,b) in dic:
        dic[(a,b)] = min(dic[(a,b)],c)
    else:
        dic[(a,b)] = c

for i,j in dic.items():
    x,y = list(i)
    e[x].append((y,j))
inf = 10**20
def search(i):
    dis = [inf]*(n+1)
    use = [0]*(n+1)
    q = [[0,i]]
    count = 0
    while q:
        d,now = heappop(q)
        if d and now == i:
            return dis[i]
        if use[now]:
            continue
        use[now] = 1
        for nex,c in e[now]:
            if d+c < dis[nex]:
                heappush(q,[d+c,nex])
                dis[nex] = d+c
   
    if dis[i] == inf:
        return -1
    else:
        return dis[i]

for i in range(1,n+1):
    print(search(i))