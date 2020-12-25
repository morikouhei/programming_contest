n = int(input())
a = list(map(int,input().split()))
a.sort()
s = sum(a)
ans = 0
for i in range(n-1):
    s -= a[i]
    ans += s-a[i]*(n-1-i)
print(ans)