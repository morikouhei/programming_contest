n,m = map(int,input().split())
M = 2*10**6+5
divisor = [0]*M
divisor[1] = 1
for i in range(2,M):
    if divisor[i]:
        continue
    for j in range(i,M,i):
        if divisor[j]:
            continue
        divisor[j] = i
 
def primes(x):
    cand = []
    while x != 1:
        p = divisor[x]
        cand.append(p)
        while divisor[x] == p:
            x //= p
    return cand

cand = [0]*(m+1)
A = list(map(int,input().split()))
for a in A:
    for j in primes(a):
        if j > m or cand[j]:
            continue
        for i in range(j,m+1,j):
            cand[i] = 1

print(m-sum(cand))
for i in range(1,m+1):
    if cand[i]:
        continue
    print(i)