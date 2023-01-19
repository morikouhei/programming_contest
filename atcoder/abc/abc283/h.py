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


def f(n,m,a,b):
    if b > n:
        return 0
    return floor_sum((n-b)//a+1,m,a,b)

def solve():
    n,m,r = map(int,input().split())

    ans = 0

    for i in range(30):
        ans += f(n+(1<<i),2<<i,m,r+(1<<i))-f(n,2<<i,m,r)
    
    print(ans)


t = int(input())
for _ in range(t):
    solve()