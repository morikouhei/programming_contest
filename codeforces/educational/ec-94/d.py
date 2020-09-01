t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    cl = [0]*(n+1)
    cr = [0]*(n+1)
    for i in a:
        cr[i] += 1
    ans = 0
    for i in range(n-3):
        cl[a[i]] += 1
        now = a[i]
        nr = [cr[j]-cl[j] for j in range(n+1)]
        cand = 0
        cn = [0]*(n+1)
        for j in range(i+1,n-1):
            y = a[j]
            if y != now:
                cand += (nr[y]-cn[y]-1)*(cn[y]+1)-(nr[y]-cn[y])*(cn[y])
                cn[y] += 1
            else:
                ans += cand
                if nr[y]-cn[y]-1 > 0:
                    cand += (nr[y]-cn[y]-2)*(cn[y]+1)-(nr[y]-cn[y]-1)*(cn[y])
                cn[y] += 1
    print(ans)