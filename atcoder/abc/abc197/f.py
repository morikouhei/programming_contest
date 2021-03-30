from collections import deque

n,m = map(int,input().split())
e = [[] for i in range(n)]
edge = set()
for i in range(m):
    a,b,c = input().split()
    a = int(a)-1
    b = int(b)-1
    e[a].append((b,c))
    e[b].append((a,c))
    edge.add((a,b))

inf = 10**10
dis = [[inf]*n for i in range(n)]
dis[0][n-1] = 0
q = deque([(0,n-1)])
while q:
    x,y = q.popleft()
    for nx,c1 in e[x]:
        for ny,c2 in e[y]:
            if c1 == c2 and dis[x][y]+1 < dis[nx][ny]:
                dis[nx][ny] = dis[x][y]+1
                q.append((nx,ny))

ans = inf
for i in range(n):
    ans = min(ans,dis[i][i]*2)

for x,y in edge:
    ans = min(ans,dis[x][y]*2+1,dis[y][x]*2+1)

if ans == inf:
    ans = -1
print(ans)