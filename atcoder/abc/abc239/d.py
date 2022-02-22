a,b,c,d = map(int,input().split())
M = 205
primes = [0]*(205)
p = []
for i in range(2,M):
    if primes[i]:
        continue
    p.append(i)
    for j in range(i,M,i):
        primes[j] = 1


for i in range(a,b+1):
    find = 0
    for j in range(c,d+1):
        if i+j in p:
            find = 1
    if find == 0:
        print("Takahashi")
        exit()
print("Aoki")