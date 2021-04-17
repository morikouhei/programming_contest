a,b = map(int,input().split())

dif = b-a
for i in range(dif,0,-1):
    if b//i - (a-1)//i >= 2:
        print(i)
        exit()