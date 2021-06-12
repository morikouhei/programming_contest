def solve():
    n = int(input())
    s = input()
    a = []
    b = []
    big = 0
    for i in s:
        i = int(i)
        if big:
            a.append(0)
            b.append(i)
            continue
        if i == 2:
            a.append(1)
            b.append(1)
        elif i == 1:
            a.append(1)
            b.append(0)
            big = 1
        else:
            a.append(0)
            b.append(0)

    print(*a,sep="")
    print(*b,sep="")



t = int(input())
for _ in range(t):
    solve()