import bisect
n,k,p = map(int,input().split())
A = list(map(int,input().split()))
x = n//2
y = n-x
l = A[:x]
r = A[x:]

cand = [[] for i in range(n+1)]

for i in range(1<<x):
    count = 0
    num = 0
    for j in range(x):
        if i >> j & 1:
            count += l[j]
            num += 1
    if count > p:
        continue
    cand[num].append(count)

for i in range(n+1):
    cand[i] = sorted(cand[i])

ans = 0
for i in range(1<<y):
    count = 0
    num = 0
    for j in range(y):
        if i >> j & 1:
            count += r[j]
            num += 1
    if count > p or num > k:
        continue
    ans += bisect.bisect_right(cand[k-num],p-count)
print(ans)