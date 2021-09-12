n = int(input())
XY = [tuple(map(int,input().split())) for i in range(n)]
dic = {}
for x,y in XY:
    dic[(x,y)] = 1

XY.sort()
ans = 0
for i in range(n):
    for j in range(i):
        x,y = XY[i]
        nx,ny = XY[j]
        if x == nx or y == ny:
            continue
        if (x,ny) in dic and (nx,y) in dic:
            ans += 1
print(ans//2)