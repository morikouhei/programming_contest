mod = 998244353

def solve():
    n = int(input())

    ans = 0
    for i in range(1,int(n**0.5)+1):
        y = i
        z = n//y
        if y > z:
            break
        
        ### consider x <= y <= z

        ### x,y,z is different
        ans += 6 * (i-1) * (z-i) % mod

        ### x,y,z is same
        if i**2 <= n:
            ans += 1

        ### x,y is same or y,z is same

        ans += 3 * (z-i) % mod
        ans += 3 * (i-1) % mod

        ans %= mod

    return ans

t = int(input())
for _ in range(t):
    print(solve())