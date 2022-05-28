n = int(input())
XY = [list(map(int,input().split())) for i in range(n)]
m = int(input())
UV = [list(map(int,input().split())) for i in range(m)]
q = int(input())
AB = [list(map(int,input().split())) for i in range(q)]


def cross_product(a,b):
    ax,ay = a
    bx,by = b
    return ax*by - ay*bx


def check_clockwise(a,b):
    dx,dy = a[1][0]-a[0][0],a[1][1]-a[0][1]
    tx,ty = b[1][0]-a[0][0],b[1][1]-a[0][1]
    if cross_product([dx,dy],[tx,ty]) >= 0:
        return 1
    else:
        return 0


L = [[[0,0],[0,0]] for i in range(n)]
for i in range(m):
    u,v = UV[i]
    for j in range(n):
        ax,ay = XY[j]
        bx,by = XY[(j+1)%n]
        sv = [ax+u,ay+v]
        gv = [bx+u,by+v]
        nv = [sv,gv]
        if i == 0 or check_clockwise(L[j],nv):
            L[j] = nv

for a,b in AB:
    inner = 1
    for i in range(n):
        v = [[0,0],[a,b]]
        if check_clockwise(L[i],v) == 0:
            inner = 0

    print("Yes" if inner else "No")


    