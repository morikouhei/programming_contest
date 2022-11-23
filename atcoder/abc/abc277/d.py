n,m = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
sa = sum(A)
ans = sa-max(A)
last = A[0]
now = 0
first = -1
for a in A:
    if a == last or a == last+1:
        now += a
        last = a
    else:
        ans = min(ans,sa-now)
        if first == -1:
            first = now
        now = a
        last = a


if (A[-1]+1)%m == A[0]:
    if first == -1:
        ans = 0
    else:
        ans = min(ans,sa-now-first)
else:
    ans = min(ans,sa-now)
print(ans)