n = int(input())
S = input()
mod = 10**9+7

dp = [1]*n

for s in S:
    ndp = [0]*n
    if s == "<":
        for i in range(n-1)[::-1]:
            ndp[i] += dp[i+1]
            dp[i] += dp[i+1]
            dp[i] %= mod
    else:
        for i in range(1,n):
            ndp[i] += dp[i-1]
            dp[i] += dp[i-1]
            dp[i] %= mod
    dp = ndp
    print(dp)
print(sum(dp)%mod)
print(dp)
            
        
    
