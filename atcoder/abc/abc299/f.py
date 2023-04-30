S = [ord(s)-ord("a") for s in input()]
n = len(S)
mod = 998244353

inf = 1<<10
nex = [[inf]*26 for i in range(n+1)]
for i in range(n)[::-1]:
    x = S[i]
    for j in range(26):
        nex[i][j] = nex[i+1][j]

    nex[i][x] = i

ans = 0

for l in range(1,n):

    dp = [[0]*n for i in range(n)]
    s = S[l]
    if nex[0][s] == l:
        continue
    dp[nex[0][s]][l] = 1
    for a in range(l):
        for b in range(l,n):
            if dp[a][b] == 0:
                continue
            
            for x in range(26):
                na = nex[a+1][x]
                nb = nex[b+1][x]
                if na >= l or nb == inf:
                    continue
                dp[na][nb] += dp[a][b]
                dp[na][nb] %= mod

    for a in range(l):
        for b in range(l,n):
            if nex[a+1][s] >= l:
                ans += dp[a][b]
                ans %= mod
print(ans)