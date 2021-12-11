from decimal import Decimal
import sys
input = sys.stdin.readline
n = int(input())
L = []
for i in range(n):
    x,y = map(Decimal,input().split())
    if x == 1:
        L.append((Decimal(10**10),(y-1)/x))
    else:
        L.append((y/(x-1),(y-1)/x))

L.sort(key=lambda x: x[0])
ans = 0
last = Decimal(0)
for a,b in L:
    if last <= b:
        ans += 1
        last = a
print(ans)