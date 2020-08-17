t = int(input())
for _ in range(t):
    n = int(input())
    l = [int(i) for i in input().split()]
    l.sort()
    check = True
    for i in range(n-1):
        if abs(l[i+1]-l[i]) > 1:
            check = False
            break
    if check:
        print("YES")
    else:
        print("NO")
