S = input()
K = int(input())
dic = {(0,0):1}
dx,dy = 0,0
X = [0]
Y = [0]
def change(x,y,s):
    if s == "L":
        x -= 1
    if s == "R":
        x += 1
    if s == "U":
        y -= 1
    if s == "D":
        y += 1
    return x,y


for s in S:
    dx,dy = change(dx,dy,s)
    dic[(dx,dy)] = 1
    X.append(dx)
    Y.append(dy)

if dx==dy==0:
    exit(print(len(dic)))

dicl = {}

if dx == 0:
    dx,dy = dy,dx
    X,Y = Y,X
for x,y in zip(X,Y):
    l = (x%dx,dx*y-dy*x)

    if l in dicl:
        dicl[l].add(x)
    else:
        dicl[l] = set([x])

d = 1
if dx < 0:
    d = -1
ans = 0
for v in dicl.values():
    ans += K
    v = sorted(list(v),key=lambda x: d*x)
    for x,nx in zip(v,v[1:]):
        ans += min((nx-x)//dx,K)
       
print(ans)
