n,x,y = map(int,input().split())
A = list(map(int,input().split()))
add = 0
while n%4:
    A.append(0)
    n += 1
    add += 1

XY = [y,x]

dirs = []

for i in range(2):
    nA = A[i::2]

    x = XY[i]

    c = len(nA)//2

    lA,rA = nA[:c],nA[c:]

    dic = {}
    lc = len(lA)
    rc = len(rA)

    for j in range(1<<lc):
        num = 0
        for k in range(lc):
            if j >> k & 1:
                num += lA[k]
            else:
                num -= lA[k]

        dic[num] = j
    ok = 0
    for j in range(1<<rc):
        num = 0
        for k in range(rc):
            if j >> k & 1:
                num += rA[k]
            else:
                num -= rA[k]

        if x-num in dic:
            dir = []
            for k in range(lc):
                if dic[x-num] >> k & 1:
                    dir.append(1)
                else:
                    dir.append(-1)
            
            for k in range(rc):
                if j >> k & 1:
                    dir.append(1)
                else:
                    dir.append(-1)

            dirs.append(dir)
            ok = 1
            break
    if ok == 0:
        print("No")
        exit()

    
ans = []

dir_all = [1]
for diry,dirx in zip(dirs[0],dirs[1]):
    dir_all.append(diry)
    dir_all.append(dirx)

for i in range(len(dir_all)-1):
    if i % 2 == 0:
        x,y = dir_all[i],0
        nx,ny = 0,dir_all[i+1]
    else:
        x,y = 0,dir_all[i]
        nx,ny = dir_all[i+1],0

    if x*ny - y * nx > 0:
        ans.append("L")
    else:
        ans.append("R")


while add:
    ans.pop()
    add -= 1
print("Yes")
print("".join(ans))
