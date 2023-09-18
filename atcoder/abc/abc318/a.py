n,m,p = map(int,input().split())
ans = 0
now = m
while now <= n:
    ans += 1
    now += p
print(ans)