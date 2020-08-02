t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    a,b = map(int,input().split())
    c,d = map(int,input().split())
    if c < a:
        a,b,c,d = c,d,a,b
    elif c == a and b < d:
        a,b,c,d = c,d,a,b
    count = 0
    if b > c:
        if d > b:
            k -= (b-c)*n
        else:
            k -= (d-c)*n
    if k <= 0:
        print(0)
        continue
    if b > c:
        if d > b:
            cal = (c+d-a-b)*n
            if cal >= k:
                print(k)
            else:
                print(cal+(k-cal)*2)
        else:
            cal = (c+b-a-d)*n
            if cal >= k:
                print(k)
            else:
                print(cal+(k-cal)*2)
    else:
        cost = c-a+d-b
        get = d-a
        if k <= get:
            print(c-b+k)
        else:
            count = cost
            k -= get
            if get*2 <= cost:
                print(count+k*2)
            else:
                ma = k//get
                if ma >= n-1:
                    print(cost*n+(k-get*(n-1))*2)
                else:
                    count += ma*cost
                    k -= ma*get
                    print(count+min(k*2,c-b+k))