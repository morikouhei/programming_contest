def solve():
    n,k = map(int,input().split())
    base_n = n
    l = []
    while n:
        l.append(n%3)
        n //= 3

    l = l[::-1]

    if sum(l)%2 != k%2:
        return "No"

    if sum(l) <= k <= base_n:
        return "Yes"
    else:
        return "No"
    

t = int(input())
for _ in range(t):
    print(solve())
