inf = 10**20
def calc(zero,one,c):

    lz = len(zero)
    lo = len(one)
    dp = [[inf]*(lo+1) for i in range(lz+1)]
    dp[0][0] = 0
    for i in range(lz+1):
        for j in range(lo+1):
            if dp[i][j] == inf:
                continue

            z1 = zero[i]
            o1 = one[j]
            dp[i+1][j] = min(dp[i+1][j],dp[i][j]+z1*2)
            dp[i][j+1] = min(dp[i][j+1],dp[i][j]+o1*2)
            dp[i+1][j+1] = min(dp[i+1][j+1],dp[i][j]+max(z1,o1)*2)
            if i < lz-1:
                dp[i+2][j] = min(dp[i+2][j],dp[i][j]+zero[i+1]*2+c)
            if j < lo-1:
                dp[i][j+2] = min(dp[i][j+2],dp[i][j]+one[j+1]*2+c)
    return dp[-2][-2]


def solve():
    n,c = map(int,input().split())
    XS = [list(map(int,input().split())) for i in range(n)]

    ans = 0
    zero = [inf]
    one = [inf]
    for x,s in XS:
        if x >= 0:
            if s:
                one.append(x)
            else:
                zero.append(x)
    one.sort()
    zero.sort()
    ans += calc(zero,one,c)

    zero = [inf]
    one = [inf]
    for x,s in XS:
        if x <= 0:
            if s:
                one.append(-x)
            else:
                zero.append(-x)
    one.sort()
    zero.sort()
    ans += calc(zero,one,c)
    return ans
t = int(input())
for i in range(t):
    ans = solve()
    print("Case #{}:".format(i+1),end=" ")
    print(ans)