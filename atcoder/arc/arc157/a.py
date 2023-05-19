n,a,b,c,d = map(int,input().split())
if abs(b-c) > 1:
    print("No")
    exit()

if b+c == 0 and a*d:
    print("No")
    exit()


print("Yes")