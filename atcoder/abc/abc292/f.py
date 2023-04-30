import math
a,b = map(int,input().split())
if b < a:
    a,b = b,a


l = 0
r = 30

def f(x):

    l = a / math.cos(math.radians(x))
    if l * math.cos(math.radians(30-x)) <= b:
        return l
    else:
        return 0

for i in range(100):
    c1 = (2*l+r)/3
    c2 = (l+2*r)/3

    if f(c1) > f(c2):
        r = c2
    else:
        l = c1
# print(l,r)
print(f(l))