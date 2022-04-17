import math
n,k = map(int,input().split())
XY = [list(map(int,input().split())) for i in range(n)]

if k == 1:
    print("Infinity")
    exit()



ans = set()
for i in range(n):
    for j in range(i):
        x1,y1 = XY[i]
        x2,y2 = XY[j]
        count = 0
        for t in range(n):
            x,y = XY[t]
            if (x2-x1)*(y-y1) == (y2-y1)*(x-x1):
                count += 1
        
        if count < k:
            continue

        a = x2-x1
        b = y2-y1
        c = -x1*(y2-y1)+y1*(x2-x1)
        g = math.gcd(a,b)
        g = math.gcd(g,c)
        a //= g
        b //= g
        c //= g
        if a < 0:
            a *= -1
            b *= -1
            c *= -1
        elif a == 0:
            if b < 0:
                b *= -1
                c *= -1
        ans.add((a,b,c))
print(len(ans))
