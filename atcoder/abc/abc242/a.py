a,b,c,x = map(int,input().split())
if a >= x:
    print(1)
elif a+1 <= x <= b:
    print(c/(b-a))
else:
    print(0)