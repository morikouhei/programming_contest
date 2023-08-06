from collections import deque

n1,n2,m = map(int,input().split())
e = [[] for i in range(n1+n2)]
n = n1+n2
for _ in range(m):
    a,b = [int(x)-1 for x in input().split()]
    e[a].append(b)
    e[b].append(a)


inf = 10**10
def bfs(x):

    dis = [inf] * n

    q = deque([x])
    dis[x] = 0
    ans = 0
    while q:
        now = q.popleft()
        ans = max(ans,dis[now])
        for nex in e[now]:
            if dis[nex] > dis[now]+1:
                dis[nex] = dis[now]+1
                q.append(nex)


    return ans


ans = bfs(0)+bfs(-1)+1
print(ans)