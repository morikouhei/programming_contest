t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    if b > a:
        a,b = b,a
    dif = a-b
    count = min(b,dif)
    b -= count
    a -= count*2
    count += (min(a,b)//3)*2
    print(count)