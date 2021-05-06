t = int(input())
for _ in range(t):
    n = int(input())
    R = list(map(int,input().split()))
    ans = 0
    for r in R:
        if r != 2:
            ans += 1
    print(ans)