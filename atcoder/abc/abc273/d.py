import bisect
h,w,x,y = map(int,input().split())
n = int(input())

dich = {}
dicw = {}
for i in range(n):
    r,c = map(int,input().split())
    if r not in dich:
        dich[r] = [0,w+1]
    dich[r].append(c)
    if c not in dicw:
        dicw[c] = [0,h+1]
    dicw[c].append(r)

for key in dich.keys():
    dich[key].sort()
for key in dicw.keys():
    dicw[key].sort()

q = int(input())
for _ in range(q):
    d,l = input().split()
    l = int(l)
    if d == "U":
        if y not in dicw:
            x = max(1,x-l)
        else:
            lind = bisect.bisect_left(dicw[y],x)
            dif = min(x-dicw[y][lind-1]-1,l)
            x = max(1,x-dif)

    if d == "D":
        if y not in dicw:
            x = min(h,x+l)
        else:
            lind = bisect.bisect_right(dicw[y],x)
            dif = min(dicw[y][lind]-x-1,l)
            x = min(h,x+dif)


    if d == "L":
        if x not in dich:
            y = max(1,y-l)
        else:
            lind = bisect.bisect_left(dich[x],y)
            dif = min(y-dich[x][lind-1]-1,l)
            y = max(1,y-dif)

    if d == "R":
        if x not in dich:
            y = min(w,y+l)
        else:
            lind = bisect.bisect_right(dich[x],y)
            dif = min(dich[x][lind]-y-1,l)
            y = min(w,y+dif)

    print(x,y)