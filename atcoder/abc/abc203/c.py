n,k = map(int,input().split())
ab = [list(map(int,input().split())) for i in range(n)]
ab.sort()
now = k
ans = 0
for a,b in ab:
    if ans+now >= a:
        now -= a-ans
        ans = a
        now += b
    else:
        break
print(ans+now)