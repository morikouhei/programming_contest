
n,m,q = map(int,input().split())
e = [[] for i in range(n)]
for i in range(m):
    a,b = [int(x)-1 for x in input().split()]
    e[a].append(b)
    e[b].append(a)
de = [[] for i in range(n)]
for now in range(n):
    for nex in e[now]:
        if len(e[now]) <= len(e[nex]):
            de[now].append(nex)
X = list(map(int,input().split()))
info = [[i+1,-1,1,-1] for i in range(n)]
for i in range(q):
    x = X[i]
    x -= 1
    for nex in de[x]:
        if info[x][1] < info[nex][3]:
            info[x][0] = info[nex][2]
            info[x][1] = info[nex][3]
    y = info[x][0]
    for nex in de[x]:
        info[nex][0] = y
        info[nex][1] = i
    info[x][0] = info[x][2] = y
    info[x][1] = info[x][3] = i

for x in range(n):
    for nex in de[x]:
        if info[x][1] < info[nex][3]:
            info[x][0] = info[nex][2]
            info[x][1] = info[nex][3]
ans = []

for i in range(n):
    ans.append(info[i][0])

print(*ans)