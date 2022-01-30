n,k = map(int,input().split())
A = list(map(int,input().split()))
mod = 998244353


A[0] = 2*A[0]-sum(A)-k
if A[0] < 0:
    exit(print(0))

kinv = 1
for i in range(1,k):
    kinv *= i
    kinv %= mod
kinv = pow(kinv,mod-2,mod)

ans = 1
for a in A:
    p = 1
    for i in range(k-1):
        p *= a+k-1-i
        p %= mod
    ans *= p*kinv%mod
    ans %= mod
print(ans)