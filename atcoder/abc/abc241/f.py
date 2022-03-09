from collections import deque
import bisect

h,w,n = map(int,input().split())
H = {}
W = {}
sx,sy = map(int,input().split())
gx,gy = map(int,input().split())
for i in range(n):
    x,y = map(int,input().split())
    if x not in H:
        H[x] = []
    H[x].append(y)
    if y not in W:
        W[y] = []
    W[y].append(x)


for k in H.keys():
    H[k].sort()

for k in W.keys():
    W[k].sort()

dis = {}
dis[(sx,sy)] = 0

q = deque([[sx,sy]])

while q:
    x,y = q.popleft()
    d = dis[(x,y)]

    if y in W:
        l = W[y]
        i = bisect.bisect_left(l,x)

        if i < len(l) and (l[i]-1,y) not in dis:
            dis[(l[i]-1,y)] = d+1
            q.append([l[i]-1,y])
        if i and (l[i-1]+1,y) not in  dis:
            dis[(l[i-1]+1,y)] = d+1
            q.append([l[i-1]+1,y])

    if x in H:
        l = H[x]
        i = bisect.bisect_left(l,y)

        if i < len(l) and (x,l[i]-1) not in dis:
            dis[(x,l[i]-1)] = d+1
            q.append([x,l[i]-1])
        if i and (x,l[i-1]+1) not in dis:
            dis[(x,l[i-1]+1)] = d+1
            q.append([x,l[i-1]+1])

print(dis.get((gx,gy),-1))