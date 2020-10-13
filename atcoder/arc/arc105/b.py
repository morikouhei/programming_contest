import math
n = int(input())
a = list(map(int,input().split()))
now = a[0]
for i in a[1:]:
    now = math.gcd(now,i)
print(now)