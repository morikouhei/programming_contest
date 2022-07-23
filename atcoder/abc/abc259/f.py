
n = int(input())
D = list(map(int,input().split()))
e = [[] for i in range(n)]

for _ in range(n-1):
    u,v,w = map(int,input().split())
    u,v = u-1,v-1
    e[u].append((v,w))
    e[v].append((u,w))


q = [0]
par = [-1]*n
topo = []
while q:
    now = q.pop()
    topo.append(now)
    for nex,_ in e[now]:
        if nex == par[now]:
            continue
        q.append(nex)
        par[nex] = now


dp = [[0]*2 for i in range(n)]

for now in topo[::-1]:

    l = [0]
    base = 0
    for nex,w in e[now]:
        if nex == par[now]:
            continue

        base += dp[nex][0]
        if D[nex] == 0:
            l.append(0)
        else:
            l.append(dp[nex][1]+w-dp[nex][0])
    l.sort(reverse=True)
    for x in range(D[now]):
        if x == D[now]-1:
            dp[now][1] = base
        base += max(l[x],0)
    dp[now][0] = base

print(dp[0][0])
