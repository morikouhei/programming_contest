n,W = map(int,input().split())
l = [tuple(map(int,input().split())) for i in range(n)]
V = n*1000+1
inf = 10**15
dp = [inf]*V
dp[0] = 0
for w,v in l:
    ndp = [inf]*V
    for i in range(V):
        ndp[i] = min(ndp[i],dp[i])
        if i + v < V:
            ndp[i+v] = min(ndp[i+v],dp[i]+w)
    dp = ndp
for i in range(V-1,-1,-1):
    if dp[i] <= W:
        print(i)
        exit()