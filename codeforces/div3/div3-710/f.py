t = int(input())
for _ in range(t):
    n = int(input())
    r = list(map(int,input().split()))
    c = list(map(int,input().split()))
    l = [(r[i],c[i]) for i in range(n)]
    l.sort()
    x,y = 1,1
    ans = 0
    for nx,ny in l:
        need = ny-y
        dif = nx-x
        if (x+y)%2 == 0:
            if dif == need:
                ans += need
            else:
                left = dif-need
                ans += left//2
        else:
            if dif == need:
                ans += 0
            else:
                left = dif-need
                ans += (left+1)//2
        x = nx
        y = ny
    print(ans)