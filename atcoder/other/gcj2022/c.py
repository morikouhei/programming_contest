def solve():
    n = int(input())
    S = sorted(list(map(int,input().split())))
    ans = 0
    for s in S:
        if ans < s:
            ans += 1
    return ans


t = int(input())
for i in range(t):
    ans = solve()
    print("Case #{}:".format(i+1),end=" ")
    print(ans)