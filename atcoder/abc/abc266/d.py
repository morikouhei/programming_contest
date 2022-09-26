n = int(input())

TXA = [list(map(int,input().split())) for i in range(n)]

last = 0
inf = 10**15
dp = [-inf]*5
dp[0] = 0

for t,x,a in TXA:

    ndp = [-inf]*5
    for i in range(5):
        ndp[i] = max(dp[i],ndp[i])
        if t-last >= abs(x-i):
            ndp[x] = max(ndp[x],dp[i]+a)
        for j in range(5):
            if t-last >= abs(i-j):
                ndp[j] = max(ndp[j],dp[i])
        
        
    dp = ndp
    last = t
print(max(dp))