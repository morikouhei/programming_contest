import sys
sys.setrecursionlimit(2*10**5)

mod = 998244353

n,m = map(int,input().split())
S = [list(input()) for i in range(n)]

dic = [[[-1]*(m+1) for i in range(n+1)] for j in range(n+1)]



def dp_last(l,r):
    if r - l > 10:
        return 0

    lma = 0
    rangeS = [S[i][m-1] for i in range(l,r)]
    for s in rangeS:
        if s == "?":
            continue
        s = int(s)
        if s < lma:
            return 0

        lma = s

    dp = [0]*10
    if rangeS[0] == "?":
        dp = [1]*10
    else:
        dp[int(rangeS[0])] = 1

    for s in rangeS[1:]:
        ndp = [0]*10
        if s == "?":
            for i in range(1,10):
                ndp[i] = sum(dp[:i])%mod
        else:
            ndp[int(s)] = sum(dp[:int(s)])%mod
    
        dp = ndp

    return sum(dp)%mod


for i in range(n):
    for j in range(i+1,n+1):
        dic[i][j][m-1] = dp_last(i,j)

    
def dfs(l,r,ind):
    global dic
    if dic[l][r][ind] != -1:
        return dic[l][r][ind]

    if ind == m:
        return 1

    lma = 0
    rangeS = [S[i][ind] for i in range(l,r)]
    for s in rangeS:
        if s == "?":
            continue
        s = int(s)
        if s < lma:
            dic[l][r][ind] = 0
            return 0

        lma = s

    dp = [[0]*10 for i in range(r-l+1)]
    dp[0][0] = 1

    for i,s in enumerate(rangeS):
        for j in range(9):
            dp[i][j+1] += dp[i][j]
            dp[i][j+1] %= mod

        if s == "?":
            x = range(10)
        else:
            x = [int(s)]
        
        for j in x:
            if dp[i][j-1] == 0:
                continue
            if i and j == 0:
                continue
            sj = str(j)
            for k in range(i,r-l):
                if rangeS[k] != "?" and rangeS[k] != sj:
                    break
                dp[k+1][j] += dp[i][j-1] * dfs(l+i,l+k+1,ind+1) % mod
                dp[k+1][j] %= mod
            
    dic[l][r][ind] = sum(dp[-1])%mod
    return dic[l][r][ind]

ans = dfs(0,n,0)
print(ans)
            