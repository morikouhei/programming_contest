n = int(input())
XY = [list(map(int,input().split())) for i in range(n+2)]


sXY = [[x,y,i] for i,(x,y) in enumerate(XY)]
sXY.sort()

def calc(a,b,c):
    x1,y1,_ = sXY[a]
    x2,y2,_ = sXY[b]
    x3,y3,_ = sXY[c]
    return (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)

l = []
for i in range(n+2):
    while len(l) > 1 and calc(l[-2], l[-1], i) <= 0:
        l.pop()
    l.append(i)
 
l2 = []
for i in range(n+2):
    while len(l2) > 1 and calc(l2[-2], l2[-1], i) >= 0:
        l2.pop()
    l2.append(i)


convex = l + l2[::-1]
convex = [sXY[i][2] for i in convex]

ans = 10**20
if n not in convex or n+1 not in convex:
    x,y = XY[-1]
    nx,ny = XY[-2]
    print(((x-nx)**2+(y-ny)**2)**0.5)
    exit()

index = convex.index(n)
count = 0
le = len(convex)
while True:
    x,y = XY[convex[index]]
    index = (index+1)%le
    nx,ny = XY[convex[index]]
    count += ((x-nx)**2+(y-ny)**2)**0.5
    if convex[index] == n+1:
        break
ans = min(ans,count)

count = 0
le = len(convex)
while True:
    x,y = XY[convex[index]]
    index = (index-1)%le
    nx,ny = XY[convex[index]]
    count += ((x-nx)**2+(y-ny)**2)**0.5
    if convex[index] == n+1:
        break
ans = min(ans,count)

print(ans)