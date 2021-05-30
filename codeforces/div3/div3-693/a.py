def solve():
    w,h,n = map(int,input().split())
    a = 1
    while w%2 == 0:
        a *= 2
        w //= 2
    b = 1
    while h %2 == 0:
        b *= 2
        h //= 2
    if a*b >= n:
        return "YES"
    else:
        return "NO"

t = int(input())
for _ in range(t):
    ans = solve()
    print(ans)