n = int(input())
XY = [list(map(int,input().split())) for i in range(n+2)]


sXY = [[x,y,i] for i,(x,y) in enumerate(XY)]
sXY.sort()

def intersect(p1, p2, p3, p4):
    tc1 = (p1[0] - p2[0]) * (p3[1] - p1[1]) + (p1[1] - p2[1]) * (p1[0] - p3[0])
    tc2 = (p1[0] - p2[0]) * (p4[1] - p1[1]) + (p1[1] - p2[1]) * (p1[0] - p4[0])
    td1 = (p3[0] - p4[0]) * (p1[1] - p3[1]) + (p3[1] - p4[1]) * (p3[0] - p1[0])
    td2 = (p3[0] - p4[0]) * (p2[1] - p3[1]) + (p3[1] - p4[1]) * (p3[0] - p2[0])
    return tc1*tc2<0 and td1*td2<0

def calc(a,b,c):
    x1,y1 = XY[a]
    x2,y2 = XY[b]
    x3,y3 = XY[c]
    return (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)


pos = [intersect(XY[n],XY[n+1],XY[i],XY[(i+1)%n]) for i in range(n)]
if len(set(pos)) == 1:
    x,y = XY[-1]
    nx,ny = XY[-2]
    print(((x-nx)**2+(y-ny)**2)**0.5)
    exit()


# l = []
# for i in range(n+2):
#     while len(l) > 1 and calc(l[-2], l[-1], i) <= 0:
#         l.pop()
#     l.append(i)
 
# l2 = []
# for i in range(n+2):
#     while len(l2) > 1 and calc(l2[-2], l2[-1], i) >= 0:
#         l2.pop()
#     l2.append(i)


# convex = l + l2[::-1]
# convex = [sXY[i][2] for i in convex]

# ans = 10**20
# if n not in convex:
#     x,y = XY[-1]
#     nx,ny = XY[-2]
#     print(((x-nx)**2+(y-ny)**2)**0.5)
#     exit()

# index = convex.index(n)
# count = 0
# le = len(convex)
# while True:
#     x,y = XY[convex[index]]
#     index = (index+1)%le
#     nx,ny = XY[convex[index]]
#     count += ((x-nx)**2+(y-ny)**2)**0.5
#     if convex[index] == n+1:
#         break
# ans = min(ans,count)

# count = 0
# le = len(convex)
# while True:
#     x,y = XY[convex[index]]
#     index = (index-1)%le
#     nx,ny = XY[convex[index]]
#     count += ((x-nx)**2+(y-ny)**2)**0.5
#     if convex[index] == n+1:
#         break
# ans = min(ans,count)

# print(ans)