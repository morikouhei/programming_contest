n = int(input())
XYZ = [list(map(int,input().split())) for i in range(n)]

ans = n


for i in range(n):
    x,y,z = XYZ[i]
    for j in range(n):
        nx,ny,nz = XYZ[j]
        if nx <= x:
            continue

        