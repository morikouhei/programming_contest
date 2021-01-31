from collections import deque
n,m = map(int,input().split())
g = [[] for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)
k = int(input())
c = list(map(int,input().split()))
cost = [[10**10]*k for i in range(k)]
for i in range(k):
    now = c[i]
    dis = [10**10]*(n+1)
    dis[now] = 0
    q = deque([now])
    while q:
        v = q.popleft()
        for nex in g[v]:
            if dis[nex] > dis[v]+1:
                dis[nex] = dis[v]+1
                q.append(nex)
    for j in range(k):
        cost[i][j] = dis[c[j]]

dp = [[10**10]*(1<<k) for i in range(k)]

for i in range(k):
    dp[i][1<<i] = 1
for i in range(1,1<<k):
    for j in range(k):
        if dp[j][i] >= 10**10:
            continue
        for t in range(k):
            if i >> t & 1:
                continue
            dp[t][i|1<<t] = min(dp[t][i|1<<t],dp[j][i]+cost[j][t])
ans = 10**10
for i in range(k):
    ans = min(ans,dp[i][-1])
if ans == 10**10:
    print(-1)
else:
    print(ans)
