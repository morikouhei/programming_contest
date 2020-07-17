t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    c = set()
    r = set()
    l = [list(map(int,input().split())) for i in range(n)]
    for i in range(n):
        for j in range(m):
            if l[i][j] == 1:
                c.add(i)
                r.add(j)
    x = n-len(c)
    y = m-len(r)
    print("Ashish" if min(x,y)%2 else "Vivek")