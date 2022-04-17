from heapq import heappop,heappush
import sys
input = sys.stdin.readline
n,m,k,l = map(int,input().split())
A = list(map(int,input().split()))
B = [int(x)-1 for x in input().split()]
e = [[] for i in range(n)]
for i in range(m):
    u,v,c = map(int,input().split())
    u,v = u-1,v-1
    e[u].append((v,c))
    e[v].append((u,c))


inf = 10**20
dis = [inf]*n
dis2 = [inf]*n
town1 = [-1]*n
town2 = [-1]*n
h = []
for b in B:
    dis[b] = 0
    town1[b] = A[b]
    heappush(h,[0,b,A[b]])

while h:
    d,now,town = heappop(h)
    if (dis[now] == d and town1[now] == town) or (dis2[now] == d and town2[now] == town):

        for nex,c in e[now]:
            if dis[nex] > d+c:
                if town1[nex] == town:
                    dis[nex] = d+c
                else:
                    town2[nex] = town1[nex]
                    dis2[nex] = dis[nex]
                    town1[nex] = town
                    dis[nex] = d+c
                heappush(h,[d+c,nex,town])
                

            elif dis2[nex] > d+c:
                if town1[nex] == town:
                    continue
                town2[nex] = town
                dis2[nex] = d+c
                heappush(h,[d+c,nex,town])

        



ans = [0]*n
for i in range(n):
    if A[i] == town1[i]:
        ans[i] = dis2[i]
    else:
        ans[i] = dis[i]
    if ans[i] == inf:
        ans[i] = -1
print(*ans)