x,y,z = map(int,input().split())

if (0 <= y <= x and 0 <= y <= z) or (x <= y <= 0 and z <= y <= 0):
    print(-1)
    exit()

if x*y < 0:
    print(abs(x))
    exit()
if 0 <= x <= y or y <= x <= 0:
    print(abs(x))
    exit()

if 0 <= z <= y <= x or x <= y <= z <= 0:
    print(abs(x))
else:
    print(abs(x)+abs(z)*2)