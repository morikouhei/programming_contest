import math
def solve():
    n,d,k = map(int,input().split())
    if k == 1:
        return 0
    d %= n
    g = math.gcd(n,d)
    x = n//g
    a,b = divmod(k-1,x)

    sta = a
    ans = (sta+(b*d))%n
    return ans


t = int(input())
for _ in range(t):
    print(solve())
