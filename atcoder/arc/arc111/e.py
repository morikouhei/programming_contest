def floor_sum(n,m,a,b):
    ans = 0
    if a >= m:
        ans += (n - 1) * n * (a // m) // 2;
        a %= m
    if b >= m:
        ans += n * (b // m)
        b %= m

    y_max = (a * n + b) // m
    x_max = (y_max * m - b)
    if y_max == 0:
        return ans
    ans += (n - (x_max + a - 1) // a) * y_max
    ans += floor_sum(y_max, a, m, (a - x_max % a) % a)
    return ans

t = int(input())

for _ in range(t):
    a,b,c,d = map(int,input().split())
    n = (d-1+c-b)//(c-b)
    x = floor_sum(n,d,c,a)
    y = floor_sum(n,d,b,a-1)
    print(n-x+y-1)
