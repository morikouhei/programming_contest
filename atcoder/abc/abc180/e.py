from collections import deque
n = int(input())
xyz = [list(map(int,input().split())) for i in range(n)]

cost = [[10**15]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        cost[i][j] = abs(xyz[i][0]-xyz[j][0])+abs(xyz[i][1]-xyz[j][1])+max(0,xyz[j][2]-xyz[i][2])

def calc(x):
    dis = [10**15]*n
    dis[x] = 0
    q = deque([x])
    while q:
        now = q.popleft()
        for i in range(n):
            if i == now:
                continue
            if dis[now]+cost[now][i] < dis[i]:
                dis[i] = dis[now]+cost[now][i]
                q.append(i)
    return dis

dist = []
for i in range(n):
    dist.append(calc(i))

dp = [[10**20]*n for i in range(1<<n)]
dp[(1<<n)-1][0] = 0
for s in range((1<<n)-1,-1,-1):
    for v in range(n):
        for u in range(n):
            if not (s>>u & 1):
                dp[s][v] = min(dp[s][v],dp[s| 1<<u][u]+dist[v][u])

print(dp[0][0])