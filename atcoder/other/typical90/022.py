from math import gcd
a,b,c = map(int,input().split())
g = gcd(a,gcd(b,c))
print(a//g+b//g+c//g-3)
