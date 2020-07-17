t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    ans = 0
    now = 0
    for i in s:
        if i == ")":
            now -= 1
        else:
            now += 1
        ans = min(ans,now)
    print(-ans)