n = int(input())
C = list(map(int,input().split()))
M = 10**6+5
ans = [0]*M

dist = [[0]*10 for i in range(10)]
for i,c in enumerate(C,1):
    for j,nc in enumerate(C,1):
        dist[i][j] = c+nc

mp = 0
mi = 0
for i,c in enumerate(C,1):
    p = n//c
    if p >= mp:
        mp = p
        mi = i
    mp = max(p,mp)

for i,c in enumerate(C,1):
    p = n//c
    if p != mp or i != mi:
        continue

    nans = [0]*M
    for j in range(p):
        nans[-1-j] = i
    cost = n-p*c
    now = -p
    while now != 0:
        upd = 0
        for j in range(i+1,10)[::-1]:
            nc = C[j-1]
            if nc > c and nc-c <= cost:
                nans[now] = j
                cost -= nc-c
                now += 1
                upd = 1
                break
        if upd == 0:
            break

    # for j,c in enumerate(C,1):
    #     if c <= cost:
    #         nans[-p] = j


    check = 1
    for j in range(M):
        if nans[j] < ans[j]:
            check = 0
            break
        if nans[j] > ans[j]:
            break
    if check:
        ans = nans

ans = [str(i) for i in ans]
for i in range(M):
    if ans[i] != "0":
        print("".join(ans[i:]))
        exit()