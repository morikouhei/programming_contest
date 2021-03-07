n = int(input())
P = list(map(float,input().split()))
dp = [0]*(n+1)
dp[0] = 1
for i,p in enumerate(P,1):
    ndp = [0]*(n+1)
    for j in range(i):
        if dp[j] == 0:
            continue
        ndp[j] += dp[j]*(1-p)
        ndp[j+1] += dp[j]*p
    dp = ndp
  
print(sum(dp[n//2+1:]))
