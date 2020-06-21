import math

x = int(input())
y = (x*360)//math.gcd(x,360)//x
print(y)