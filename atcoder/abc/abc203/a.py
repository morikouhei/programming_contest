a,b,c = map(int,input().split())
if a == b:
    print(c)
elif c == a:
    print(b)
elif b == c:
    print(a)
else:
    print(0)