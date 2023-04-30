n,m = map(int,input().split())
l = []
for i in range(m):
    c = int(input())
    A = list(map(int,input().split()))
    count = 0
    for a in A:
        count += 1<<(a-1)
    l.append(count)
mask = (1<<n)-1
ans = 0
for i in range(1<<m):
    num = 0
    for j in range(m):
        if i >> j & 1:
            num |= l[j]
    if num == mask:
        ans += 1
print(ans)