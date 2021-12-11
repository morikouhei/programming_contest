h,w,n = map(int,input().split())
C = [[int(x) for x in input()] for i in range(h)]
mod = 998244353

dp = [0]*1<<h
dp[-1] = 1

hmask = [[0]*10 for i in range(h)]
for i in range(h):
    for j in range(w):
        hmask[i][C[i][j]] |= 1<<j

wmask = [[0]*10 for i in range(w)]
for i in range(w):
    for j in range(h):
        wmask[i][C[j][i]] |= 1<<j

for i in range(2*n):
    ndp = [0]*1<<w
    for j in range(1,1<<h):
        for num in range(1,10):
            mask = 0
            for k in range(h):
                if j >> k & 1:
                    mask |= hmask[k][num]
            if mask:
                ndp[mask] += dp[j]
                ndp[mask] %= mod

    dp = ndp
    h,w = w,h
    hmask,wmask = wmask,hmask

print(sum(dp)%mod)

