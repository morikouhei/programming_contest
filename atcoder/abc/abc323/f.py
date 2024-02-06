from heapq import heappush,heappop
l = list(map(int,input().split()))
X,Y = l[0:6:2],l[1:6:2]
if X[1] > X[2]:
    X = [-x for x in X]

if Y[1] > Y[2]:
    Y = [-y for y in Y]

l = [[X[0],Y[0]]]
for dx,dy in [[1,0],[0,1],[0,-1],[-1,0]]:
    l.append([X[1]+dx,Y[1]+dy])


pos = set()
for x,y in l:

    for nx,ny in l:

        if x != nx:
            pos.add((x,ny))
            pos.add((nx,y))
    pos.add((x,y))


dis = {}
inf = 10**20
for k in pos:
    dis[k] = inf

h = []
sx,sy = X[0],Y[0]
dis[(sx,sy)] = 0
heappush(h,[0,(sx,sy)])

bx,by = X[1],Y[1]

while h:
    d,k = heappop(h)
    x,y = k
    if dis[(x,y)] != d:
        continue

    for (nx,ny) in pos:

        if x == nx == bx and min(y,ny) <= by <= max(y,ny):
            continue
        if y == ny == by and min(x,nx) <= bx <= max(x,nx):
            continue
        if x != nx and y != ny:
            continue

        nd = d + abs(x-nx) + abs(y-ny)

        if nd < dis[(nx,ny)]:
            dis[(nx,ny)] = nd
            heappush(h,[nd,(nx,ny)])


dx = X[2]-X[1]
dy = Y[2]-Y[1]

ans = inf

num = dis[(bx-1,by)] + dx+dy
if dy:
    num += 2
ans = min(ans,num)

num = dis[(bx,by-1)] + dx+dy
if dx:
    num += 2
ans = min(ans,num)
print(ans)