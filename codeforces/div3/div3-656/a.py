t = int(input())
for _ in range(t):
    l = list(map(int,input().split()))
    l2 = sorted(l)
    if l2[0] < l2[1] < l2[2]:
        print("NO")
    elif l2[0] == l2[1] < l2[2]:
        print("NO")
    else:
        print("YES")
        print(l2[2],l2[0],l2[0])
    