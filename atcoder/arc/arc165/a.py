def solve():
    n = int(input())
    divs = set()
    for i in range(2,int(n**0.5)+1):
        if n%i:
            continue
        divs.add(i)
        while n%i == 0:
            n //= i

    if n != 1:
        divs.add(n)

    return "Yes" if len(divs) != 1 else "No"

t = int(input())
for _ in range(t):
    print(solve())