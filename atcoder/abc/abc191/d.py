from decimal import Decimal

x,y,r = map(Decimal, input().split())
mul = 10**4

x = int(x*Decimal(mul))%mul
y = int(y*Decimal(mul))%mul
r = int(r*Decimal(mul))

ans = 0
s = ((x-r)//mul-5)*mul
t = ((x+r)//mul+5)*mul

for i in range(s,t,mul):
    if abs(x-i) > r:
        continue
    l1 = y
    r1 = 10**10
    dif = r**2-(x-i)**2
    while (r1+mul-1)//mul > l1//mul+1:
        m = (r1+l1)//2
        if (y-m)**2 <= dif:
            l1 = m
        else:
            r1 = m
    l2 = -10**10
    r2 = y
    while (r2+mul-1)//mul > l2/mul+1:
        m = (r2+l2)//2
        if (y-m)**2 <= dif:
            r2 = m
        else:
            l2 = m
    ans += l1//mul-(r2+mul-1)//mul+1
print(ans)