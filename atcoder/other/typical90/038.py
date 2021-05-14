import math
a,b = map(int,input().split())
g = math.gcd(a,b)
ans = a*b//g
print("Large" if ans > 10**18 else ans)