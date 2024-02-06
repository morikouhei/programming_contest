n,d = map(int,input().split())
W = list(map(int,input().split()))


inf = (1<<60) - 1.0
xbar = sum(W)/d
dp = [inf]*(1<<n)
dp[-1] = 0

count = [0]*(1<<n)
for i in range(1<<n):
    num = 0
    for j in range(n):
        if i >> j & 1:
            num += W[j]

    count[i] = num

d2 = d**2
for i in range(d):

    ndp = [inf]*(1<<n)
    
    for bi in range(1<<n):
        if dp[bi] == inf:
            continue

        s = bi
        ndp[bi] = min(ndp[bi],dp[bi]+xbar**2)
        while s:

            num = count[s]
            ndp[bi^s] = min(ndp[bi^s],dp[bi]+(num-xbar)**2)
            s = (s-1)&bi

    dp = ndp
print(dp[0]/d)            
