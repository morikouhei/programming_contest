n = int(input())
R = list(map(int,input().split()))
C = list(map(int,input().split()))
mod = 998244353

sR = sum(R)
sC = sum(C)
if sR != sC:
    print(0)
    exit()

num = [0]*3
for c in C:
    num[c] += 1

m = num[2]+1
dp = [0]*m
dp[-1] = 1

for r in R:
    if r == 0:
        continue
    ndp = [0]*m

    for i in range(m):
        if dp[i] == 0:
            continue
        j = sC-2*i
        if j < 0:
            continue
        if r == 1:
            if i:
                ndp[i-1] += dp[i]*i
                ndp[i-1] %= mod
            if j:
                ndp[i] += dp[i]*j
                ndp[i] %= mod

        else:
            if j >= 2:
                ndp[i] += dp[i]*(j*(j-1)//2)
                ndp[i] %= mod
            
            if i >= 1 and j >= 1:
                ndp[i-1] += dp[i]*i*j
                ndp[i-1] %= mod
            if i >= 1:
                ndp[i-1] += dp[i]*i
                ndp[i-1] %= mod
            
            if i >= 2:
                ndp[i-2] += dp[i]*(i*(i-1)//2)
                ndp[i-2] %= mod
    dp = ndp
    sC -= r
print(dp[0])