from collections import Counter
n = int(input())
l = list(map(int,input().split()))
c = Counter(l)
l = list(set(l))
ans = 0
l.sort()

n = len(l)
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if l[i]+l[j] > l[k] and l[i]+l[k] > l[j] and l[j]+l[k]>l[i]:
                ans += c[l[i]]*c[l[j]]*c[l[k]]
print(ans)