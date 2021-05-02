from heapq import heappush, heappop
R,C = map(int,input().split())
A = [list(map(int,input().split())) for i in range(R)]
B = [list(map(int,input().split())) for i in range(R-1)]
e = [[] for i in range(R*C*2)]
for i in range(R):
    for j in range(C):
        id0 = i*2*C+j*2
        id1 = id0+1
        e[id0].append((id1,1))
        e[id1].append((id0,0))
        if j != C-1:
            e[id0].append((id0+2,A[i][j]))
        if j != 0:
            e[id0].append((id0-2,A[i][j-1]))
        if i != R-1:
            e[id0].append((id0+2*C,B[i][j]))
        if i != 0:
            e[id1].append((id1-2*C,1))

inf = 10**10
dis = [inf]*(R*C*2)
dis[0] = 0
mod = 1<<32
h = [0]
while h:
    d,i = divmod(heappop(h),mod)
    if d != dis[i]:
        continue

    for ind,c in e[i]:
        if dis[ind] > d+c:
            dis[ind] = d+c
            heappush(h,((d+c)<<32)+ind)
print(dis[-2])
