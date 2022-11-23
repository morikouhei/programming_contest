from collections import Counter
import random
n = int(input())
A = list(map(int,input().split()))

def check(x):

    C = Counter([a%x for a in A])
    if C.most_common(1)[0][1]*2 > n:
        print(x)
        exit()
    return 1

check(4)
for i in range(20):
    x = A[random.randint(0,n-1)]
    y = A[random.randint(0,n-1)]
    if x == y:
        continue
    dif = abs(x-y)

    for j in range(3,int(dif**0.5)+1):
        if dif%j:
            continue
        check(j)
        while dif%j == 0:
            dif //= j
    if dif > 2:
        check(dif)
print(-1)