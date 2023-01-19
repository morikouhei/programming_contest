def solve():
    n = int(input())

    p,q = 0,0
    for i in range(2,3*10**6+5):
        if n%i:
            continue
        c = 0
        while n%i == 0:
            n //= i
            c += 1
        if c == 2:
            return i,n
        else:
            p = int(n**0.5)
            for j in range(p-1,p+2):
                if j**2 == n:
                    return j,i


t = int(input())
for _ in range(t):
    p,q = solve()
    print(p,q)