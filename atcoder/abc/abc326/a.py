x,y = map(int,input().split())

if (x < y and y-x <= 2) or (x > y and x-y <= 3):
    print("Yes")
else:
    print("No")