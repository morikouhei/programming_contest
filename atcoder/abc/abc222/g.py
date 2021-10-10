
def extgcd(a, b):
    # ax + by = gcd(a,b)
    # return gcd(a,b), x, y
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extgcd(b % a, a)
        return g, y - (b // a) * x, x

def extinv(a,mod):
    g,x,y = extgcd(a,mod)
    if g != 1:
        return -1
    return x%mod

def solve():
    k = int(input())
    if k%2 == 0:
        k //= 2
    k *= 9
    if k%2 == 0 or k%5 == 0:
        return -1

    D = {}
    sq = int(k**0.5)+1
    Z = 1
    for i in range(sq):
        Z *= 10
        Z %= k
        D[Z] = i+1
        if 1 in D:
            return D[1]
    
    R = extinv(Z,k)
    Y = 1
    for i in range(1,sq+1):
        Y *= R
        Y %= k
        if Y in D:
            return D[Y]+i*sq
    return -1

    


t = int(input())

for _ in range(t):
    print(solve())