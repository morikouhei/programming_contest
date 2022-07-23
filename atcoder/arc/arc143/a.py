a,b,c = map(int,input().split())

L = [a,b,c]
if L.count(0) == 1:
    x,y = 0,0
    for l in L:
        if l:
            x = l
            x,y = y,x
    if x != y:
        print(-1)
        exit()

elif L.count(0) == 2:
    print(-1)
    exit()
elif L.count(0) == 3:
    print(0)
    exit()

m = max(L)

A = []
for l in L:
    A.append(m-l)

for i in range(3):
    x = A[i]
    for j in range(3):
        if i == j:
            continue
        L[j] -= x
if min(L) < 0:
    print(-1)
    exit()
print(sum(A)+min(L))