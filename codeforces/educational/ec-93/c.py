from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(input())
    d = defaultdict(int)
    d[0] = 1
    ans = 0
    now = 0
    for i in range(n):
        now += int(a[i])
        x = now-i-1
        ans += d[x]
        d[x] += 1
    print(ans)