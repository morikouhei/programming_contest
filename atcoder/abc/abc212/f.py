import bisect
n,m,q = map(int,input().split())
e = [[] for i in range(n)]
bus = [list(map(int,input().split())) for i in range(m)]
for i,(a,b,s,t) in enumerate(bus):
    e[a-1].append((s,i))

for i in range(n):
    e[i].sort()

doubling = [[m]*(m+1) for i in range(20)]

for i,(a,b,s,t) in enumerate(bus):
    b -= 1
    ind = bisect.bisect_left(e[b],(t,-1))
    if ind == len(e[b]):
        continue
    doubling[0][i] = e[b][ind][1]

for i in range(1,20):
    for j in range(m):
        doubling[i][j] = doubling[i-1][doubling[i-1][j]]


for _ in range(q):
    x,y,z = map(int,input().split())
    y -= 1
    ind = bisect.bisect_left(e[y],(x,-1))
    if ind == len(e[y]):
        print(y+1)
        continue
    now = e[y][ind][1]
    if bus[now][2] >= z:
        print(y+1)
        continue
    for i in range(20)[::-1]:
        if doubling[i][now] == m:
            continue
        if bus[doubling[i][now]][2] < z:
            now = doubling[i][now]
    if bus[now][3] >= z:
        print(bus[now][0],bus[now][1])
    else:
        print(bus[now][1])