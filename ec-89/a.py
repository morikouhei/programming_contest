t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    if b > a:
        a,b = b,a
    dif = a-b
    count = min(b,dif)
    b -= count
    a -= count*2
    if b > 0:
        x = (a+b)//3
        print(count+x)
    else:
        print(count)