n,x,y = map(int,input().split())
A = list(map(int,input().split()))

if x <= y:
    for a in A:
        d = a%(x+y)
        if x <= d < x+y:
            print("First")
            exit()
    print("Second")
else:
    for a in A:
        d = a%(x+y)
        if x <= d < x+y:
            print("Second")
            exit()
    print("First")