t = int(input())
def extgcd(a, b):
    # ax + by = gcd(a,b)
    # return gcd(a,b), x, y
    if a == 0:
        return b, 0, 1
    else:
        g, x,y = extgcd(b % a, a)
        return g, y - (b // a) * x, x

def chineseRem(b1, m1, b2, m2):
    # 中国剰余定理
    # x ≡ b1 (mod m1) ∧ x ≡ b2 (mod m2) <=> x ≡ r (mod m)
    # となる(r. m)を返す
    # 解無しのとき(0, -1)
    d, p, q = extgcd(m1, m2)
    if (b2 - b1) % d != 0:
        return -1, -1
    m = m1 * (m2 // d)  # m = lcm(m1, m2)
    tmp = (b2-b1) // d * p % (m2 // d)
    r = (b1 + m1 * tmp) % m
    return r, m
for _ in range(t):
    n,s,k = map(int,input().split())
    x,y = chineseRem(n-s,n,0,k)
    print(x//k)
