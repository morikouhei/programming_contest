t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    for i in range(n):
        if i%2 and l[i] > 0:
            l[i] *= -1
        elif i%2 == 0 and l[i] < 0:
            l[i] *= -1
    print(*l)