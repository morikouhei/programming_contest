n = int(input())
a = list(map(int,input().split()))
l = [0]*32

for i in a:
    for j in range(32):
        if i >> j & 1:
            l[j] += 1

ans = [0]*n

for i in range(32):
    if l[i]%2 == 0:
        for j in range(n):
            if a[j]>>i & 1:
                ans[j] += 1<<i
    else:
        for j in range(n):
            if not a[j] >> i & 1:
                ans[j] += 1<<i
print(*ans)