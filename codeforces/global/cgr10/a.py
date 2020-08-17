t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    s = set(a)
    if len(s) == 1:
        print(n)
    else:
        print(1)