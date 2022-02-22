n,k = map(int,input().split())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))
mod = 998244353

PQ = [[p,q] for p,q in zip(P,Q)]
PQ.sort()

dp = [[0]*(n+1) for i in range(k+1)]
dp[0][n] = 1

for i in range(n):
    ndp = [[0]*(n+1) for i in range(k+1)]
    q = PQ[i][1]-1
    for j in range(k)[::-1]:
        for t in range(n+1):
            if dp[j][t] == 0:
                continue
            if j < k and q < t:
                ndp[j+1][t] += dp[j][t]
                ndp[j+1][t] %= mod
            ndp[j][min(t,q)] += dp[j][t]
            ndp[j][min(t,q)] %= mod
    dp = ndp

ans = sum(dp[k])%mod
print(ans)
