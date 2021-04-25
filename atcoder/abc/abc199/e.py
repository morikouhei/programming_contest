n,m = map(int,input().split())
L = [list(map(int,input().split())) for i in range(m)]

cand = [[] for i in range(n)]
for x,y,z in L:
    cand[x].append((y,z))
dp = [0]*(1<<n)

dp[0] = 1
for i in range(1<<n):
    if dp[i] == 0:
        continue
    count = [0]*(n+1)
    bi = 0
    num = dp[i]
    for j in range(n):
        if i >> j & 1:
            count[j+1] += 1
            bi += 1
    for j in range(n):
        count[j+1] += count[j]

    for j in range(n):
        if i >> j & 1:
            continue
        check = True
        for y,z in cand[bi+1]:
            if j+1 <= y:
                if count[y]+1 > z:
                    check = False
                    break
            else:
                if count[y] > z:
                    check = False
                    break
        if check:
            dp[i|1<<j] += num

print(dp[-1])
                        

