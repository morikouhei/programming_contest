n = int(input())
ans = 0
XY = [list(map(int,input().split())) for i in range(n)]

for i in range(n):
    for j in range(i):
        x,y = XY[i]
        nx,ny = XY[j]
        ans = max(ans,((x-nx)**2+(y-ny)**2)**0.5)
print(ans)