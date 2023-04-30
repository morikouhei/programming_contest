def calc(s,r):

    s = list(map(int,str(s)))
    ls = len(s)

    rs = []
    while r:
        r,m = divmod(r,10)
        rs.append(m)
    
    rs = rs[::-1]

    lr = len(rs)

    ans = 0
    for si in range(lr-ls+1):
        dp = [[0]*2 for i in range(2)]
        dp[0][0] = 1

        ## 0,1 same,lower to r
        ## 0,1 leading 0 or not

        for i in range(lr):
            ndp = [[0]*2 for i in range(2)]
            for j in range(2):
                for k in range(2):
                    for d in range(10):

                        if j == 0 and rs[i] < d:
                            continue

                        nk = 1 if (k or d) else 0

                        nj = j
                        if j == 0 and rs[i] > d:
                            nj = 1

                        if si <= i < si+ls:
                            if d != s[i-si]:
                                continue
                            if nk == 0 and d == 0:
                                continue
                            ndp[nj][nk] += dp[j][k]

                            continue

                        ndp[nj][nk] += dp[j][k]

            dp = ndp
        ans += dp[0][1] + dp[1][1]

    return ans


def solve():
    s,l,r = input().split()
    l,r = int(l),int(r)

    return calc(s,r) - calc(s,l-1)


t = int(input())

for _ in range(t):
    print(solve())

