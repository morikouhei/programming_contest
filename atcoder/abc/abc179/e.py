n,x,m = map(int,input().split())

l = []
ans = 0
for i in range(n):
    if x in l:
        d = l.index(x)
        ans += sum(l[:d])
        le = len(l)-d
        count = sum(l[d:])
        n -= d
        ans += count*(n//le)
        n %= le
        for k in range(d,d+n):
            ans += l[k]
        print(ans)
        exit()
    l.append(x)
    x = (x**2)%m

print(sum(l))
