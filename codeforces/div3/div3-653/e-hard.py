n,m,k = map(int,input().split())
ab = []
a = []
b = []
other = []
l = [list(map(int,input().split())) for i in range(n)]
for i in range(n):
    t,c,d = l[i]
    if c and d == 0:
        a.append([t,i+1])
    elif d and c == 0:
        b.append([t,i+1])
    elif c*d:
        ab.append([t,i+1])
    else:
        other.append([t,i+1])
a.sort()
b.sort()
ab.sort()
other.sort()
la = len(a)
lb = len(b)
lab = len(ab)
lo = len(other)
a.append([float("INF"),-1])
b.append([float("INF"),-1])
ab.append([float("INF"),-1])
other.append([float("INF"),-1])
if la<lb:
    la,lb = lb,la
    a,b = b,a
ans = float("INF")
count = 0
ia = 0
ib = 0
iab = 0
io = 0
ana = 0
anb = 0
anab = 0
ano = 0
for i in range(lab+1):
    if k-i > lb:
        continue
    if 2*k-i > m:
        continue
    if i + la + lb + lo < m: 
        continue
    if ia > 0:
        ia -= 1
        count -= a[ia][0]
    if ib > 0:
        ib -= 1
        count -= b[ib][0]
    if io > 0:
        io -= 1
        count -= other[io][0]
    while ia < la and ia < k-i:
        count += a[ia][0]
        ia += 1
    while ib < lb and ib < k-i:
        count += b[ib][0]
        ib += 1
    while iab < lab and iab < i:
        count += ab[iab][0]
        iab += 1

    while ia+ib+iab+io < m:
        na = a[ia][0]
        nb = b[ib][0]
        no = other[io][0]
        
        mi = min(na,nb,no)
        if mi == na:
            count += na
            ia += 1
        elif mi == nb:
            count += nb
            ib += 1
        else:
            count += no
            io += 1
    if count < ans:
        ans = count
        ana = ia
        anb = ib
        anab = iab
        ano = io
    
if ans == float("INF"):
    print(-1)
else:
    print(ans)
    l = []
    for i in range(ana):
        l.append(a[i][1])
    for i in range(anb):
        l.append(b[i][1])
    for i in range(anab):
        l.append(ab[i][1])
    for i in range(ano):
        l.append(other[i][1])
    print(*l)