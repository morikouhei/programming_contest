import sys
n,t = map(int,input().split())
for _ in range(t):
    k = int(input())
    l = 0
    r = n
    base = 0
    while r > l + 1:
        m = (r+l)//2
        print("?", 1,m)
        sys.stdout.flush()
        x = int(input())
        if m-x >= k:
            r = m
        else:
            l = m
    print("!",r)
    sys.stdout.flush()