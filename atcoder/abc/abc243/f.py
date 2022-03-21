n,m,k = map(int,input().split())
mod = 998244353
N = max(n,k)+5
W = [int(input()) for i in range(n)]
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


dp = [[0]*(m+1) for i in range(k+1)]
dp[0][0] = 1

for i in range(n):
    for j in range(k)[::-1]:
        for t in range(m)[::-1]:
            if dp[j][t] == 0:
                continue
            for x in range(1,k-j+1):
                c = nCr(k-j,x)*pow(W[i],x,mod)%mod
                dp[j+x][t+1] += dp[j][t]*c%mod
                dp[j+x][t+1] %= mod
div = pow(sum(W),k,mod)
div = pow(div,mod-2,mod)
print(dp[k][m]*div%mod)