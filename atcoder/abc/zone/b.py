n,D,H = map(int,input().split())
L = [list(map(int,input().split())) for i in range(n)]
l = 0
r = H
for i in range(60):
    m = (r+l)/2
    dif = H-m

    check = True
    for d,h in L:
        if h > m+dif*(d/D):
            check = False
    if check:
        r = m
    else:
        l = m

print(l)