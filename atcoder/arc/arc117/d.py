import sys
sys.setrecursionlimit(30)
from collections import deque
n = int(input())
e = [[] for i in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    e[a].append(b)
    e[b].append(a)


def bfs(x):
    dis = [n]*(n)
    dis[x] = 0
    q = deque([x])
    while q:
        now = q.popleft()
        for nex in e[now]:
            if dis[nex] > dis[now]+1:
                dis[nex] = dis[now]+1
                q.append(nex)
    return dis

dis = bfs(0)
dis = bfs(dis.index(max(dis)))
ans = [-1]*n
print(dis)
def dfs(x,num):
    ans[x] = num
    p = -1
    print(x)
    for nex in e[x]:
        if ans[nex] > 0:
            continue
        if dis[nex] == dis[x]-1:
            p = nex
            continue
        num = dfs(nex,num+1)+1
    if p == -1:
        return num
    dfs(p,num+1)
print(dis,dis.index(max(dis)))
dfs(dis.index(max(dis)),1)
print(ans)
    


