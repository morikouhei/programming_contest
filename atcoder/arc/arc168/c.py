n,k = map(int,input().split())
S = input()
mod = 998244353

### for bigger prime 
N = n+5
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


ans = 0

A,B,C = S.count("A"),S.count("B"),S.count("C")

for ab in range(k+1):
    for ac in range(k+1-ab):
        if ab+ac > A:
            break

        for bc in range(k+1-ab-ac):
            for ba in range(k+1):
                if ba+bc > B:
                    break

                aa = A - ab - ac
                bb = B - ba - bc
                ca = A - aa - ba
                cb = B - bb - ab
                cc = C - ca - cb
                
                if ca < 0 or cb < 0 or cc < 0:
                    continue

                nab,nac = ab,ac
                nba,nbc = ba,bc
                nca,ncb = ca,cb

                mab = min(nab,nba)
                nab -= mab
                nba -= mab

                mac = min(nac,nca)
                nac -= mac
                nca -= mac

                mbc = min(nbc,ncb)
                nbc -= mbc
                ncb -= mbc


                if mab + mac + mbc > k:
                    continue

                if nab != nbc or nbc != nca:
                    continue
                if nba != ncb or ncb != nac:
                    continue
                if mab + mac + mbc + (nab+nbc+nca+nba+ncb+nac)//3*2 > k:
                    continue
                
                ans += nCr(A,aa) * nCr(A-aa,ab) % mod * nCr(B,ba) * nCr(B-ba,bb) % mod * nCr(C,ca) * nCr(C-ca,cc) % mod
                ans %= mod
print(ans) 

