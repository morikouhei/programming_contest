from decimal  import *
a,b = input().split()

b = Decimal(b)
a = Decimal(a)
ans = a*b
print(int(ans))

