import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())

    ab = [list(map(int,input().split())) for i in range(m)]
    
    mb = 0
    ab.sort(reverse=True)
    for i in range(m):
        mb = max(mb,ab[i][1])
    nb = 0
    ans = 0
    
    for i in range(0,m):
        a,b = ab[i]
        
        if a >= mb:
            ans += a
            nb = max(nb,b)
            n -= 1
        if n == 0 or a < mb:
            break
    
    nc = nb*n
    l = i
    for i in range(l,m):
        a,b = ab[i]
        c = a+(n-1)*b
        nc = max(nc,c)
    ans += nc
    print(ans)
    if _ < t-1:
        s = input()