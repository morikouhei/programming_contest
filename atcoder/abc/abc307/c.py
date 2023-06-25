import copy
ha,wa = map(int,input().split())
base = [[0]*50 for i in range(50)]

alls = 0
for i in range(ha):
    a = input()
    for j in range(wa):
        if a[j] == "#":
            base[20+i][20+j] = 1
            alls += 1

hb,wb = map(int,input().split())
def get(h,w):
    B = []

    for i in range(h):
        b = input()
        nb = []
        for x in b:
            if x == ".":
                nb.append(0)
            else:
                nb.append(1)
        B.append(nb)
    return B

B = get(hb,wb)
hx,wx = map(int,input().split())
X = get(hx,wx)


for i in range(50-hb+1):
    for j in range(50-wb+1):

        A = copy.deepcopy(base)
        for x in range(hb):
            for y in range(wb):
                A[i+x][j+y] += B[x][y]

        
        minh,maxh,minw,maxw = 100,-1,100,-1

        for x in range(50):
            for y in range(50):
                if A[x][y]:
                    minh = min(minh,x)
                    maxh = max(maxh,x)
                    minw = min(minw,y)
                    maxw = max(maxw,y)

        
        for x in range(50-hx+1):
            for y in range(50-wx+1):
                if minh < x or maxh >= x+hx or minw < y or maxw >= y+wx:
                    continue

                ok = 1
                for h in range(hx):
                    for w in range(wx):
                        if X[h][w] and A[x+h][y+w] == 0:
                            ok = 0
                        if X[h][w] == 0 and A[x+h][y+w]:
                            ok = 0
                if ok:
                    print("Yes")
                    exit()
print("No")