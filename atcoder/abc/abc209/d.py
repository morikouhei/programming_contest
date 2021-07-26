from collections import deque
n,Q = map(int,input().split())
e = [[] for i in range(n)]
for _ in range(n-1):
    a,b = [int(x)-1 for x in input().split()]
    e[a].append(b)
    e[b].append(a)

dis = [-1]*n
dis[0] = 0
q = deque([0])
while q:
    now = q.popleft()
    for nex in e[now]:
        if dis[nex] == -1:
            dis[nex] = dis[now]^1
            q.append(nex)
for _ in range(Q):
    c,d = [int(x)-1 for x in input().split()]
    if dis[c] == dis[d]:
        print("Town")
    else:
        print("Road")