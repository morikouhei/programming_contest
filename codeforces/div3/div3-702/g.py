import bisect
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    X = list(map(int,input().split()))
    upd = [0]
    updl = [0]
    m = 0
    cum = 0
    for i,a in enumerate(A):
        cum += a
        if m < cum:
            m = cum
            upd.append(m)
            updl.append(i)
    
    ans = []
    for x in X:
        if x > m and cum <= 0:
            ans.append(-1)
            continue
        if x <= m:

            ind = bisect.bisect_right(upd, x)
            if upd[ind-1] >= x:
                ans.append(updl[ind-1])
            else:
                ans.append(updl[ind])

        else:    
            c = (x-m+cum-1)//cum
            base = c*n
            x = x-cum*c
            ind = bisect.bisect_right(upd, x)
            if upd[ind-1] >= x:
                ans.append(base+updl[ind-1])
            else:
                ans.append(base+updl[ind])
    
    print(*ans)