n,x = map(int,input().split())
Y = list(map(int,input().split()))
Z = list(map(int,input().split()))
if x < 0:
    x = -x
    Y = [-y for y in Y]
    Z = [-z for z in Z]

inf = 10**20
S = sorted(Y+Z+[0,x])
dic = {x:i for i,x in enumerate(S)}
dicy = {y:i for i,y in enumerate(Y)}
dicz = {z:i for i,z in enumerate(Z)}
le = len(S)

s,x = dic[0],dic[x]
Y = [dic[y] for y in Y]
Z = [dic[z] for z in Z]

dp = [[[inf]*le for i in range(le)] for j in range(2)]
dp[0][s][s] = 0

ans = inf
for l in range(s+1)[::-1]:
    for r in range(l,le):
        dif = S[r]-S[l]
        dp[0][l][r] = min(dp[0][l][r],dp[1][l][r]+dif)
        dp[1][l][r] = min(dp[1][l][r],dp[0][l][r]+dif)

        if l >= 1:
            nl = l-1
            pos = S[nl]
            if pos in dicy:
                h = Z[dicy[pos]]
                if l <= h <= r:
                    dp[0][nl][r] = min(dp[0][nl][r],dp[0][l][r]+S[l]-S[nl])
            else:
                dp[0][nl][r] = min(dp[0][nl][r],dp[0][l][r]+S[l]-S[nl])

        if r < le-1:
            nr = r+1
            pos = S[nr]
            if pos in dicy:
                h = Z[dicy[pos]]
                if l <= h <= r:
                    dp[1][l][nr] = min(dp[1][l][nr],dp[1][l][r]+S[nr]-S[r])
            else:
                dp[1][l][nr] = min(dp[1][l][nr],dp[1][l][r]+S[nr]-S[r])

        if l <= x <= r:
            ans = min(ans,dp[0][l][r])
            ans = min(ans,dp[1][l][r])
if ans == inf:
    ans = -1
print(ans)