n,m = map(int,input().split())
n2 = n*2
par = [[0]*n2 for i in range(n2)]
for i in range(m):
    a,b = [int(x)-1 for x in input().split()]
    par[a][b] = par[b][a] = 1

mod = 998244353

fact = [1,1]
finv = [1,1]
inv = [0,1]
 
for i in range(2,n+5):
    fact.append((fact[-1]*i)%mod)
    inv.append((inv[mod%i]*(mod-mod//i))%mod)
    finv.append((finv[-1]*inv[-1])%mod)
 
def nCr(n,r,mod):
    if r > n:
        return 0
    else: 
        return fact[n]*finv[r]%mod*finv[n-r]%mod


dp = [[0]*(n+1) for i in range(n2+1)]
for i in range(n2+1):
    dp[i][0] = 1

for i in range(1,n+1):
    for j in range(n2):
        if j+2*i > n2:
            break
        for k in range(i):
            if par[j][j+1+2*k] == 0:
                continue
            dp[j][i] += dp[j+1][k]*dp[j+(k+1)*2][i-k-1]%mod*nCr(i,k+1,mod)%mod
            dp[j][i] %= mod
print(dp[0][n])
