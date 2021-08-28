n = int(input())
mod = 998244353

ans = 0
for i in range(1,int(n**0.5)+1):
    x = n//i
    ans += (x-i+2)//2
    ans %= mod
print(ans)