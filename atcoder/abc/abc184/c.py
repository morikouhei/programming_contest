r1,c1 = map(int,input().split())
r2,c2 = map(int,input().split())
x = abs(r1-r2)
y = abs(c1-c2)
if y > x:
    x,y = y,x
if x == 0 and y == 0:
    print(0)
    exit()
if x == y:
    print(1)
    exit()
if x+y <= 3:
    print(1)
    exit()
if x+y <= 6:
    print(2)
    exit()
if (x+y)%2 == 0:
    print(2)
    exit()
if x-y <= 3:
    print(2)
    exit()
print(3)