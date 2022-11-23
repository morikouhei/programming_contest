n = int(input())
XY = []
for i in range(n):
    a,b,c = map(int,input().split())
    XY.append([a/c,b/c])
XY.sort()

def calc(a,b,c):
    x1,y1 = XY[a]
    x2,y2 = XY[b]
    x3,y3 = XY[c]
    return (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)

# print(XY)
dconvex = []
for i in range(n):
    while len(dconvex) > 1 and calc(dconvex[-2], dconvex[-1], i) <= 0:
        dconvex.pop()
    dconvex.append(i)
# print(dconvex)

cost = 10**5
for x,y in XY:
    cost = min(cost,max(x,y))

for i,ni in zip(dconvex,dconvex[1:]):
    x,y = XY[i]
    nx,ny = XY[ni]
    if ny > nx:
        cost = min(cost,ny)
        continue
    if y < x:
        cost = min(cost,x)
        continue

    dy = y-ny
    dx = x-nx
    a = dy/dx
    b = y-a*x
    xx = b/(1-a)
    cost = min(cost,xx)
print(1/cost)


