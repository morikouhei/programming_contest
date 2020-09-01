h,w = map(int,input().split())
now = [[1,w]]

for i in range(h):
    a,b = map(int,input().split())
    nex = []
    for x,y in now:
        if x < a:
            nex.append([x,w])
            break
        else:
            if b < y and b != w:
                nex.append([b+1,w])
    if nex == []:
        print(-1)
    else:
        print(nex[0][0])
    now = nex
    