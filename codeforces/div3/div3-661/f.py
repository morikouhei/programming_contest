import sys
input = sys.stdin.buffer.readline
def solve():
    n = int(input())
    LR = [tuple(map(int,input().split())) for i in range(n)]
    s = set()
    for l,r in LR:
        s.add(l)
        s.add(r)
    dic = {x:i for i,x in enumerate(sorted(list(s)))}
    le = len(s)
    seg = [[] for i in range(le)]
    for l,r in LR:
        seg[dic[r]].append(dic[l])

    dp = [[len(seg[0])]]
    for i in range(1,le):
        dp.append(dp[-1]+[0])
        for l in sorted(seg[i],reverse=True):
            dp[i][l] += 1
            for j in range(l):
                dp[i][j] = max(dp[i][j],dp[i][l]+dp[l-1][j])
    return dp[-1][0]

t = int(input())
for _ in range(t):
    ans = solve()
    print(ans)
