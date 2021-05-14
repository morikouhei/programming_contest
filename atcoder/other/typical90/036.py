n,q = map(int,input().split())
XY = [tuple(map(int,input().split())) for i in range(n)]
Q = [int(input())-1 for i in range(q)]

l1 = []
l2 = []
for x,y in XY:
    l1.append(x-y)
    l2.append(x+y)
l1.sort()
l2.sort()
for q in Q:
    x,y = XY[q]
    a = x-y
    b = x+y
    print(max(a-l1[0],l1[-1]-a,b-l2[0],l2[-1]-b))