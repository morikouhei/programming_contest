import math
import bisect
n = int(input())
XY = [list(map(int,input().split())) for i in range(n)]

ans = 0

for x,y in XY:
    l = [-1000,1000]
    for nx,ny in XY:
        l.append(math.degrees(math.atan2(ny-y, nx-x)))
    l.sort()
    for i in range(1,n):
        ind = bisect.bisect_left(l, l[i]+180)
        a = min(l[ind-1]-l[i],360-l[ind-1]+l[i])
        b = min(l[ind]-l[i],360-l[ind]+l[i])
        ans = max(a,b,ans)
print(ans)