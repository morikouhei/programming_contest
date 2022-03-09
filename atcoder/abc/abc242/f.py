n,m,b,w = map(int,input().split())
mod = 998244353

N = n*m+5
fact = [1]*N
finv = [1]*N
 
for i in range(2,N):
    fact[i] = (fact[i-1]*i)%mod
finv[-1] = pow(fact[-1],mod-2,mod)
for i in range(1,N)[::-1]:
    finv[i-1] = (finv[i]*i)%mod

def nCr(n,r):
    if r > n:
        return 0
    else: 
        return fact[n]*finv[r]%mod*finv[n-r]%mod


ans = 0
dp = [[0]*(m+1) for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if i*j < b:
            continue
        for x in range(i+1):
            for y in range(j+1):
                if i == x and j == y:
                    dp[i][j] += nCr(x*y,b)
                else:
                    dp[i][j] -= dp[x][y]*nCr(i,x)*nCr(j,y)%mod
                dp[i][j] %= mod
        ans += dp[i][j]*nCr((n-i)*(m-j),w)*nCr(n,i)*nCr(m,j)%mod
        ans %= mod
print(ans)