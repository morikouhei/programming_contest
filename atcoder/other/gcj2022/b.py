def solve():
    CMYK = [list(map(int,input().split())) for i in range(3)]
    mi = CMYK[0]
    for i in range(3):
        for j in range(4):
            mi[j] = min(mi[j],CMYK[i][j])
    
    ans = []
    num = 10**6
    for i in range(4):
        if mi[i] <= num:
            ans.append(mi[i])
            num -= mi[i]
        else:
            ans.append(num)
            num = 0
    if num:
        return ["IMPOSSIBLE"]
    else:
        return ans


t = int(input())
for i in range(t):
    ans = solve()
    print("Case #{}:".format(i+1),end=" ")
    print(*ans)