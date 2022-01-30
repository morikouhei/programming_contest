from collections import defaultdict
n,k = map(int,input().split())
XY = [list(map(int,input().split())) for i in range(n)]
ans = set()
dic = defaultdict(list)
for i,(x,y) in enumerate(XY):

    ix = x//k
    iy = y//k
    for dx,dy in ((0,0),(0,1),(1,0),(1,1)):
        iix = ix+dx
        iiy = iy+dy
        dic[(iix<<30)+iiy].append(i)

for lis in dic.values():

    for i in range(len(lis)):
        for j in range(i):

            x,y = XY[lis[i]]
            nx,ny = XY[lis[j]]
            if (nx-x)**2+(ny-y)**2 <= k**2:
                ans.add((lis[j],lis[i]))

ans = sorted(ans)
print(len(ans))
for x,y in ans:
    print(x+1,y+1)

        
