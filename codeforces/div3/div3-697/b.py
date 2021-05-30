
def solve():
    n = int(input())
    for i in range(1000):
        if i*2020 > n:
            break
        if (n-i*2020)%2021 == 0:
            return "YES"
    return "NO"


t = int(input())
for _ in range(t):
    ans = solve()
    print(ans)