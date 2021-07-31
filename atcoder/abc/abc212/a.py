a,b = map(int,input().split())
if 0 < a and b == 0:
    print("Gold")
elif a == 0 and b > 0:
    print("Silver")
else:
    print("Alloy")