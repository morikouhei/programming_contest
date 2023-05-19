h,w = map(int,input().split())
S = [list(input()) for i in range(h)]

mod = 998244353

### for bigger prime 
N = h+w+5
fact = [1]*N
finv = [1]*N
 
for i in range(2,N):
    fact[i] = (fact[i-1]*i)%mod
finv[-1] = pow(fact[-1],mod-2,mod)
for i in range(1,N)[::-1]:
    finv[i-1] = (finv[i]*i)%mod

def nCr(n,r):
    if r > n:
        return 0
    else: 
        return fact[n]*finv[r]%mod*finv[n-r]%mod



dp_score = [[0]*w for i in range(h)]
dp_same = [[0]*w for i in range(h)]

for i in range(h):
    for j in range(w):
        s = S[i][j]

        if i < h-1:
            dp_score[i+1][j] += dp_score[i][j]
            dp_score[i+1][j] %= mod

            dp_same[i+1][j] += dp_same[i][j]
            dp_same[i+1][j] %= mod

            ns = S[i+1][j]

            if s == ns == "Y":
                dp_score[i+1][j] += 2*dp_same[i][j] + nCr(i+j,i)
                dp_score[i+1][j] %= mod

                dp_same[i+1][j] += nCr(i+j,j)
                dp_same[i+1][j] %= mod



        if j < w-1:
            dp_score[i][j+1] += dp_score[i][j]
            dp_score[i][j+1] %= mod

            dp_same[i][j+1] += dp_same[i][j]
            dp_same[i][j+1] %= mod

            ns = S[i][j+1]

            if s == ns == "Y":
                dp_score[i][j+1] += 2*dp_same[i][j] + nCr(i+j,i)
                dp_score[i][j+1] %= mod

                dp_same[i][j+1] += nCr(i+j,j)
                dp_same[i][j+1] %= mod


print(dp_score[-1][-1])