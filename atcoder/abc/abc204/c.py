from collections import deque
n,m = map(int,input().split())
e = [[] for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    e[a-1].append(b-1)


def bfs(x):
    dis = [0]*n
    dis[x] = 1
    q = deque([x])
    while q:
        now = q.popleft()
        for nex in e[now]:
            if dis[nex]:
                continue
            dis[nex] = 1
            q.append(nex)
    return sum(dis)

ans = 0
for i in range(n):
    ans += bfs(i)
print(ans)