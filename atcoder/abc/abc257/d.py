
from collections import deque
from dis import dis
n = int(input())
XYP = [list(map(int,input().split())) for i in range(n)]

dist = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        x,y,_ = XYP[i]
        nx,ny,_ = XYP[j]
        dist[i][j] = abs(x-nx)+abs(y-ny)

def calc(X,ind):
    vis = [0]*n
    vis[ind] = 1
    q = deque([ind])
    while q:
        now = q.popleft()
        x,y,p = XYP[now]
        for i in range(n):
            if vis[i]:
                continue
            if p*X >= dist[now][i]:
                vis[i] = 1
                q.append(i)

    return sum(vis) == n

ans = 10**10
for i in range(n):
    l = 0
    r = ans+1

    while r > l + 1:
        m = (r+l)//2
        if calc(m,i):
            r = m
        else:
            l = m
    ans = min(ans,r)
print(ans)