n,a,b,p,q = map(int,input().split())
mod = 998244353
dp = [[0]*(n+1) for i in range(n+1)]

pat = pow(p*q,mod-2,mod) ### 1/pq

dp[a][b] = 1

for i in range(n):
    for j in range(n):
        if dp[i][j] == 0:
            continue

        for x in range(1,p+1):
            for y in range(1,q+1):
                nx = min(i+x,n)
                ny = min(j+y,n)
                dp[nx][ny] += dp[i][j]*pat
                dp[nx][ny] %= mod
# print(dp)
ans = 0
for i in range(n+1):
    ans += dp[n][i]
    ans %= mod
print(ans)