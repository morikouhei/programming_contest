h,w,n = map(int,input().split())
L = [list(map(int,input().split())) for i in range(n)]
H = set()
W = set()
for x,y in L:
    H.add(x)
    W.add(y)

dich = {x:i for i,x in enumerate(sorted(list(H)))}
dicw = {x:i for i,x in enumerate(sorted(list(W)))}

for x,y in L:
    print(dich[x]+1,dicw[y]+1)