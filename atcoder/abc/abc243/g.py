M = 10**5+5
dp = [0]*M
dp[1] = 1
accum = 0
now = 1
for i in range(2,M):
    while now**2 <= i:
        accum += dp[now]
        now += 1
    dp[i] = accum

def solve():
    x = int(input())

    ans = 0
    l = 0
    r = x+5
    while r > l + 1:
        m = (r+l)//2
        if m**2 <= x:
            l = m
        else:
            r = m

    for i in range(1,M):
        i2 = i**2
        ans += max(0,l-i2+1)*dp[i]
    print(ans)

t = int(input())
for _ in range(t):
    solve()

