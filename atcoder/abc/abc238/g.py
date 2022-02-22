import random
n,q = map(int,input().split())
A = list(map(int,input().split()))
M = 10**6+1
primes = set()
use = [0]*M
for i in range(2,M):
    if use[i]:
        continue
    primes.add(i)
    for j in range(i,M,i):
        if use[j]:
            continue
        use[j] = i


l = len(primes)

hx = {}
hy = {}
for p in primes:
    hx[p] = random.randint(M,10**9)
    hy[p] = random.randint(M,10**9)
count = {}

cum = [0]*(n+1)
for i,a in enumerate(A):
    now = 0
    while a != 1:
        p = use[a]
        a //= p
        num = count.get(p,0)
        if num == 0:
            now ^= hx[p]
        elif num == 1:
            now ^= hy[p]
        else:
            now ^= hx[p]^hy[p]
        count[p] = (num+1)%3

    cum[i+1] = cum[i]^now


for i in range(q):
    l,r = map(int,input().split())
    l -= 1
    print("Yes" if cum[l] == cum[r] else "No")