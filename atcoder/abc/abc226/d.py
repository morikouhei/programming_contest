from math import gcd
n = int(input())
XY = [list(map(int,input().split())) for i in range(n)]

ans = set()
for i in range(n):
    for j in range(i):
        x,y = XY[i]
        nx,ny = XY[j]
        dx = x-nx
        dy = y-ny

        g = gcd(dx,dy)
        dx //= g
        dy //= g
        ans.add((dx,dy))
        ans.add((-dx,-dy))
print(len(ans))