
from heapq import heappush,heappop
n = int(input())
XY = [list(map(int,input().split())) for i in range(n)]

inf = 10**10
xmin = [(inf,n)]
xmax = [(inf,n)]
ymin = [(inf,n)]
ymax = [(inf,n)]
for i in range(n):
    x,y = XY[i]
    heappush(xmin,(x,i))
    heappush(xmax,(-x,i))
    heappush(ymin,(y,i))
    heappush(ymax,(-y,i))

ans = [0,0]
for i in range(n-1):
    x,y = XY[i]
    cand = []
    while xmin and xmin[0][1] < i:
        heappop(xmin)
    cand.append((x-xmin[0][0],xmin[0][1]))
    cand.append((x-xmin[1][0],xmin[1][1]))
    while xmax and xmax[0][1] < i:
        heappop(xmax)
    cand.append((-x-xmax[0][0],xmax[0][1]))
    cand.append((-x-xmax[1][0],xmax[1][1]))
    while ymin and ymin[0][1] < i:
        heappop(ymin)
    cand.append((y-ymin[0][0],ymin[0][1]))
    cand.append((y-ymin[1][0],ymin[1][1]))
    while ymax and ymax[0][1] < i:
        heappop(ymax)
    cand.append((-y-ymax[0][0],ymax[0][1]))
    cand.append((-y-ymax[1][0],ymax[1][1]))
    cand.sort(reverse=True)
    done = set()
    for m,ind in cand:
        if ind in done:
            continue
        done.add(ind)
        if ans[0] < m:
            ans[1] = ans[0]
            ans[0] = m
        elif ans[1] < m:
            ans[1] = m


print(ans[1])