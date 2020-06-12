n = int(input())
e = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    e[a].append(b)
    e[b].append(a)

def getpar(x,d,p):
    depth[x] = d
    ax = ancestor[x]
    ax[0] = p
    for i in range(d.bit_length()-1):
        ax[i+1] = ancestor[ax[i]][i]
    for nex in e[x]:
        if nex == p:
            continue
        getpar(nex,d+1,x)
 
depth = [0]*(n+1)
ancestor = [[0]*19 for i in range(n+1)]
getpar(1,0,0)
 
def LCA(x,y):
    dx = depth[x]
    dy = depth[y]
 
    if dx > dy:
        x,y = y,x
        dx,dy = dy,dx
    dif = dy-dx
    while dif:
        s = dif & (-dif)
        y = ancestor[y][s.bit_length()-1]
        dif -= s
    while x != y:
        j = 0
        while ancestor[x][j] != ancestor[y][j]:
            j += 1
        if j == 0:
            return ancestor[x][0]
        x = ancestor[x][j-1]
        y = ancestor[y][j-1]
    return x
 
q = int(input())
for i in range(q):
    a,b = map(int,input().split())
    print(depth[a]+depth[b]-2*depth[LCA(a,b)] + 1)
