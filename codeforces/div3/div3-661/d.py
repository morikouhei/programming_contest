t = int(input())
for _ in range(t):
    n = int(input())
    S = input()
    ans = []
    zero = []
    one = []
    now = 0
    for s in S:
        if s == "1":
            if zero == []:
                now += 1
                add = now
                one.append(now)
            else:
                add = zero.pop()
                one.append(add)
        else:
            if one == []:
                now += 1
                add = now
                zero.append(now)
            else:
                add = one.pop()
                zero.append(add)
        ans.append(add)
    print(now)
    print(*ans)
