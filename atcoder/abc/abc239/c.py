x1,y1,x2,y2 = map(int,input().split())

for i in range(x1-2,x1+2):
    for j in range(y1-2,y1+2):
        if (x1-i)**2+(y1-j)**2 == 5 and (x2-i)**2+(y2-j)**2 == 5:
            print("Yes")
            exit()

for i in range(x2-2,x2+2):
    for j in range(y2-2,y2+2):
        if (x1-i)**2+(y1-j)**2 == 5 and (x2-i)**2+(y2-j)**2 == 5:
            print("Yes")
            exit()


print("No")