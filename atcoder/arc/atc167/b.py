a,b = map(int,input().split())
mod = 998244353
if b == 0:
    print(0)
    exit()


divs = 1
even = 0

for i in range(2,int(a**0.5)+1):
    if a%i:
        continue
    num = 0
    while a % i == 0:
        a //= i
        num += 1
    if (num*b+1)%2 == 0:
        even = 1
    divs *= num*b+1
    divs %= mod

if a != 1:
    if (b+1) % 2 == 0:
        even = 1
    divs *= b+1
    divs %= mod

# print(divs,even)
if even == 0:
    divs -= 1
divs *= pow(2,mod-2,mod)
divs %= mod

ans = b*divs % mod
if even == 0:
    ans += b//2
    ans %= mod
print(ans)

