from math import gcd
l,r = map(int,input().split())

ans = 0
for i in range(10):
    for j in range(10):
        l1 = j+l
        r1 = r-i
        if r1 >= l1:
            if gcd(r1,l1) == 1:
                ans = max(ans,r1-l1)
print(ans)