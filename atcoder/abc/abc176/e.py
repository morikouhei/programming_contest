h,w,m = map(int,input().split())
H = [0]*(h+1)
W = [0]*(w+1)
d = {}
for i in range(m):
    x,y = map(int,input().split())
    d[(x,y)] = 1
    H[x] += 1
    W[y] += 1

mh = max(H)
mw = max(W)
la = []
lb = []
for i in range(h+1):
    if H[i] == mh:
        la.append(i)
    
for i in range(w+1):
    if W[i] == mw:
        lb.append(i)

ans = mh+mw-1

for i in la:
    for j in lb:
        if (i,j) not in d:
            print(ans+1)
            exit()
print(ans)
