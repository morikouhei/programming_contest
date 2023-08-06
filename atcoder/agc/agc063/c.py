n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

dic1 = {}
dic2 = {}

for a,b in zip(A,B):
    if a in dic1 and dic1[a] != b:
        print("No")
        exit()
    
    dic1[a] = b

    if b not in dic2:
        dic2[b] = set()
    dic2[b].add(a)


ope = []
for x in dic2.values():
    if len(x) == 1:
        continue

    s = sorted(x)

    for d1,d2 in zip(s,s[1:]):
        dx = d2-d1
        ope.append([dx-d1,dx])

        A = [(dx-d1+a)%dx for a in A]
    

dic1 = {}
dic2 = {}

for a,b in zip(A,B):
    if a in dic1 and dic1[a] != b:
        print("No")
        exit()
    
    dic1[a] = b

    if b not in dic2:
        dic2[b] = set()
    dic2[b].add(a)

sp = set()
sm = set()

for a,b in zip(A,B):
    dx = b-a
    if dx >= 0:
        sp.add(dx)
    else:
        sm.add(dx)

if len(sp) > 1 or len(sm) > 1:
    print("No")
    exit()

if len(sp) == 1 and len(sm) == 1:

    y = list(sp)[0] - list(sm)[0]
    dx = list(sp)[0]
    ope.append([dx,y])

elif len(sp) == 1:
    sp = list(sp)
    y = 10**18
    dx = sp[0]
    ope.append([dx,y])
else:
    sm = list(sm)
    y = 10**10
    dx = y+sm[0]
    ope.append([dx,y])

print("Yes")
print(len(ope))
for x,y in ope:
    print(x,y)