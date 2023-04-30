n,m,k = map(int,input().split())
A = list(map(int,input().split()))
mod = 998244353
nums = [0]*(m+1)
for a in A:
    nums[a] += 1

zero = nums[0]

N = n+5
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

used = 0
less = 0

for i in range(1,m+1):
    used += nums[i]

    count = 0
    for j in range(zero+1):
        if j+used < k:
            continue
        count += nCr(zero,j) * pow(i,j,mod) * pow(m-i,zero-j,mod) % mod

    ans += i * (count - less)
    ans %= mod
    less = count

ans *= pow(pow(m,zero,mod),mod-2,mod)
ans %= mod
print(ans)