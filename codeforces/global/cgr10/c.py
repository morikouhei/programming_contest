t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))+[float("INF")]
    ans = 0
    now = 0
    d = 1
    m = 0
    for i in range(n+1):
        if a[i] >= m:
            if d == 1:
                
                ans += m-now
            else:
                ans += m-now
                d = 1
        else:
            if a[i] >= now:
                ans += a[i]-now
                d = 1
            else:
                now = a[i]
                d = -1
        now = a[i]
        m = max(m,now)
    print(ans)

