h,w,n,m = map(int,input().split())
l = [[0]*w for i in range(h)]

ab = [tuple(map(int,input().split())) for i in range(n)]
cd = [tuple(map(int,input().split())) for i in range(m)]
for a,b in ab:
    a -= 1
    b -= 1
    l[a][b] = 1
for c,d in cd:
    c -= 1
    d -= 1
    l[c][d] = -1

for i in range(h):
    now = 0
    while now < w:
        count = 0
        check = False
        while now+count < w and l[i][now+count] != -1: 
            if l[i][now+count] == 1:
                check = True
            count += 1
            
        if check:
            for j in range(count):
                if l[i][now+j] == 1:
                    continue
                l[i][now+j] = 2
        now += count+1


for i in range(w):
    now = 0
    while now < h:
        count = 0
        check = False
        while now+count < h and l[now+count][i] != -1: 
            if l[now+count][i] == 1:
                check = True
            count += 1
            
        if check == False:
            now += count+1
            continue
        if check:
            for j in range(count):
                if l[now+j][i] == 1:
                    continue
                l[now+j][i] = 2
            now += count+1

ans = 0
for i in range(h):
    for j in range(w):
        if l[i][j] > 0:
            ans += 1
print(ans)