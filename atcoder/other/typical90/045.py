n,k = map(int,input().split())
XY = [tuple(map(int,input().split())) for i in range(n)]

inf = 10**18
dis = []
for i in range(1<<n):
    d = 0
    for j in range(n):
        if i >> j & 1:
            for t in range(j):
                if i >> t & 1:
                    x1,y1 = XY[j]
                    x2,y2 = XY[t]
                    d = max(d,(x1-x2)**2+(y1-y2)**2)
    dis.append(d)
dp = [[inf]*(k+1) for i in range(1<<n)]
for i in range(1<<n):
    dp[i][1] = dis[i]
for j in range(1,k):
    for i in range(1,1<<n):
        now = i & (i-1)
        s = inf
        while now > now^i:
            x,y = dp[now][j],dis[now^i]
            if s > x and s > y:
                s = x if x > y else y
            now = (now-1) & i
        dp[i][j+1] = s
print(dp[-1][-1])
