import math
n = int(input())
XY = [list(map(int,input().split())) for i in range(n)]
XY.sort()
ans = 0
for i in range(n):
    for j in range(i):
        for k in range(j):
            x1,y1 = XY[i]
            x2,y2 = XY[j]
            x3,y3 = XY[k]
            if x1 == x2 == x3:
                continue
            if y1 == y2 == y3:
                continue
            dx1 = x2-x1
            dy1 = y2-y1
            g1 = math.gcd(dx1,dy1)
            dx1 //= g1
            dy1 //= g1

            dx2 = x3-x1
            dy2 = y3-y1
            g2 = math.gcd(dx2,dy2)
            dx2 //= g2
            dy2 //= g2

            if dx1 == dx2 and dy1 == dy2:
                continue
            ans += 1
print(ans)