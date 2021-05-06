t = int(input())
for _ in range(t):
    n = int(input())
    count = 0
    for i in range(1,10):
        base = 0
        for j in range(15):
            base = base*10+i
            if base <= n:
                count += 1
    print(count)