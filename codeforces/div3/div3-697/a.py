
def solve():
    n = int(input())
    while n%2 == 0:
        n //= 2
    if n == 1:
        return "NO"
    else:
        return "YES"


t = int(input())
for _ in range(t):
    ans = solve()
    print(ans)