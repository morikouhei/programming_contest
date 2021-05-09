t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int,input().split()))
    now = 0
    for a in A:
        now ^= a
    if now == 0:
        print("YES")
        continue
    last = now
    now = 0
    flag = 0
    for a in A:
        now ^= a
        if now == last:
            if flag == 0:
                flag = 1
        if now == 0 and flag:
            flag = 2
    if flag == 2:
        print("YES")
    else:
        print("NO")
