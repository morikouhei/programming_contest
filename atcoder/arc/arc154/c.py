def solve():
    n = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    if A == B:
        return "Yes"

    compB = [B[0]]
    for b,nb in zip(B,B[1:]):
        if b != nb:
            compB.append(nb)

    if len(compB) >= 2 and compB[0] == compB[-1]:
        compB.pop()
    if len(compB) == n:
        return "No"

    s = len(compB)
    for i in range(n):
        now = 0
        for j in range(n):
            if A[(i+j)%n] == compB[now]:
                now += 1
            
            if now == s:
                return "Yes"
    return "No"
t = int(input())
for _ in range(t):
    print(solve())