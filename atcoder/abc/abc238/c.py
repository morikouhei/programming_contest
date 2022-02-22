n = int(input())
mod = 998244353
ans = 0

l = len(str(n))
for i in range(1,l):
    m = 9*10**(i-1)
    ans += m*(m+1)//2
    ans %= mod

dif = n-10**(l-1)+1

ans += dif*(dif+1)//2
ans %= mod
print(ans)