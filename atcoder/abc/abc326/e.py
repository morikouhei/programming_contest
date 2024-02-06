n = int(input())
A = list(map(int,input().split()))
mod = 998244353

ans = 0

prob = 1

invn = pow(n,-1,mod)

for a in A:
    
    ans += a * (prob) * invn % mod
    ans %= mod

    prob += prob * invn
    prob %= mod
print(ans)