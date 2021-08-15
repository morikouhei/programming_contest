n = int(input())
H = list(map(int,input().split()))
mod = 10**9+7

dp = [0]*(n+1)
dp[1] = 1
for i,(bh,h) in enumerate(zip(H,H[1:]),2):
    ndp = [0]*(n+1)
    if bh >= h:
        count = 0
        for j in range(1,i+1):
            ndp[j] += count
            count += dp[j]
            count %= mod
            
    if h >= bh:
        count = 0
        for j in range(i,0,-1):
            count += dp[j]
            count %= mod
            ndp[j] += count
            
            
    dp = ndp
print(sum(dp)%mod)