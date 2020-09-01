n = int(input())
a = list(map(int,input().split()))
mod = 10**9+7

ans = 0
sa = sum(a)%mod

for i in a:
    sa -= i
    sa %= mod
    ans += i*sa%mod
    ans %= mod
print(ans)