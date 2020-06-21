from collections import defaultdict

n = int(input())
a = list(map(int,input().split()))
ans = sum(a)
d = defaultdict(int)
for i in a:
    d[i] += 1

q = int(input())
for _ in range(q):
    b,c = map(int,input().split())
    count = d[b]
    ans += (c-b)*count
    print(ans)
    d[b] = 0
    d[c] += count
