t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    e = 0
    o = 0
    for i in range(n):
        if i%2:
            if l[i]%2 == 0:
                o += 1
        else:
            if l[i]%2 == 1:
                e += 1
    if e != o:
        print(-1)
    else:
        print(e)