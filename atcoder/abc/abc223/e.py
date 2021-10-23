x,y,a,b,c = map(int,input().split())

for i in range(3):
    for j in range(2):
        x,y = y,x

        nx = (a+y-1)//y
        nxb = (b+y-1)//y
        nxc = (c+y-1)//y
        if nx+nxb+nxc <= x:
            print("Yes")
            exit()

        left = x-nx
        if left <= 0:
            continue
        nxb = (b+left-1)//left
        nxc = (c+left-1)//left
        if nxb+nxc <= y:
            print("Yes")
            exit()

    a,b,c = b,c,a
print("No")