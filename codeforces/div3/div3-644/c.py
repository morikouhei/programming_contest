t = int(input())
for _ in range(t):
    n = int(input())
    l = sorted(list(map(int,input().split())))
    a = 0
    b = 0
    check = False
    for i in range(n):
        if l[i]%2:
            a += 1
        else:
            b += 1

        if i > 0:
            if l[i]-l[i-1] == 1:
                check = True
    if check:
        print("YES")
    elif a%2 == 0:
        print("YES")
    else:
        print("NO")