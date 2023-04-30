h,w = map(int,input().split())
A = [list(map(int,input().split())) for i in range(h)]

ans = 0
dis = h+w-2
for i in range(1<<dis):
    if bin(i).count("1") != h-1:
        continue
    x,y = 0,0
    used = set()

    used.add(A[x][y])
    for j in range(dis):
        if i >> j & 1:
            x += 1
        else:
            y += 1
        used.add(A[x][y])
    if len(used) == dis+1:
        ans += 1
print(ans)