t = int(input())
def extgcd(a, b):
    # ax + by = gcd(a,b)
    # return gcd(a,b), x, y
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extgcd(b % a, a)
        return g, y - (b // a) * x, x

def chineseRem(b1, m1, b2, m2):
    # x ≡ b1 (mod m1) ∧ x ≡ b2 (mod m2) <=> x ≡ r (mod m)
    # となる(r. m)を返す
    # 解無しのとき(0, -1)
    d, p, q = extgcd(m1, m2)
    if (b2 - b1) % d != 0:
        return 0, -1
    m = m1 * (m2 // d)  # m = lcm(m1, m2)
    tmp = (b2-b1) // d * p % (m2 // d)
    r = (b1 + m1 * tmp) % m
    return r, m

for _ in range(t):
    x,y,p,q = map(int,input().split())
    ans = float("inf")
    #print(ans)
    for i in range(x,x+y):
        for j in range(p,p+q):
            r,m = chineseRem(i,2*x+2*y,j,p+q)
            if r != 0:
                ans = min(ans,r)
    if ans == float("inf"):
        ans = "infinity"
    print(ans)