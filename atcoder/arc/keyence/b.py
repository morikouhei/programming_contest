n,k = map(int,input().split())
from collections import Counter

a = list(map(int,input().split()))
ans = 0
c = Counter(a)
now = k

for i in range(n+1):
    if i in c:
        if c[i] >= now:
            continue
        dif = now-c[i]
        ans += dif*i
        now = c[i]
    else:
        ans += now*i
        break
    
print(ans)