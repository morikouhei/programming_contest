
import bisect
n,m,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.append(float("INF"))
b.append(float("INF"))
la = [a[0]]
lb = [b[0]]
for i in range(1,n):
    la.append(la[-1]+a[i])
for i in range(1,m):
    lb.append(lb[-1]+b[i])
ans = 0
for i in range(n):
    if la[i] > k:
        break
    x = k-la[i]

    count = i+1
    ind = bisect.bisect_right(lb,x)
    count += ind
    ans = max(ans,count)
for i in range(m):
    if lb[i] > k:
        break
    x = k-lb[i]

    count = i+1
    ind = bisect.bisect_right(la,x)
    count += ind
    ans = max(ans,count)
print(ans)
