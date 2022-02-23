from collections import deque

n = int(input())
e = [[] for i in range(n)]
for i in range(n-1):
    a,b = [int(x)-1 for x in input().split()]
    e[a].append(b)
    e[b].append(a)
ans = [[n+1,0] for i in range(n)]

par = [-1]*n
topo = []
q = deque([0])
while q:
    now = q.pop()
    topo.append(now)
    for nex in e[now]:
        if par[now] == nex:
            continue
        q.append(nex)
        par[nex] = now

num = 0
for now in topo[::-1]:
    l = n+1
    r = 0
    for nex in e[now]:
        if par[now] == nex:
            continue
        l = min(l,ans[nex][0])
        r = max(r,ans[nex][1])
    if l == n+1:
        num += 1
        ans[now] = [num,num]
    else:
        ans[now] = [l,r]

for i in ans:
    print(*i)