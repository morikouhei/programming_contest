n,k = map(int,input().split())
A = list(map(int,input().split()))
mod = 998244353
M = 4*10**5+5
### for bigger prime 
N = M+5
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
nums = [0]*M
for a in A:
    nums[a] = 1

left = k
ans = 0
last = 0
for i in range(M):
    if nums[i] == 0:
        left -= 1

    if left < 0:
        break
    ans += nCr(left-nums[i]+i,i)
    ans %= mod
    if left == 0:
        break

print(ans)