a,b,x,y = map(int,input().split())
if a == b:
    print(x)
elif a > b:
    dif = a-b
    if 2*x <= y:
        print(2*x*(dif-1)+x)
    else:
        print((dif-1)*y+x)
else:
    dif = b-a
    if 2*x <= y:
        print(2*x*(dif)+x)
    else:
        print(dif*y+x)