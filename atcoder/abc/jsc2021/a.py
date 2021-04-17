x,y,z = map(int,input().split())
a = y/x
for i in range(10**6,-1,-1):
    if i/z < a:
        print(i)
        exit()