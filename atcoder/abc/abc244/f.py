from collections import deque
n,m = map(int,input().split())
e = [[] for i in range(n)]
for i in range(m):
    u,v = [int(x)-1 for x in input().split()]
    e[u].append(v)
    e[v].append(u)


inf = 1000
dp = [[inf]*(1<<n) for i in range(n)]
for i in range(n):
    dp[i][0] = 0

q = deque([[0,i,0] for i in range(n)])

while q:
    c,nind,nbit = q.popleft()
    if dp[nind][nbit] != c:
        continue
    for nex in e[nind]:
        nnbit = nbit ^ (1<<nex)
        if dp[nex][nnbit] > c+1:
            dp[nex][nnbit] = c+1
            q.append([c+1,nex,nnbit])

ans = 0
for i in range(1<<n):
    mi = inf
    for j in range(n):
        mi = min(mi,dp[j][i])
    ans += mi
print(ans)