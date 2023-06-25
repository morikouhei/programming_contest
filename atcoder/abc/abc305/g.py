n,m = map(int,input().split())
S = [input() for i in range(m)]
mod = 998244353


if n <= 5:
    ans = 0
    for i in range(1<<n):
        s = ""
        for j in range(n):
            if i >> j & 1:
                s += "a"
            else:
                s += "b"
        
        ok = 1
        for x in S:
            if x in s:
                ok = 0
        ans += ok

    print(ans)
    exit()




size = 1<<5

def calc(a,b):

    ans = [[0]*size for i in range(size)]

    for i in range(size):
        for j in range(size):
            for k in range(size):
                ans[i][j] += a[i][k]*b[k][j]
                ans[i][j] %= mod

    return ans




base = [[0]*size for i in range(size)]
for i in range(size):
    base[i][i] = 1


A = [[0]*size for i in range(size)]

first = []
for i in range(size):

    s = ""
    for j in range(5):
        if i >> j & 1:
            s += "a"
        else:
            s += "b"

    
    ok = 1
    for x in S:
        if x in s:
            ok = 0

    first.append(ok)

    if ok == 0:
        continue

    mask = (1<<4)-1

    ni = i // 2

    ### a
    ns = s+"a"
    na = ni+(1<<4)
    ok = 1
    for x in S:
        if x in ns:
            ok = 0
    
    if ok:
        A[na][i] += 1


    ### b
    ns = s+"b"
    nb = ni
    ok = 1
    for x in S:
        if x in ns:
            ok = 0
    
    if ok:
        A[nb][i] += 1



n -= 5
while n:
    if n & 1:
        base = calc(A,base)

    A = calc(A,A)
    n >>= 1

ans = 0
for i in range(size):
    for j in range(size):
        ans += base[i][j]*first[j]%mod
        ans %= mod
print(ans)

    