from math import gcd
n,m = map(int,input().split())
D = list(map(int,input().split()))
mod = 998244353
ans = 0
num = 1
for d in D:
    num *= m//d
    num %= mod
ans += num
print(ans)
for i in range(1,1<<n):
    b = bin(i).count("1")
    if b == 1:
        continue

    g = 1
    num = 1
    for j in range(n):
        if i >> j & 1:
            g = g*D[j]//(gcd(g,D[j]))
        else:
            num *= m//D[j]
            num %= mod
    num *= m//g
    num %= mod
    if b%2:
        ans += num
    else:
        ans -= num
    ans %= mod
    print(i,num)
print(ans)
