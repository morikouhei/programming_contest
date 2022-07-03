n,d = map(int,input().split())
d += 1
mod = 998244353

N = d+5
fact = [1]*N
finv = [1]*N
 
for i in range(2,N):
    fact[i] = (fact[i-1]*i)%mod
finv[-1] = pow(fact[-1],mod-2,mod)
for i in range(1,N)[::-1]:
    finv[i-1] = (finv[i]*i)%mod

def nCr(n,r):
    if r > n or r < 0:
        return 0

    else: 
        return fact[n]*finv[r]%mod*finv[n-r]%mod
        
def calc(a,b):
    ans = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                ans[i][j] += a[i][k]*b[k][j]
                ans[i][j] %= mod
    return ans


ans = 0
for i in range(d+1):
    A = [[nCr(d-2,i-2),nCr(d-2,i-1)],[nCr(d-2,i-1),nCr(d-2,i)]]
    base = [[1,0],[0,1]]
    nn = n
    while nn:
        if nn & 1:
            base = calc(A,base)
        nn //= 2
        A = calc(A,A)
    ans += base[0][0] + base[1][1]
    ans %= mod
print(ans)