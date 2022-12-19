a,b = map(int,input().split())


# b*(g-1) + a/g**0.5
l = 1
r = a**2+5

def calc(x):
    count = b*(x-1)
    count += a/(x**0.5)
    return count

for i in range(200):
    m1 = (2*l+r)/3
    m2 = (l+2*r)/3

    c1 = calc(m1)
    c2 = calc(m2)

    if c1 > c2:
        l = m1
    else:
        r = m2
# print(l,r)
ans = 10**36
for i in range(max(int(l)-5,1),int(r)+5):
    ans = min(ans,calc(i))
print("{:.10f}".format(ans))