n,m = map(int,input().split())
XY = [list(map(int,input().split())) for i in range(n)]
PQ = [list(map(int,input().split())) for i in range(m)]


pos = [[0,0]]+XY+PQ
mask = 0
mask2 = 0
for i in range(1,n+m+1):
    if 1 <= i <= n:
        mask2 |= 1<<i
    else:
        mask |= 1<<i
s = len(pos)
inf = 10**20
dp = [[inf]*(1<<s) for i in range(s)]
dp[0][1] = 0

for b in range(1<<s):

    num = bin(b&mask).count("1")
    speed = 1<<num

    for i in range(s):
        if dp[i][b] == inf:
            continue
        x,y = pos[i]
        for j in range(s):
            if b >> j & 1:
                continue
            nx,ny = pos[j]
            d = ((x-nx)**2+(y-ny)**2)**0.5
            t = dp[i][b]+d/speed
            dp[j][b|1<<j] = min(dp[j][b|1<<j],t)

ans = inf
for i in range(s):
    for b in range(1<<s):
        if dp[i][b] == inf:
            continue
        if mask2 & b != mask2:
            continue

        num = bin(b&mask).count("1")
        speed = 1<<num
        x,y = pos[i]
        d = (x**2+y**2)**0.5
        t = dp[i][b]+d/speed
        ans = min(ans,t)
print(ans)
