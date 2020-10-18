n,m,l = map(int,input().split())

mod = 10**9+7

nCr = [[0]*(n+1) for i in range(n+1)]
nCr[0][0] = 1
for i in range(n):
    for j in range(i+1):
        nCr[i+1][j] += nCr[i][j]
        nCr[i+1][j] %= mod
        nCr[i+1][j+1] += nCr[i][j]
        nCr[i+1][j+1] %= mod

path = [1,1,1]
for i in range(3,l+1):
    path.append(path[-1]*i%mod)

def f(n,m,l):
    dp = [[0]*(m+1) for i in range(n+1)]
    dp[0][0] = 1

    for i in range(n+1):
        for j in range(m+1):
            for k in range(1,l+1):
                if i + k > n:
                    break
                if j + k - 1 > m:
                    break
                dp[i+k][j+k-1] += nCr[n-i-1][k-1]*path[k]%mod*dp[i][j]%mod
                dp[i+k][j+k-1] %= mod
                
                if j + k > m:
                    break
                if k >= 2:
                    dp[i+k][j+k] += nCr[n-i-1][k-1]*path[k-1]%mod*dp[i][j]%mod
                    dp[i+k][j+k] %= mod
                
    return dp[n][m]

ans = f(n,m,l) - f(n,m,l-1)
print(ans%mod)
