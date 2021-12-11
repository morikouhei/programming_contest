n = int(input())

mi = int(n**0.5)

ans = 0
for i in range(1,mi+1):
    ans += n//i

mi += 1
now = n//mi

while now:

    l = mi
    r = n+1
    while r > l + 1:
        m = (r+l)//2
        if n//m < now:
            r = m
        else:
            l = m
    ans += (r-mi)*now
    now -= 1
    mi = r
print(ans)