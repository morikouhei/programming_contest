def solve():
    a,b = map(int,input().split())
    print((b-a%b)%b)


t = int(input())
for _ in range(t):
    solve()