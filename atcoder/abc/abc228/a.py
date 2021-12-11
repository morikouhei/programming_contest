s,t,x = map(int,input().split())
if s > t:
    t += 24

if s <= x < t or s <= x+24 < t:
    print("Yes")
else:
    print("No")
