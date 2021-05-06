from collections import deque
import io,os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n,m,w = map(int,input().split())
E = [list(map(int,input().split())) for i in range(n)]
inf = 10**20
ans = inf
dx = [0,0,1,-1]
dy = [1,-1,0,0]

dp = [inf]*(n*m)
dp[0] = 0
q = deque([0])
cost = inf

while q:
    id = q.popleft()
    a,b = divmod(id,m)
    if E[a][b] > 0:
        cost = min(cost,E[a][b]+dp[id]*w)
    for i in range(4):
        nx = a+dx[i]
        ny = b+dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and E[nx][ny] != -1:
            nid = nx*m+ny
            if dp[nid] > dp[id]+1:
                dp[nid] = dp[id]+1
                q.append(nid)
ans = dp[-1]*w

dp = [inf]*(n*m)
dp[(n-1)*m+m-1] = 0
q = deque([(n-1)*m+m-1])
cost2 = inf
while q:
    id = q.popleft()
    a,b = divmod(id,m)
    if E[a][b] > 0:
        cost2 = min(cost,E[a][b]+dp[id]*w)
    for i in range(4):
        nx = a+dx[i]
        ny = b+dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and E[nx][ny] != -1:
            nid = nx*m+ny
            if dp[nid] > dp[id]+1:
                dp[nid] = dp[id]+1
                q.append(nid) 

ans = min(ans,cost+cost2)
if ans >= inf:
    print(-1)
else:
    print(ans)



