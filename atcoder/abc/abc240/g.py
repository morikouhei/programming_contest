n,x,y,z = map(int,input().split())
mod = 998244353
x,y,z = abs(x),abs(y),abs(z)

if x+y+z > n:
    print(0)
    exit()

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

X = x+y
Y = abs(x-y)

ans = 0
for i in range(z,n+1):
    if (i-z)%2:
        continue
    left = n-i
    if left < X or left < Y:
        continue
    if (left-X)%2 or (left-Y)%2:
        continue

    zmove = nCr(n,z+(i-z)//2)*nCr(n-(z+(i-z)//2),(i-z)//2)%mod
    
    xmove = nCr(left,X+(left-X)//2)
    ymove = nCr(left,Y+(left-Y)//2)
    ans += zmove*xmove%mod*ymove%mod
    ans %= mod
print(ans)