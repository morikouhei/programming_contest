n,t,m = map(int,input().split())
pars = [[0]*n for i in range(n)]
for _ in range(m):
    a,b = [int(x)-1 for x in input().split()]
    pars[a][b] = pars[b][a] = 1


cans = [0]*(1<<n)

for b in range(1<<n):

    can = 1
    for i in range(n):
        if b >> i & 1 == 0:
            continue

        for j in range(n):
            if b >> j & 1 and pars[i][j]:
                can = 0
    
    cans[b] = can



dp = [[0]*(1<<n) for i in range(t+1)]

for i in range(1,1<<n,2):
    if cans[i]:
        dp[1][i] = 1


for i in range(1,t):
    for b in range(1<<n):
        if dp[i][b] == 0:
            continue

        mi = -1
        for j in range(n):
            if b >> j & 1:
                continue
            mi = j

        if mi == -1:
            continue

        for nb in range(1<<n):
            if b & nb or cans[nb] == 0:
                continue
            if nb >> mi & 1:
                dp[i+1][b|nb] += dp[i][b]
print(dp[-1][-1])
