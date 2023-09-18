from collections import deque

n,m = map(int,input().split())
ABXY = [list(map(int,input().split())) for i in range(m)]
pos = [[-1,-1] for i in range(n)]
vis = [0]*n

e = [[] for i in range(n)]
for a,b,x,y in ABXY:
    a,b = a-1,b-1
    e[a].append([b,x,y])
    e[b].append([a,-x,-y])


vis[0] = 1
q = deque([])
q.append(0)
while q:
    now = q.popleft()

    x,y = pos[now]

    for nex,nx,ny in e[now]:
        if vis[nex]:
            continue
        vis[nex] = 1
        q.append(nex)
        pos[nex] = [x+nx,y+ny]

for i in range(n):
    if vis[i] == 0:
        print("undecidable")
    else:
        print(*pos[i])