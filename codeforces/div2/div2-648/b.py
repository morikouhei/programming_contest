t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    l2 = sorted(l)
    b = list(map(int,input().split()))
    if l == l2:
        print("Yes")
    elif 1 in b and 0 in b:
        print("Yes")
    else:
        print("No")