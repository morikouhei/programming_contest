h,w = map(int,input().split())
a = [list(map(int,input().split())) for i in range(h)]
mi = 1000
for i in a:
    mi = min(mi,min(i))

ans = 0
for i in a:
    for j in i:
        ans += j-mi
print(ans)