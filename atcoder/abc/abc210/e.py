from math import gcd

n,m = map(int,input().split())
AC = [list(map(int,input().split())) for i in range(m)]
AC.sort(key=lambda x: x[1])

size = n
g = n
ans = 0
for a,c in AC:
    g = gcd(g,a)
    ans += (size-g)*c
    size = g
if size != 1:
    ans = -1
print(ans)