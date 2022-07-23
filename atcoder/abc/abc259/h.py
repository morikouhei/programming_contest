n = int(input())
A = [list(map(int,input().split())) for i in range(n)]

mod = 998244353

### for bigger prime 
N = 2*n+5
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


num_dic = {}
for a in A:
    for i in a:
        num_dic[i] = num_dic.get(i,0)+1


less_dic = {}
less_num = set()
many_num = set()
for a,num in num_dic.items():
    if num < n:
        less_num.add(a)
        less_dic[a] = []
    else:
        many_num.add(a)

for i in range(n):
    for j in range(n):
        if A[i][j] in less_num:
            less_dic[A[i][j]].append([i,j])


ans = n**2
for values in less_dic.values():
    for i in range(len(values)):
        x,y = values[i]
        for j in range(i):
            nx,ny = values[j]
            if nx <= x and ny <= y:
                ans += nCr(x+y-nx-ny,x-nx)
                ans %= mod


dp = [[0]*n for i in range(n)]
for a in many_num:
    for i in range(n):
        for j in range(n):
            if A[i][j] == a:
                dp[i][j] = 1
            else:
                dp[i][j] = 0

    for i in range(n):
        for j in range(n):

            x = 0
            if i:
                x += dp[i-1][j]
            if j:
                x += dp[i][j-1]
            
            if dp[i][j]:
                ans += x
                ans %= mod
            dp[i][j] += x
            dp[i][j] %= mod
print(ans)