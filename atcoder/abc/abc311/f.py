n,m = map(int,input().split())
S = [input() for i in range(n)]
mod = 998244353

dp = [0]*(n+1)
ndp = [0]*(n+1)
dp[-1] = 1

for i in range(m):
    last = n
    for j in range(n):
        if S[j][i] == "#":
            last = j
            break

    cum = dp[-1]
    for j in range(n+1)[::-1]:
        if j:
            cum += dp[j-1]
            cum %= mod
        
        if j <= last:
            ndp[j] = cum
        else:
            ndp[j] = 0
            
    dp = ndp
print(sum(dp)%mod)