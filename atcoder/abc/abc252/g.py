n = int(input())
P = list(map(int,input().split()))
mod = 998244353
dp = [[0]*(n+1) for i in range(n)]
dp2 = [[0]*(n+1) for i in range(n)]
for i in range(n):
    dp[i][1] = 1

for i in range(2,n+1):
    for ind in range(n-i+1):
        p1 = P[ind]
        dp[ind][i] = (dp[ind+1][i-1]+dp2[ind+1][i-1])%mod
        for j in range(ind+1,ind+i):
            s1 = j-ind
            s2 = i-s1
            if p1 < P[j]:
                dp2[ind][i] += (dp[ind][s1])*(dp[j][s2]+dp2[j][s2])%mod
                dp2[ind][i] %= mod

print(dp[0][n])