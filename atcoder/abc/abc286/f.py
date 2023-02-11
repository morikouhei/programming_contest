import sys

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

l = [23, 19, 17, 13, 11, 9, 7, 5, 4]
print(sum(l))
sys.stdout.flush()
A = []

now = 1
for x in l:
    a = [now+i for i in range(x)]
    a = a[1:]+[a[0]]
    A += a
    now += x
print(*A)
sys.stdout.flush()

r,m = 0,1
B = list(map(int,input().split()))
now = 0
for x in l:
    b = B[now:now+x]
    a = [i+1+now for i in range(x)]
    # print(a)
    for i in range(x+1):
        if a == b:
            nm = i
            break
        a = a[1:] + [a[0]]
    # print(x,nm)
    r,m = chineseRem(r,m,nm,x)
    now += x
    # print(r,m)

print(r)
sys.stdout.flush()
