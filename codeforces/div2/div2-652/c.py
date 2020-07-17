t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    a = [int(i) for i in input().split()]
    w = [int(i) for i in input().split()]
    a.sort()
    ans = sum(a[-k:])
    if 1 in w:
        ans += sum(a[-w.count(1):])
    w.sort(reverse=True)
    now = 0
    for i in w:
        if i > 1:
            ans += a[now]
            now += i-1
    print(ans)
