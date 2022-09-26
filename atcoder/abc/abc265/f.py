n,d = map(int,input().split())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))
mod = 998244353

md = d+1
dp = [[0]*md for i in range(md)]
dp[0][0] = 1

for p,q in zip(P,Q):
    dif = abs(p-q)
    ndp1 = [[0]*md for i in range(md)]
    ndp2 = [[0]*md for i in range(md)]

    for i in range(md):
        for j in range(md):
            if dp[i][j] == 0:
                continue
            x = dp[i][j]

            ni,nj = i+dif,j
            if ni < md:
                ndp1[ni][nj] += x
                ndp1[nj][nj] %= mod

            if dif:
                ni,nj = i,j+dif
            else:
                ni,nj = i+1,j+1
            if ni < md and nj < md:
                ndp1[ni][nj] += x
                ndp1[nj][nj] %= mod

            if dif == 0:
                continue

            ni,nj = i+dif-1,j+1
            if ni >= md:
                di = ni-(md-1)
                ni,nj = ni-di,nj+di
            if 0 <= ni < md and 0 <= nj < md:
                ndp2[ni][nj] += x
                ndp2[ni][nj] %= mod
            else:
                continue

            ni,nj = i,j+dif

            if 0 <= ni < md and 0 <= nj < md:
                ndp2[ni][nj] -= x
                ndp2[ni][nj] %= mod

    for i in range(md):
        for j in range(md):
            if i < md-1 and j < md-1:
                ndp1[i+1][j+1] += ndp1[i][j]
                ndp1[i+1][j+1] %= mod

    for i in range(md)[::-1]:
        for j in range(md):
            ni,nj = i-1,j+1
            if 0 <= ni < md and 0 <= nj < md:
                ndp2[ni][nj] += ndp2[i][j]
                ndp2[ni][nj] %= mod
            ndp1[i][j] = (ndp1[i][j]+ndp2[i][j])%mod
    dp = ndp1

ans = 0

for i in dp:
    ans += sum(i)%mod
    ans %= mod
print(ans)        

            
