a,b,c = map(int,input().split())
mod = 998244353

ans = 1
for i in (a,b,c):
    ans *= i*(i+1)//2
    ans %= mod
print(ans)