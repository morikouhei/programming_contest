import itertools

n,k = map(int,input().split())
mod = 998244353

if k == 1:
    A = [[1,1],[1,0]]

    def cal(x,y):
        ans = [[0]*2 for i in range(2)]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    ans[i][j] += x[i][k]*y[k][j]
                    ans[i][j] %= mod
        return ans

    ans = [[0]*2 for i in range(2)]
    for i in range(2):
        ans[i][i] = 1
    while n:
        if n%2:
            ans = cal(ans,A)
        A = cal(A,A)
        n //= 2
    print(sum(ans[0])%mod)
if n <= 6 and k <= 6:

    ans = 0
    for l in itertools.product([i for i in range(0,k+1)],repeat=n):
        ok = 1
        for i in range(n):
            m = l[i]
            for j in range(i+1,n):
                m = min(m,l[j])
                if m*(j-i+1) > k:
                    ok = 0
        if ok:
            ans += 1

    print(ans%mod)

if n <= 100 and k <= 100:
    dp = [[0]*(k+1) for i in range(n+1)]
    dp[0][0] = 1
    for i in range(1,n+1):
        ndp = [[0]*(k+1) for j in range(n+1)]
        for j in range(k+1):
            ndp[1][j] = 1
        for j in range(1,n+1):
            for m in range(k+1):
                for t in range(m,k+1):
                    if j*m <= k:
                        ndp[j][m] += dp[j-1][t]
                        ndp[j][m] %= mod
        dp = ndp
    print(sum(dp[n])%mod)
    