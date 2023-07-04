MAX = 10**9

ans = [[] for i in range(501)]

ans[1] = [1]
ans[3] = [2,3,6]
for i in range(4,501):
    base = ans[i-1][:]
    base.sort()
    s = set(base)
    for x in base:
        if x+1 > MAX or x+1 in s  or x*(x+1) > MAX or x*(x+1) in s:
            continue

        base.append(x+1)
        base.append(x*(x+1))
        base.remove(x)
        ans[i] = base
        break


t = int(input())
for _ in range(t):
    n = int(input())
    if n == 2:
        print("No")
    else:
        print("Yes")
        print(*ans[n])