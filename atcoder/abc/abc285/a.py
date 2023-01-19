a,b = map(int,input().split())
a,b = min(a,b),max(a,b)
if a == b//2:
    print("Yes")
else:
    print("No")