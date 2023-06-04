n,m,h,k = map(int,input().split())
S = input()
XY = set([tuple(map(int,input().split())) for i in range(m)])

x,y = 0,0
for s in S:
    h -= 1
    if s == "R":
        x += 1
    elif s == "L":
        x -= 1
    elif s == "U":
        y += 1
    elif s == "D":
        y -= 1
    
    if h < 0:
        print("No")
        exit()
    if (x,y) in XY and h < k:
        h = k
        XY.remove((x,y))
print("Yes")