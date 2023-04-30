n,p = map(int,input().split())

primes = []
count = [0]*(p+1)
for i in range(2,p+1):
    if count[i]:
        continue
    primes.append(i)
    for j in range(i,p+1,i):
        count[j] = 1



d1 = [1]
d2 = [1]

def add(d,p):

    le = len(d)
    for i in range(le):
        x = d[i]*p

        while x <= n:
            d.append(x)
            x *= p
    
    return d
for p in primes:
    if len(d2) < len(d1):
        d1,d2 = d2,d1

    d1 = add(d1,p)

d1.sort()
d2.append(0)
d2.sort()

r = len(d2)-1

ans = 0
for d in d1:
    lim = n//d
    while r and d2[r] > lim:
        r -= 1
    
    ans += r
print(ans)