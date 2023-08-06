n = int(input())
XYZ = [[[0]*(101) for i in range(101)] for j in range(101)]


for i in range(n):
    x1,y1,z1,x2,y2,z2 = map(int,input().split())

    for x in range(x1,x2):
        for y in range(y1,y2):
            for z in range(z1,z2):
                XYZ[x][y][z] = i+1

ans = [set() for i in range(n)]

for x in range(101):
    for y in range(101):
        for z in range(101):
            i = XYZ[x][y][z]
            if i == 0:
                continue

            for dx,dy,dz in [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]:
                nx = x+dx
                ny = y+dy
                nz = z+dz
                if 0 <= nx < 101 and 0 <= ny < 101 and 0 <= nz < 101 and XYZ[nx][ny][nz] and XYZ[nx][ny][nz] != i:
                    ans[i-1].add(XYZ[nx][ny][nz])
for i in ans:
    print(len(i))