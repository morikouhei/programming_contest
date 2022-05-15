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

ans = 0

l = len(primes)

now = 0
for i in range(l)[::-1]:
    p = primes[i]
    x = p**3

    while now < i and x*primes[now] <= n:
        now += 1

    ans += min(now,i)
  
print(ans)