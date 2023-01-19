def solve():
    n = int(input())
    A = list(map(int,input().split()))
    print(sum([a%2 for a in A]))


t = int(input())
for _ in range(t):
    solve()