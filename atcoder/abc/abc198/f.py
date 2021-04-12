S = int(input())
mod = 998244353

S -= 6

def comb(a,b):
    x = 1
    y = 1
    for i in range(b):
        y *= (i+1)
        x *= a-i
        x %= mod
    y = pow(y,mod-2,mod)
    return x*y%mod

ans = 0
ans += comb(S+5, 5)
if S%2 == 0:
    ans += comb(S//2+2, 2)*6
    ans %= mod

if S%3 == 0:
    ans += comb(S//3+1, 1)*8
    ans %= mod

for i in range(2):
    for j in range(2):
        n = S-i-j
        if n >= 0 and n%2 == 0:
            ans += comb(n//2+3, 3)*3
            ans %= mod

for i in range(4):
    for j in range(4):
        n = S-i-j
        if n >= 0 and n%4 == 0:
            ans += comb(n//4+2, 2)*6
            ans %= mod

inv = pow(24,mod-2,mod)
print(ans*inv%mod)