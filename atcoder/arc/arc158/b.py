import math
n = int(input())
mod = 998244353

divs = set()
for i in range(1,int(n**0.5)+1):
    if n%i:
        continue
    divs.add(i)
    divs.add(n//i)

divs = sorted(divs)
le = len(divs)
primes = []


for i in range(2,int(n**0.5)+1):
    if n%i:
        continue
    primes.append(i)
    while n % i == 0:
        n //= i

if n != 1:
    primes.append(n)

div_count = [[0]*len(primes) for i in range(le)]

for i,div in enumerate(divs):
    now = div
    for j,prime in enumerate(primes):
        while now%prime == 0:
            now //= prime
            div_count[i][j] += 1

dp = [0]*le
dp[0] = 1
lp = len(primes)

for i in range(le-1):
    for j in range(i+1,le):
        if divs[j]%divs[i]:
            continue
        pat = 1
        for x in range(lp):
            if div_count[i][x] == div_count[j][x]:
                pat *= div_count[i][x]+1
                pat %= mod
        dp[j] += dp[i]*pat
        dp[j] %= mod
print(dp[-1])