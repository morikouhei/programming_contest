from collections import deque

n = int(input())
e = [[] for i in range(n)]
for _ in range(n-1):
    u,v = [int(x)-1 for x in input().split()]
    e[u].append(v)
    e[v].append(u)


topo = []
par = [-1]*n
q = deque([0])
while q:
    now = q.pop()
    topo.append(now)
    for nex in e[now]:
        if par[now] == nex:
            continue
        q.append(nex)
        par[nex] = now


match = [[0]*2 for i in range(n)]

for now in topo[::-1]:
    count = 0
    size = 0
    for nex in e[now]:
        if par[now] == nex:
            continue
        count += match[nex][1]
        size += 1
    if size == 0:
        continue
    match[now][0] = count
    num = 0
    for nex in e[now]:
        if par[now] == nex:
            continue
        num = max(num,count-match[nex][1]+match[nex][0]+1)
    match[now][1] = num
print(match)
    