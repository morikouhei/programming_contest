from decimal import *
T = int(input())

def ctemp(x):
    return (h*(x+1)+c*x)/(2*x+1)
def ctemp2(x):
    return (h*(x+1)+c*x)/(2*x+1)

for _ in range(T):
    h,c,t = map(int,input().split())
    now = abs((h+c)/2-t)
    if (h+c)/2 >= t:
        print(2)
    else:
        l = 0
        r = h
        while r > l + 1:
            m = (r+l)//2
            temp = ctemp(m)
            
            if temp > t:
                l = m
            else:
                r = m
        h = Decimal(h)
        c = Decimal(c)
        t = Decimal(t)
        temp1 = ctemp2(l)
        temp2 = ctemp(r)
        if abs(temp1-t) <= abs(temp2-t):
            print(2*l+1)
        else:
            print(2*r+1)
            
