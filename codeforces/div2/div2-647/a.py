t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    if b > a:
        a,b = b,a
    if a%b:
        print(-1)
    elif a == b:
        print(0)
    else:
        a //= b
        count = 0
        while a%2 == 0:
            count += 1
            a //= 2
        if a > 1:
            print(-1)
        else:
            print((count+2)//3)
