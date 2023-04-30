M = 2*10**6+5
mod = 998244353

fact = [1]*M
for i in range(2,M):
    fact[i] = fact[i-1]*i%mod


t = int(input())
for _ in range(t):
    n = int(input())

    ans = (n-1)*n**2*(n**2-3)%mod*fact[2*n-4]%mod
    ans *= pow(fact[n]**2,mod-2,mod)
    ans %= mod
    print(ans)