import math
n = int(input())
X = list(map(int,input().split()))

prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
base = 1
cand = set()
for x in X:
    check = False
    for p in prime:
        if x%p == 0:
            check = True
            cand.add(p)
    if check == False:
        base *= x

ans = float("INF")
l = list(cand)
n2 = 1 << len(l)

for i in range(n2):
    count = base
    for j in range(len(l)):
        if i >> j & 1:
            count *= l[j]
    
    check = True
    for x in X:
        if math.gcd(x,count) == 1:
            check = False
            break
    if check:
        ans = min(ans,count)
print(ans)