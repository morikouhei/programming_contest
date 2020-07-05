t = int(input())
for _ in range(t):
    n = int(input())
    two = 0
    thr = 0
    while n%2 == 0:
        n //= 2
        two += 1
    while n%3 == 0:
        n //= 3
        thr += 1
    if n != 1 or two > thr:
        print(-1)
    else:
        print(2*thr-two)