n = int(input())
edge = [0]*(27**3)
valid = [1]*(27**3)
for i in range(27):
    for j in range(27):
        for k in range(27):
            if j == 26 and i != 26:
                valid[i*27**2+j*27+k] = 0
for i in range(n):
    t,p = input().split()
    p = -int(p)

    nt = [ord(s)-ord("a") for s in t]

    if len(t) == 3:
        id = nt[0]*27**2+nt[1]*27+nt[2]
        edge[id] += p
        

    elif len(t) == 2:
        id = nt[0]*27+nt[1]
        for j in range(27):
            edge[id+j*27**2] += p

    else:
        for j in range(27):
            for k in range(27):

                id = j*27**2+k*27+nt[0]
                edge[id] += p


inf = 10**15
dp = [inf]*(27**2)
dp[-1] = 0

for i in range(27**2+5):
    upd = 0

    for id,num in enumerate(edge):
        if valid[id] == 0:
            continue
        fr = id//27
        to = id%(27**2)
        if dp[fr]+num < dp[to]:
            dp[to] = dp[fr]+num
            # print(fr,to,dp[to])
            upd = 1
    if upd == 0:
        print(-min(dp[1:-1]))
        exit()
print("Infinity")