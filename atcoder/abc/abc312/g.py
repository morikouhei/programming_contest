n = int(input())
e = [[] for i in range(n)]
for _ in range(n-1):
    a,b = [int(x)-1 for x in input().split()]
    e[a].append(b)
    e[b].append(a)


topo = []

par = [-1]*n

q = [0]
while q:
    now = q.pop()
    topo.append(now)

    for nex in e[now]:
        if nex == par[now]:
            continue
        par[nex] = now
        q.append(nex)


size = [0]*n
num = 0

for now in topo[::-1]:

    left = n-1
    si = 1
    for nex in e[now]:
        if par[now] == nex:
            continue
        si += size[nex]

        left -= size[nex]
        num += size[nex] * left
    size[now] = si


ans = n*(n-1)*(n-2)//6 - num
print(ans)

