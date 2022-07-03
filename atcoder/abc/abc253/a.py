l = list(map(int,input().split()))
b = l[1]
if sorted(l)[1] == b:
    print("Yes")
else:
    print("No")