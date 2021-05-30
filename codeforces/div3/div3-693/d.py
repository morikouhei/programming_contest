def solve():
    n = int(input())
    A = sorted(list(map(int,input().split())),reverse=True)
    alice = 0
    bob = 0
    for i,a in enumerate(A):
        if i%2 and a%2:
            bob += a
        if i%2 == 0 and a%2 == 0:
            alice += a
    if alice > bob:
        return "Alice"
    if alice == bob:
        return "Tie"
    return "Bob"
    

t = int(input())
for _ in range(t):
    ans = solve()
    print(ans)