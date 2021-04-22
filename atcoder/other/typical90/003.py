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
    dis = [n]*n
    dis[x] = 0
    q = deque([x])
    while q:
        now = q.popleft()
        for nex in e[now]:
            if dis[nex] > dis[now]+1:
                dis[nex] = dis[now]+1
                q.append(nex)

    return dis

def diameter():
    dis = bfs(0)
    m = dis.index(max(dis))
    dis2 = bfs(m)
    return max(dis2)

print(diameter()+1)