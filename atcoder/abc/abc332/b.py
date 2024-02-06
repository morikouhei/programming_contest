k,g,m = map(int,input().split())

a,b = 0,0
for i in range(k):
    if a == g:
        a = 0
        continue
    if b == 0:
        b = m
        continue
    dif = min(g-a,b)
    a += dif
    b -= dif
print(a,b)