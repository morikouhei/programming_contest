t = int(input())
for _ in range(t):
    a,b,c = map(int,input().split())
    gcd = 1
    while len(str(gcd)) < c:
        gcd *= 5
    x = gcd
    while len(str(x)) < a:
        x *= 2
    y = gcd
    while len(str(y)) < b:
        y *= 3

    print(x,y)