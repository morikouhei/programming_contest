n = int(input())
A = list(map(int,input().split()))
mod = 998244353

dp = [[[0]*(n+1) for i in range(n+1)] for j in range(n+1)]
for i in range(n+1):
    dp[i][0][0] = 1

for i,a in enumerate(A):

    for j in range(1,n+1):
        for k in range(i+1)[::-1]:
            for t in range(j):
                if dp[j][k][t] == 0:
                    continue
                nk = k+1
                nt = (t+a)%j
                dp[j][nk][nt] += dp[j][k][t]
                dp[j][nk][nt] %= mod

ans = 0
for i in range(1,n+1):
    ans += dp[i][i][0]
    ans %= mod
print(ans)