import math

def extgcd(a, b):
    # ax + by = gcd(a,b)
    # return gcd(a,b), x, y
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extgcd(b % a, a)
        return g, y - (b // a) * x, x


n,a,b,c,x = map(int,input().split())

if x < a+b+c:
    print(0)
    exit()

x -= a+b+c

## 0 <= i,j,k < n

g = math.gcd(b,c)
nb,nc = b//g,c//g
ans = 0
for i in range(n):
    nx = x-a*i
    if nx < 0:
        break
    
    if nx%g:
        continue
    nx //= g
    _,j,k = extgcd(nb,nc)
    j *= nx
    k *= nx

    ans += max(0,min(j//nc,(n-k-1)//nb) - max((-k+nb-1)//nb,(j-n+nc)//nc)+1)
print(ans)
    ## b * j + c * k = nx
    ## b * (j - c * t) + c * (k + b * t) = nx
    ## 0 <= j - c * t < n
    ## c * t <= j , j - n < c * t
    ## t <= j/c , (j-n)/c < t <= j/c

    ## 0 <= k + b * t < n
    ## -k <= b*t , b*t < n-k
    ## -k/b <= t < (n-k)/b
    
