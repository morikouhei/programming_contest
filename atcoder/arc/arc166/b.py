import math
n,*ABC = map(int,input().split())
A = list(map(int,input().split()))

inf = 10**20
dp = [inf]*8
dp[0] = 0

for a in A:

    ndp = dp[:]

    for i in range(8):
        if dp[i] == inf:
            continue

        for j in range(8):
            t = 1
            for k in range(3):
                if j >> k & 1:
                    t = math.lcm(t,ABC[k])
            
            if a%t == 0:
                ndp[i|j] = min(ndp[i|j],dp[i])
            else:
                ndp[i|j] = min(ndp[i|j],dp[i]+(t-a%t))
    dp = ndp
print(dp[7])