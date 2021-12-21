n = int(input())
P = list(map(int,input().split()))

divs = [[] for i in range(n+1)]
for i in range(2,n+1):
    for j in range(i,n+1,i):
        divs[j].append(i)


mu = [-1]*(n+1)
prime = [1]*(n+1)
for i in range(2,n+1):
    if prime[i] == 0:
        continue
    for j in range(i,n+1,i):
        mu[j] *= -1
        prime[j] = 0

    for j in range(i**2,n+1,i**2):
        mu[j] = 0

ans = 0
count = [0]*(n+1)

for i in range(2,n+1):
    if mu[i] == 0:
        continue

    num = 0
    for j in range(i-1,n,i):
        for d in divs[P[j]]:
            count[d] += 1

    for j in range(i-1,n,i):
        for d in divs[P[j]]:
            if count[d]:
                num += count[d]*(count[d]+1)//2*mu[d]
                count[d] = 0
    ans += mu[i]*num
print(ans)
