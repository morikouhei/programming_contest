import bisect
n = int(input())
M = 10**6+5
count = [0]*M
primes = []

for i in range(2,M):
    if count[i]:
        continue
    primes.append(i)
    for j in range(i,M,i):
        count[j] = 1

primes.append(n+5)
ans = 0

le = len(primes)
for i,a in enumerate(primes):

    a2 = a**2
    lim = le-1
    for j in range(i+1,le):
        b = primes[j]
        if a2*b > n:
            break
        while lim > j and a2*b*primes[lim]**2 > n:
            lim -= 1

        if lim == j:
            break
        ans += lim-j

print(ans)

