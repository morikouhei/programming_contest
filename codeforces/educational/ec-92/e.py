import math
t = int(input())
for _ in range(t):
    m,d,w = map(int,input().split())
    l = min(m,d)
    
    if (d-1)%w == 0:
        print(l*(l-1)//2)
    else:
        gcd = math.gcd(w,d-1)
        w2 = w//gcd
        a = l-w2
        if a > 0:
            b = l%w2
            c = l//w2
            print((a+b)*c//2)
        else:
            print(0)