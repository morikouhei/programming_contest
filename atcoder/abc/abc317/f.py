import math

n,*A = map(int,input().split())
tn = n
n += 1
mod = 998244353

dp = [[[[[[0]*A[2] for i in range(A[1])] for j in range(A[0])] for k in range(2)] for l in range(2)] for m in range(2)]
dp[1][1][1][0][0][0] = 1

for i in range(60)[::-1]:
    ndp = [[[[[[0]*A[2] for _ in range(A[1])] for j in range(A[0])] for k in range(2)] for l in range(2)] for m in range(2)]
    
    b = n >> i & 1

    for f0 in range(2):
        for f1 in range(2):
            for f2 in range(2):
                for a0 in range(A[0]):
                    for a1 in range(A[1]):
                        for a2 in range(A[2]):
                            if dp[f0][f1][f2][a0][a1][a2] == 0:
                                continue
                            
                            for nb in [0,3,5,6]:

                                if b == 0:
                                    if f0 and nb >> 0 & 1:
                                        continue
                                    if f1 and nb >> 1 & 1:
                                        continue
                                    if f2 and nb >> 2 & 1:
                                        continue

                                nf0 = f0
                                if b and nf0 and (nb >> 0 & 1) == 0:
                                    nf0 = 0

                                nf1 = f1
                                if b and nf1 and (nb >> 1 & 1) == 0:
                                    nf1 = 0
                                
                                nf2 = f2
                                if b and nf2 and (nb >> 2 & 1) == 0:
                                    nf2 = 0

                                na0 = a0+(1<<i) if nb >> 0 & 1 else a0
                                na1 = a1+(1<<i) if nb >> 1 & 1 else a1
                                na2 = a2+(1<<i) if nb >> 2 & 1 else a2
                                na0 %= A[0]
                                na1 %= A[1]
                                na2 %= A[2]

                                ndp[nf0][nf1][nf2][na0][na1][na2] += dp[f0][f1][f2][a0][a1][a2]
                                ndp[nf0][nf1][nf2][na0][na1][na2] %= mod

    dp = ndp

ans = dp[0][0][0][0][0][0] - 1

ans -= tn//math.lcm(A[0],A[1])
ans -= tn//math.lcm(A[1],A[2])
ans -= tn//math.lcm(A[2],A[0])
ans %= mod
print(ans)