from math import gcd
n = int(input())
L = []
for i in range(n):
    x,y,c = map(int,input().split())
    L.append((x*2,y*2,c))
dic = {}
for i in range(n):
    for j in range(i):
        x1,y1,c1 = L[i]
        x2,y2,c2 = L[j]
        w = c1+c2
        a = 2*(x2-x1)
        b = 2*(y2-y1)
        c = x2**2-x1**2+y2**2-y1**2
        nx,ny = (x1+x2)//2,(y1+y2)//2

        if x1 == x2:
            if b < 0:
                b *= -1
                c *= -1
            g = gcd(b,c)
            b //= g
            c //= g

        elif y1 == y2:
            if a < 0:
                a *= -1
                c *= -1
            g = gcd(a,c)
            a //= g
            c //= g
        else:
            if a < 0:
                a *= -1
                b *= -1
                c *= -1
            g = gcd(gcd(a,b),c)
            a //= g
            b //= g
            c //= g
        if (a,b,c) in dic:
            dic[(a,b,c)].append((w,nx,ny))
        else:
            dic[(a,b,c)] = [(w,nx,ny)]


ans = -1
for v in dic.values():
    V = sorted(v,reverse=True)
    w,x,y = V[0]
    for w2,x2,y2 in V[1:]:
        if x == x2 and y == y2:
            continue
        ans = max(ans,w+w2)
print(ans)