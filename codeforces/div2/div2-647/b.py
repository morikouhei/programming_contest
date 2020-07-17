t = int(input())
for _ in range(t):
    n = int(input())
    s = set(map(int,input().split()))
    c = set()
    check = True
    for i in range(1,1024):
        c = set()
        for j in s:
            c.add(j^i)
        if s == c:
            print(i)
            check = False
            break
    if check:
        print(-1)
        