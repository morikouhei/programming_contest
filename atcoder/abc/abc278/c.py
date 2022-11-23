n,q = map(int,input().split())
follows = {}

for _ in range(q):
    t,a,b = map(int,input().split())

    # a,b = min(a,b),max(a,b)

    if t == 1:
        follows[(a,b)] = 1
    elif t == 2:
        follows[(a,b)] = 0
    else:
        if (a,b) not in follows or (b,a) not in follows or follows[(a,b)] == 0 or follows[(b,a)] == 0:
            print("No")
        else:
            print("Yes")