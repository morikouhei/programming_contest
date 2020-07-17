t = int(input())
for _ in range(t):
    n = int(input())
    l = sorted(list(map(int,input().split())))
    ans = float("INF")
    for i in range(n-1):
        ans = min(ans,l[i+1]-l[i])
    print(ans)