t = int(input())
for _ in range(t):
    n,x,m = map(int,input().split())
    le = x
    ri = x
    for i in range(m):
        a,b = map(int,input().split())
        if a <= le <= b:
            le = a
        if a <= ri <= b:
            ri = b
    print(ri-le+1)
