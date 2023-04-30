sx,sy = map(int,input().split())
tx,ty = map(int,input().split())
a,b,c,d = map(int,input().split())

ans = []
def add(x,y):
    global sx,sy
    ans.append([x,y])
    sx = 2*x-sx
    sy = 2*y-sy

def no():
    print("No")
    exit()

def yes():
    print("Yes")
    for x,y in ans:
        print(x,y)
    exit()


if (sx%2 != tx%2) or (sy%2 != ty%2):
    no()

if (sx != tx and (a == b and a*2 != sx+tx)) or (sy != ty and (c == d and c*2 != sy+ty)):
    no()

if a == b and c == d:
    if sx == tx and sy == ty:
        yes()
    add(a,c)
    if sx == tx and sy == ty:
        yes()
    else:
        no()

if a == b:
    if sx != tx:
        add(a,c)

if c == d:
    if sy != ty:
        add(a,c)

while sx < tx:
    add(a,c)
    add(a+1,c)
while sx > tx:
    add(a+1,c)
    add(a,c)

while sy < ty:
    add(a,c)
    add(a,c+1)
while sy > ty:
    add(a,c+1)
    add(a,c)

yes()
