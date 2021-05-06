import sys
n,t = map(int,input().split())
for _ in range(t):
    k = int(input())
    l = 1
    r = n//2
    size = n//4
    while size:
        print("?", l,r)
        sys.stdout.flush()
        x = int(input())
        if r-x >= k:
            r -= size
        else:
            r += size
        size //= 2
        if size == 0:
            break
    print("?", 1,r)
    sys.stdout.flush()
    x = int(input())
    if r-x == k:
        print("!", r)
    else:
        print("!",r+1)
    sys.stdout.flush()