a,b = input().split()
for x,y in zip(a[::-1],b[::-1]):
    x = int(x)
    y = int(y)
    if x+y >= 10:
        print("Hard")
        exit()
print("Easy")
